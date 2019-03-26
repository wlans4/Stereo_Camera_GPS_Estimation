# Stereo_Vision

This project uses two cameras in order to produce a matrix for distance calculations.

0: test_cameras.py

Use this file to test where the checkerboard images are in each camera



1. image_capture.py

Capture images of chessboards in order to calibrate each camera individually. 
(Examples given here: https://docs.opencv.org/2.4.13.7/doc/tutorials/calib3d/camera_calibration/camera_calibration.html)



2. calibration.py

Each camera is indivually calibrated, and then the stereo calibration is created. This is the calibration that will be used to create the disparity calculation



3. calculate_depth.py

Calculate the disparity matrix created from images of the calibrated cameras. Distance to each pixel can be calculated using this matrix, as long as you have distance between cameras and focal length. The formula is given as 

D = Distance
o = Offset between cameras
f = focal length of the cameras (use the average if they are different between the cameras)
d = disparity value at your chosen pixel

D = (o*f)/d

