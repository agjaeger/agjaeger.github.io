title: ACM VRST 2018 Summary
slug: vrst-2018-summary
category: research notes
date: 2019-04-25
modified: 2017-02-07
summary: Summary of the ACM VRST 2018 conference
tags: vrst 2018 virtual reality

A set of research notes as I read through the ACM VRST 2018 Proceedings

## Session: UI & Display

<div>
  <h3>
      Sublime: a Hands-Free Virtual Reality Menu Navigation System
      Using a High-Frequency SSVEP-based Brain-Computer Interface
  </h3>
  <i>
      Alexandre Armengol-Urpi and Sanjay E. Sarma. 2018.Sublime: a
      Hands-Free Virtual Reality Menu Navigation System Using a
      High-Frequency SSVEP-based Brain-Computer Interface. In 24th ACM
      Symposium on Virtual RealitySoftware and Technology (VRST ’18),
      November 29-December 1, 2018, Tokyo,Japan.ACM, New York, NY, USA, 8 pages.
      https://doi.org/10.1145/3281505.3281514
  </i>
  <p>
      Virtual reality, brain-computer interface, steady-state visually
      evoked potentials, electroencephalography
  </p>
  <p>
      Introduces a new technique of a Brain-Computer Interface where the
      objects are flickering. The measurements from the EEG the flicker
      of the objects is used to uniquely
      identify each object. The previous approaches used fiducials.

      This study used 3 participants?? Ah ok, only to prove the concept
      of the system. The results showcased that the system could work
      although the participants noticed the flicker of the objects and
      reported it was mildly difficult to use.
  </p>
</div>

<hr style="border:none; border-bottom: dotted 5px;" />

<div>
  <h3>
      Design and Implementation of a Multi-person Fish-Tank Virtual
      Reality Display
  </h3>
  <i>
      Dylan Brodie Fafard, Qian Zhou, Chris Chamberlain, Georg Hagemann,
      Sidney Fels, and Ian Stavness. 2018. Design and Implementation of a
      Multi-person Fish-Tank Virtual Reality Display. In VRST 2018: 24th
      ACM Sym-posium on Virtual Reality Software and Technology (VRST ’18),
      November28-December 1, 2018, Tokyo, Japan.ACM, New York, NY, USA, 9 pages.
      https://doi.org/10.1145/3281505.3281540
  </i>
  <p>
      Fish tank virtual reality, collaboration, co-location, stereo,
      3D dis-plays, spherical displays
  </p>
  <p>
      Previous implementations of Fish-Tank Virtual Reality have been
      single user focused. This paper introduces a strategy using multiple
      projectors to create a multi-user system. In order to do the multi-user
      modes, they utilize the additional projectors in the system. They also
      implemented an auto calibration for image alignment and blending. The
      system also features a smartphone view that produces a perspective correct
      view for outside participants.
  </p>
</div>

<hr style="border:none; border-bottom: dotted 5px;" />


<div>
  <h3>
      Audio-Tactile Proximity Feedback for Enhancing 3D Manipulation
  </h3>
  <i>
      Alexander Marquardt, Ernst Kruijff, Christina Trepkowski, Jens Maiero,Andrea Schwandt, André Hinkenjann, Wolfgang Stuerzlinger, and JohannesSchöning. 2018. Audio-Tactile Proximity Feedback for Enhancing 3D Manip-ulation. InVRST 2018: 24th ACM Symposium on Virtual Reality Software andTechnology (VRST ’18), November 28-December 1, 2018, Tokyo, Japan.ACM,New York, NY, USA, 10 pages. https://doi.org/10.1145/3281505.3281525
  </i>
  <p>
      Tactile feedback; 3D user interface; hand guidance
  </p>
  <p>
      The researchers developed a tactile-glove and combined with a system to
      generate 3D audio, they wanted to test the effects of high-resolution,
      directional cues of manipulation tasks. Their results suggest that
      these cues increased the performance and the awareness of the user.
  </p>
</div>

<hr style="border:none; border-bottom: dotted 5px;" />

## Demos

<div>
  <h3>A Lightweight and Efficient System for Tracking Handheld Objects in Virtual Reality</h3>
  <i>
      Ya-Kuei Chang, Jui-Wei Huang, Chien-Hua Chen, Chien-Wen Chen,
      Jian-Wei Peng, Min-Chun Hu, Chih-Yuan Yao, and Hung-Kuo Chu.
      2018. A lightweight and efficient system for tracking handheld
      objects in virtual reality. In Proceedings of the 24th ACM Symposium
      on Virtual Reality Software and Technology (VRST '18), Stephen N.
      Spencer (Ed.). ACM, New York, NY, USA, Article 43, 2 pages.
      DOI: https://doi.org/10.1145/3281505.3281567
  </i>
  <p>
    Showcases the effect of lightweight tracking using just a Leap Motion and
    IMU sensor. This is especially useful imo for prototyping new tracked objects
    or objects that need to be tracked but cannot be retrofitted with a more
    powerful solution.

    The author states that the limitations of this approach are
    <ol>
      <li>Unable to track the object when the user is not holding it</li>
      <li>There is a small working area due to the range of the leap</li>
      <li>Unable to exchange hands after the object is being held</li>
  </p>
</div>

<hr style="border:none; border-bottom: dotted 5px;" />

<div>
  <h3>A Low-cost Motion Platform with Balance Board</h3>
  <i>
      Wataru Wakita, Tomoyuki Takano, and Toshiyuki Hadama. 2018.
      A Low-costMotion Platform with Balance Board. In VRST 2018: 24th
      ACM Symposium on Virtual Reality Software and Technology (VRST ’18),
      November 28-December1, 2018, Tokyo, Japan.ACM, New York, NY, USA, 2 pages.
      DOI: https://doi.org/10.1145/3281505.3281571
  </i>
  <p>
    Using two hydraulic arms and a metal hemisphere, they present the ability
    to build a low cost motion platform. This motion platform is capable
    of += 25deg on the row and pitch axes.
  </p>
</div>

<hr style="border:none; border-bottom: dotted 5px;" />

<div>
  <h3>A Low-cost Omni-directional VR Walking Platform by ThighSupporting and Motion Estimation</h3>
  <i>
      Wataru Wakita, Tomoyuki Takano, and Toshiyuki Hadama. 2018.
      A Low-cost Omni-directional VR Walking Platform by Thigh Supporting
      and MotionEstimation. In VRST 2018: 24th ACM Symposium on
      Virtual Reality Softwareand Technology (VRST ’18),
      November 28-December 1, 2018, Tokyo, Japan.ACM, New York, NY, USA, 2 pages.
      DOI: https://doi.org/10.1145/3281505.3281570
  </i>
  <p>
    Traditional infinite walking strategies utilize a foot-slipping technique, movable
    floor, redirected walking, or tilting the user. The researchers present
    another strategy where the system tracks the thigh of the user as they
    apply a force into the barrier of the device.

    The user wears two bands of load sensors, one on the upper thigh and
    the other on the lower thigh. This allows the system to detect when the
    user is walking and can estimate the final leg movement.
  </p>
</div>

<hr style="border:none; border-bottom: dotted 5px;" />

<div>
  <h3>
      AR DeepCalorieCam V2: Food Calorie Estimationwith CNN and AR-based
      Actual Size Estimation
  </h3>
  <i>
      Ryosuke Tanno, Takumi Ege, and Keiji Yanai. 2018. AR DeepCalorie
      Cam V2: Food Calorie Estimation with CNN and AR-based Actual Size
      Estimation. In VRST 2018: 24th ACM Symposium on Virtual Reality
      Software andTechnology (VRST ’18), November 28-December 1, 2018,
      Tokyo, Japan. ACM, New York, NY, USA,2 pages.
      DOI: https://doi.org/10.1145/3281505.3281580
  </i>
  <p>
      They use ARKit to measure the size of the intended food and a CNN
      to classify the found food into a category. Previous techniques
      required a reference object to be placed in the scene for size
      estimation. The user has to draw the area of the food, it is not
      automatically detected.
  </p>
</div>

<hr style="border:none; border-bottom: dotted 5px;" />

<div>
  <h3>
      Automatic 3D Modeling of Artwork andVisualizing Audio in an Augmented
      Reality Environment
  </h3>
  <i>
      Elijah Schwelling and Kyungjin Yoo. 2018. Automatic 3D Modeling of
      Artwork and Visualizing Audio in an Augmented Reality Environment.
      In Proceedings ofVRST ‘18. ACM, Tokyo, Japan, 2 pages.
      https://doi.org/10.1145/3281505.3281576
  </i>
  <p>
      Goal is to make art museums more interactive through the use of AR.
      The app recognizes a painting then creates a heightmap and renders
      a 3D model. The scale factor of the resulting 3D model is modified
      by music associated with the painting.
  </p>
</div>

<hr style="border:none; border-bottom: dotted 5px;" />