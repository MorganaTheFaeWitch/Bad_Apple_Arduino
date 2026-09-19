# Bad Apple on Arduino UNO R4 wifi. 
Hi, This is a funny little project to play bad apple on an arduino UNO R4 WIFI. 

How to run:
write sketch_apr23c.ino and badapple.h to an arduino UNO R4 wifi.
tada, it should start playing right away.

If you want to build the project yourself:
 - Download a copy of the bad apple video
 - rename the video "BadAppleOriginal.mp4" without the quotes, or change the input_video variable to target the name of the bad apple video.
 - Run VideoResizer.py with the bad apple video in the same folder.
 - this should output a video called BadAppleLR.mp4
 - Run BadAppleSerializer.py in the same file.
 - this should output badapple.h
 - include badapple.h with sketch_apt23c.ino and upload to an arduino uno r4 wifi.
