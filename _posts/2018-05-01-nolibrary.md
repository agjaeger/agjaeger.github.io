---
layout: 	post
title:  	"Creating an OpenGL Context without libraries"
date:   	2018-05-01
category: 	"opengl experiments"
tag:		blog
---

I grew tired of using libraries like SDL, GLFW, and QT. I wanted to 
learn how to create an OpenGL context without any real libraries.

This code relies on merely the X11 window handling and the OpenGL 
extensions in the operating system. I should note that the code is thus 
OS-dependent.

The full code can be located [here](https://github.com/agjaeger/opengl-experiments/blob/master/no-library/main.cpp)

There are a few steps for an OpenGL application
1. Initialize an X display
2. Find the best frame buffer configuration that is supported by the display
3. Create an X window and map it into the display
4. Create an initialize an OpenGL Context
5. Run your application loop
6. Deallocate window, display, and context once you are done

At the end of the day, you should have something like this

{% include image name="nolibrary.png" caption="An OpenGL Application with minimal libraries" %}

## Code
<hr>

### Step 1
{% highlight c %}
Display *display = XOpenDisplay(NULL);
	
if (!display) {
	printf("Failed to open X display\n");
	exit(1);
}
{% endhighlight %}

### Step 2
{% highlight c %}
printf( "Getting matching framebuffer configs\n" );

// Get a matching FB config
static int visual_attribs[] = {
	GLX_X_RENDERABLE    , True,
	GLX_DRAWABLE_TYPE   , GLX_WINDOW_BIT,
	GLX_RENDER_TYPE     , GLX_RGBA_BIT,
	GLX_X_VISUAL_TYPE   , GLX_TRUE_COLOR,
	GLX_RED_SIZE        , 8,
	GLX_GREEN_SIZE      , 8,
	GLX_BLUE_SIZE       , 8,
	GLX_ALPHA_SIZE      , 8,
	GLX_DEPTH_SIZE      , 24,
	GLX_STENCIL_SIZE    , 8,
	GLX_DOUBLEBUFFER    , True,
	//GLX_SAMPLE_BUFFERS  , 1,
	//GLX_SAMPLES         , 4,
	None
};

int fbcount;
GLXFBConfig* fbc = glXChooseFBConfig(display, DefaultScreen(display), visual_attribs, &fbcount);
if (!fbc) {
	printf("Failed to retrieve a framebuffer config\n");
	exit(1);
}

printf("Found %d matching FB configs.\n", fbcount);

// Pick the FB config/visual with the most samples per pixel
printf("Getting XVisualInfos\n");
int best_fbc = -1, worst_fbc = -1, best_num_samp = -1, worst_num_samp = 999;

int i;
for (i=0; i<fbcount; ++i) {
	XVisualInfo *vi = glXGetVisualFromFBConfig( display, fbc[i] );
	if (vi) {
		int samp_buf, samples;
		glXGetFBConfigAttrib( display, fbc[i], GLX_SAMPLE_BUFFERS, &samp_buf );
		glXGetFBConfigAttrib( display, fbc[i], GLX_SAMPLES       , &samples  );
  
		printf(
			"Matching fbconfig %d, visual ID 0x%2x: SAMPLE_BUFFERS = %d, SAMPLES = %d\n",
			i, vi -> visualid, samp_buf, samples
		);

		if (best_fbc < 0 || samp_buf && samples > best_num_samp)
			best_fbc = i, best_num_samp = samples;
		if (worst_fbc < 0 || !samp_buf || samples < worst_num_samp)
			worst_fbc = i, worst_num_samp = samples;
	}
	XFree(vi);
}

GLXFBConfig bestFbc = fbc[best_fbc];
{% endhighlight %}	

### Step 3
{% highlight c %}
// Get a visual
XVisualInfo *vi = glXGetVisualFromFBConfig(display, bestFbc);
printf("Chosen visual ID = 0x%x\n", vi->visualid);

printf("Creating colormap\n");
XSetWindowAttributes swa;
Colormap cmap;
swa.colormap = cmap = XCreateColormap(
	display,
	RootWindow(display, vi->screen), 
	vi->visual, 
	AllocNone 
);

swa.background_pixmap = None ;
swa.border_pixel      = 0;
swa.event_mask        = StructureNotifyMask;

printf("Creating window\n");
Window win = XCreateWindow(
	display, 
	RootWindow(display, vi->screen), 
	0, 0, 
	400, 400,
	0, vi->depth, 
	InputOutput, 
	vi->visual, 
	CWBorderPixel|CWColormap|CWEventMask, 
	&swa 
);

if (!win) {
	printf( "Failed to create window.\n" );
	exit(1);
}

// Done with the visual info data
XFree(vi);

XStoreName(display, win, "GL 3.0 Window");
printf("Mapping window\n");

XMapWindow(display, win);
{% endhighlight %}

### Step 4
{% highlight c %}
// Build opengl context	
int context_attribs[] = {
	GLX_CONTEXT_MAJOR_VERSION_ARB, 3,
	GLX_CONTEXT_MINOR_VERSION_ARB, 0,
	//GLX_CONTEXT_FLAGS_ARB        , GLX_CONTEXT_FORWARD_COMPATIBLE_BIT_ARB,
	None
};

printf("Creating context\n");
GLXContext ctx = glXCreateNewContext(
	display, 
	bestFbc, 
	GLX_RGBA_TYPE, 
	0, 
	True 
);

XMapWindow(display, win);
glXMakeCurrent(display, win, ctx);

int major = 0, minor = 0;
glGetIntegerv(GL_MAJOR_VERSION, &major);
glGetIntegerv(GL_MINOR_VERSION, &minor);

printf(
	"OpenGL context created.\nVersion %d.%d\nVendor %s\nRenderer %s\n",
	major, minor,
	glGetString(GL_VENDOR),
	glGetString(GL_RENDERER)
);
{% endhighlight %}

### Step 5
{% highlight c %}
// Application_loop
while (1) {
	glClearColor(0, 0.5, 1, 1);
	glClear(GL_COLOR_BUFFER_BIT);
	glXSwapBuffers (display, win);	
}
{% endhighlight %}

### Step 6
{% highlight c %}
// Destroy display and context
glXMakeCurrent(display, 0, 0);
glXDestroyContext(display, ctx);

XDestroyWindow(display, win);
XFreeColormap(display, cmap);
XCloseDisplay(display);
{% endhighlight %}
