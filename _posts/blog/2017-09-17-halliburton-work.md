---
layout: post
title: Summer 2017 Halliburton Intern
date: 2017-09-17 20:45:00
categories: blog

draft: true
---

Hey guys! Its been a while since my last update, sorry about that. I hope 
to be uploading more posts this semester.

I just completed a really fun internship for Halliburton (Major Oil 
Servicing Company) in Houston. I worked in their Virtual / Augmented Reality 
lab underneath David d'Angelo and Phil Norland. I was tasked with designing 
an AR visualization of their sub-surface data. 

Their managment / visualization product is called DecisionSpace and it 
already had a 3D 'cube view', so I used Unity and the Microsoft Hololens 
to create an immersive world. This world allowed the user to manipulate 
the data via voice commands and standard hand input. The basics of the 
project were already done (the cube view was in the world), however it 
was rushed so one of my first tasks was to redo the existing system. An 
overview of my tasks were:

- redesign the base system
- implement a cleaner input system
- use photon networking to share the world with others
- use c# sockets to send data to DecisionSpace (to modify the data)
- write the code / project in such a way that all devices are compiled from one project

My colleague, Juan Munoz-Arango, was working on the VR portion by designing 
the world to work with the HTC Vive. We met several interesting challenges 
along the way since we were working under the same Unity project. This meant 
the project (and all dependencies) had to be compiled against both systems. 
One of the most infuriating portions of this blocker was SteamVR, we had 
to personally go through the source files and add #if !UNITY_METRO to all 
files that can't compile to the Hololens (mind you that this is before 
the recent update that fixed this). We also had to use that preprocessor
for the networking code because hololens doesnt really support sockets but 
websockets.

Overall it was a really enlightening experience and I am happy that I was 
able to help them out.


PS If I remember I will upload some photos.
