title: The Matrix Has You - Notes
slug: the-matrix-has-you-notes
category: research notes
date: 2017-07-02
modified: 2017-07-02

## Citation

Michael Rietzler, Florian Geiselhart, and Enrico Rukzio. 2017. The matrix has you: realizing slow motion in full-body virtual reality. In Proceedings of the 23rd ACM Symposium on Virtual Reality Software and Technology (VRST '17). ACM, New York, NY, USA, Article 2, 10 pages. 

## Notes

This paper explores time manipulation using two different classes of cues:
environmental and manipulating user's body movement. 

The problems with traditional methods of time manipulation are a problem because the user has no natural understanding of it. We can't just delay the user's movements because that will be percieved as lag. Also, we can't just slowly decrease the velocity of the joints in the virtual body because then the two avatars will be out of sync. Lastly, we can't modify the user's body without using movment-limiting devices (such as haptics)

They describe three different methods using low-pass filters to support the notion of time manipulation

1. Simple - The virtual avatar moves as fast as possible up to a maximum to keep up with the real avatar.
2. Restricted - This uses the simple low-pass method however it also takes into consideration the real avatar's current velocity. This gives the real avatar more control, for example if the real avatar didnt move using the simple low-pass then the virtual avatar would still move, however it wouldnt with this approach.
3. Simple with Forecast - This method is the simple low-pass method however it is 
only applied to a semi-transparent version of the body. The virtual avatar is in sync with the real avatar aside from this semi-transparent version.

They tested these three different methods using a user study of 16 and tested with 
the following conditions

1. Control Realtime
2. Control Slow motion
3. Permanent Simple Low-Pass
4. Permanent Restricted Low-Pass
5. Permanent Simple Low-Pass with Forecast
6. Alternating Simple Low-Pass
7. Alternating Restricted Low-Pass
8. Alternating Simple Low-Pass with Forecast

This paper concludes that environment cues did not play a signficant role in percieved time.



