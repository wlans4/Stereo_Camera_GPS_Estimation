# Stereo_Vision

This project uses two cameras on a sailboat in order to estimate the GPS location of a buoy. It requires a current and updating GPS location as the boat moves, as well as an assumption that the cameras will not move with respect to the boat once secured in place and calibrated.


1. Image_Capture.py

Capture images of chessboards in order to calibrate each camera individually. 
(Examples given here: https://docs.opencv.org/2.4.13.7/doc/tutorials/calib3d/camera_calibration/camera_calibration.html)

This file will create the required directories and clear them out before each use if necessary.


2. Calibration.py

Each camera is indivually calibrated, and then the stereo calibration is created. This is the calibration that will be used to create the disparity map.



3. Depth_Map_Calculator

This file holds a Depth_Map_Calculator object which houses the requirements to quickly create a depth map at a moments notice. It will store calibration information and other necessary information for the different uses of the depth map.

4. Distance_Calculator

This file has a Distance_Calculator object which houses a Depth_Map_Calculator. This file is used to take advantage of the depth map and estimate the gps location of a buoy based on color and contour.

5. Uncalibrated_Calculate_Depth_Map

Do not use this file, it is for testing purposes to make sure that the cameras are reading correctly and that you are not using the headless version of openCV
