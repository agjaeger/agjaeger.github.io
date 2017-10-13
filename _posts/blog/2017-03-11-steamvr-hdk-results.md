---
layout: post
title: SteamVR HDK Results
date: 2017-03-11 13:51:00
categories: blog
short_description: Our first iteration of success for custom SteamVR / Vive Hardware

draft: false
---

{% include iframe  iframePath='/slides/2017/03/11/steamvr-hdk-results-slides.html' %}

The last two weeks have been at a nonstop pace. From after hours 3D printing 
to iterative CAD Design, we have been trying to create our own trackable glasses. 
In January, my colleague Juan attended the SteamVR HDK training seminar and 
now in March we have gotten around to producing our own hardware. 

Professional tracking solutions can cost $5000 and easily get much higher. 
We wanted to experiment with creating a custom tracking system with the SteamVR Lighthouses 
that could be interfaceable with Unity. This system would cost approximately 
$800 and requires the usage of a 3D printer, making it much more affordable.

### The Development Process

We first started doing the 3D modeling work in 123D (since it was simple to print on a Makerbot).
Quickly, we switched to Autodesk Inventor 2015 because of greater support for 
dimensions and rigid constraints. I felt like I was in heaven when modeling in 
Inventor. After each modeling iteration, we checked the model in the simulator and fine tuned.

With satisfactory results from the simulation, we started building the json file. At first, 
we hand calculated the normals for the faces of sensors, but I soon wrote a python script that 
converted a custom json (one that specified corner positions) into an offical json file for steam.
This script made life so much easier, no more vector math.

3D printing the constellation took approximately 8 hours, with rafts and supports. 
On several occasions, we had to restart due to the 3D printer messing up. Thankfully, our 
Makerbot printed at a accuracy high enough to get ideal results. 

After the sensors and imu were placed on the constellation, calibration had to be done.
The calibration process was straighforward, hold the trackable in 6 different directions and 
then wave. 

And finally, we got it tracking in Unity through the SteamVR package.

### Results

Our first testable iteration passed and we were able to get it tracking in Unity. 
The simulation results show a mostly blue region on the front of the constellation 
with it moving to yelllow then red towards the edges. The tracking results 
in Unity were great, no major problems unless you turned away from a sensor.
The current constellation design was successful, however we need to make it sturdier. 
As it stands anyone could easily break the device and that needs to be fixed.

### Potential Improvements

- More blue coverage around the sphere
- Find a quicker way to produce constellations
- Iterate the constellation design to make it more robust



