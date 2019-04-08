title: Learning Optix Raytracing Part 1: Compiling OptixHello
slug: learning-optix-rt-p1
category: micro adventures
date: 2019-04-08
modified: 2019-04-08
summary: The beginnings of learning Optix

I wanted to get the optixHello project compiling and running on my machine.
I havent sat down and learned CMake yet, so typically I create a new Visual Studio
project and begin this micro-adventure

Slowly but surely, I will create a pathtracer with Optix.

# Download The Dependencies

1. CUDA (I am using version 10)
2. Optix SDK (I am using version 6)
3. FreeGLUT
4. GLEW
5. sutil (located in the SDK examples, this will have to be compiled or included in the project)

# Setting up the Visual Studio Project

Create a new Visual Studio Project with the CUDA Runtime Template<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This will automatically compile CUDA C/C++ source files

Copy the source files from the optixHello demo in the SDK examples.<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Should be two files draw_color.cu and optixHello.cpp

We need to modify some Visual Studio project propeties to correctly compile .cu to ptx<br/>
  1. C/C++<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; * Additional Include Directories: Add the includes for the Optix SDK and the library dependencies<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; * Add NOMINMAX to the list of preprocessor definitions<br/>
  2. CUDA C/C++<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; * Compiler Output: Change the filename to something you will remember and the extension should be ptx<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; * Additional Include Directories: Add the includes for the Optix SDK<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; * Set Keep Prepprocessed Files to Yes (--keep)<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; * NVCC Compilation Type should be Generate.ptx file (--ptx)<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; * Turn Debug Information to No in Device and Host<br/>
  3. Linker<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; * Additional Dependencies should be added with the dependencies' library files plus glu32.lib and opengl32.lib

One Important Note:
  In order to use Optix, you have to read the .ptx file then pass the string into Optix to be used. If you rely on
  sutil.h, there is a default file name that it looks for. Change the compiler output filename (in CUDA C/C++ Properties) to reflect this

# Optional: Replace the sutil.h dependency

I really disliked the reliance on sutil, its just so thick... So I worked towards the removal.

In order to compile and run OptixHello without sutil, we need to replace the functions that the demo
relies on.
  * initGlut
  * displayBufferGlut
  * getPtxString

It was straightforward enough to create a seperate c++ namespace with just these functions

# Result So Far

<img
  src="{filename}/images/learning-optix-p1-1.png"
  width="100%"/>