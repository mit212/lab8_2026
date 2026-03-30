# Lab 8: Computer Vision

2.12/2.120 Intro to Robotics  
Spring 2025[^1]

<details>
  <summary>Table of Contents</summary>

- [0 (Prelab) Software Set Up](#0-prelab-software-set-up)
  - [0.1 Python](#01-python)
  - [0.2 OpenCV](#02-opencv)
  - [0.3 Matplotlib](#03-matplotlib)
  - [0.4 AprilTag Library](#04-apriltag-library)
- [1 Hardware Set Up](#1-hardware-set-up)
- [2 Gamma Adjustment](#2-gamma-adjustment)
- [3 Otsu’s method of Thresholding](#3-otsus-method-of-thresholding)
- [4 Canny Edge Detection](#4-canny-edge-detection)
- [5 Hough Transforms](#5-hough-transforms)
  - [5.1 Lines](#51-lines)
  - [5.2 Circles](#52-circles)
  - [5.3 Sudoku Grid](#53-sudoku-grid)
- [6 HSV vs RGB](#6-hsv-vs-rgb)
- [7 Morphological Operations](#7-morphological-operations)
- [8 Optical Flow](#8-optical-flow)
- [X AprilTags (Optional)](#X-apriltags-optional)

</details>

In this lab, you will be trying out different functions from OpenCV to visualize the computer vision techniques introduced in lecture. The entire lab is designed to take **around an hour**. Before the lab begins, we will do a quick demo of AprilTag detection and pose estimation along with the associated camera calibration procedure. We will also show you the output of the D435 depth camera in the Intel RealSense Viewer. The rest of lab time is allotted to working on the final project. Remember, building hardware always takes around 2-3 times longer than you think, so use your time wisely.

## 0 (Prelab) Software Set Up

### 0.1 Python

You should already have Python (version 3.9+) installed from [Lab 4](https://github.com/mit212/lab4_2025?tab=readme-ov-file#01-python). You can check which version of Python you have by entering `python3 -V` or `python -V` in your terminal.

### 0.2 OpenCV

OpenCV is an open source computer vision library. To install OpenCV, enter `pip install opencv-python` in your terminal. 

### 0.3 Matplotlib

Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python. To install Matplotlib, enter `pip install matplotlib` in your terminal.

### 0.4 AprilTag Library

Python bindings for the Apriltags3 library developed by AprilRobotics. To install, enter `pip install pupil-apriltags` in your terminal. If the installation fails, try using `pyapriltags` instead: `pip install pyapriltags`.

### 0.5 Test Imports of Libraries

Enter `python` or `python3` in the terminal depending on which Python you are using. A Python shell should begin in your terminal. Enter `import cv2`, `import matplotlib`, and `import pupil_apriltags` or `import pyapriltags` (depending on the library you installed for step 0.4) in the Python shell and make sure no errors occur. Enter `exit()` or press `Ctrl-D` to exit the Python shell.

<details> <summary><i> Module not found error? </i></summary>

Make sure that you installed the library to the Python version you are using. If you are running code with Python, then use `pip` to install the libraries. If you are running code with Python3 you may have to use `pip3` to install the libraries or `python3 -m pip install -U [library to install]`.
    
</details>

### 0.6 [Optional] Intel RealSense Viewer 

If you are on the UR5 team, it may be useful to download the Intel RealSense Viewer to set camera properties, view camera ouput, and view camera coordinate system. You can download it from [here](https://www.intelrealsense.com/sdk-2/). Scroll down to the Intel RealSense Viewer section and click Download.

## 1 Hardware Set Up 

Please review the [Canvas announcement regarding the Hardware/Software design review](https://canvas.mit.edu/courses/30408/discussion_topics/357910).

You will be using the built-in camera on your laptop. If your laptop does not have one, please ask the staff for an external camera.

Additionally, you should choose an object, preferably one of a solid color, to use for the entire lab. Throughout the lab, we will attempt to separate that object in the images taken by your camera from everything else.

## 2 Gamma Adjustment

Clone this repository or download/extract the ZIP file to your computer. You can use any code editor that supports Python. We recommend using IDLE, Python's built-in editor that should have been installed alongside Python, to edit and run each file. Using Visual Studio Code to edit and run the code is fine as well.

In computer vision, one of the first things introduced is gamma adjustment or correction. To experiment with this concept, open and run `gammaAdj.py`.

When you run this file, three windows will appear. One will show your unprocessed raw camera footage, another will show a processed (gamma adjusted image), and the last will have a slider. Play around with the slider and see what you observe (make it completely black or white).

To stop running the script, click on the `IDLE Shell 3.x.x` window and press `Ctrl+C`, then close the shell window.

## 3 Otsu’s Method for Automatic Image Thresholding

It is important to note that one of the prime goals of computer vision is to separate an image into *what you care about* and *what you don’t care about*. Otsu’s method of thresholding is a good example of a simple method that algorithmically separates pixels into two separate classes. To use it, open and run `otsu.py`.

When you run this command, a single image will be taken and then processed using Otsu’s method of thresholding. A histogram will appear on your screen, as well as the unprocessed and processed image.

You should remember from lecture how Otsu's method works. Hint: the teal line on the histogram seperates the pixels into two classes. All pixels from one class are set to black, and all pixels from the other class are set to white. The threshold seperating the pixels is set to minimize the intra-class variance, defined as a weighted sum of variances of the two classes.

## 4 Canny Edge Detection

Though Otsu’s method is nice due to the algorithm being relatively straightforward and fast, it is apparent that more complex techniques may be needed, especially to reduce background noise and handle cases where the object is a similar color to the background. This will help us further tackle the problem of separating *what you care about* from *what you don’t care about*.

To that end, Canny edge detection is an attempt at answering this problem when all you care about are **edges**. Hypothetically, since your object has edges, you would be able to separate it from its background if no background edges intersect with the object, or the background is "edgeless" (e.g. a solid colored wall). To experiment with the concept further, open and run `canny.py`. You may need to play with the sliders a bit before the edges start showing up. The sliders affect the minimum and maximum intensity gradient necessary for an edge to be counted, as described [here](https://docs.opencv.org/4.x/da/d22/tutorial_py_canny.html#:~:text=Hysteresis%20Thresholding).

You’ll notice that if you increase the lower threshold above the upper threshold, the algorithm should automatically switch so that the lower threshold becomes the upper threshold for the algorithm.

## 5 Hough Transforms

Similarly to how Canny edge detection would work great if your object is the only object with edges, Hough transforms are great if your object is either circular or a line.

### 5.1 Lines

Open and run `houghLines.py`. Note that a Canny edge detector is used to pre-process the image, to make it easier for the Hough transform to "agree" on lines. Play around with the sliders to see how changing the thresholds affects which lines are detected in the image. Unlike the circles algorithm, the lines algorithm is much less time intensive when it comes to false negatives (e.g. a line exists but is not detected), so there is no image shrinking done for this one.

You can find more information on the commands used [here](https://docs.opencv.org/2.4/doc/tutorials/imgproc/imgtrans/hough_lines/hough_lines.html).

### 5.2 Circles

Open and run `houghCircles.py`. Due to how many false circles are detected by the algorithm, the frame is shrunk with respect to the original captured image. This is accounted for in the accumulator ratio slider bar, which controls the ratio of image resolution to accumulator resolution. For example, if `Accumulator Ratio = 1`, the accumulator will have the same resolution as the input image. If `Accumulator Ratio = 2`, the accumulator will have half as big width and height. You can also change the degree the image is shrunk in line 44 of the code.

You can find more information on the commands used [here](https://docs.opencv.org/2.4/doc/tutorials/imgproc/imgtrans/hough_circle/hough_circle.html).

### 5.3 Sudoku Grid

Before running this on camera footage, you will be processing `sudoku.png`. Namely, edit the `TODO's` in `process.py`. The goal for this script is to isolate the grid lines (and **only** the grid lines) of the sudoku grid. If you see `TypeError: 'NoneType' object is not iterable`, no lines were detected in the Hough lines transform using your parameters.

Don't just blindly change the thresholds until something happens. Look at the code and understand how it works first. What intermediate image processing step do you need to get working properly before the Hough lines transform has a chance of detecting any lines in the image? (Hint: it rhynmes with "nanny")

| :white_check_mark: CHECKOFF 1 :white_check_mark:   |
|:---------------------------------------------------|
| Show the detected grid output to a TA or LA. |

## 6 HSV vs RGB

If you were paying very close attention, you may have noticed that ALL the algorithms before this section were conducted after converting your raw image into grayscale. With that in mind, we will now experiment with colors. For this section, in addition to the object you’ve been using, we ask that you find a few different colored objects to experiment with the robustness of the two methods for separation presented here. To begin the script, open and run `colorThresh.py`.

After capturing the objects of your choosing, you’ll want to note down the HSV values for the next part of the lab.

## 7 Morphological Operations

After using color thresholding, you may have noticed that there are some features that remain in the image besides the object that you want to detect. Morphological operations are an excellent way of getting rid of extra features you don’t want and enlarging objects you do want. To experiment and find which operations work best, open and run `morphOps.py`. Use the HSV values from the [previous section](#6-hsv-vs-rgb).

Something else interesting about morphological operations is the kernel operator that is used. The kernel determines the shape of a pixel neighborhood over which the morphological operation (erosion, dilation, etc.) is taken. If you open the script, you’ll find a section of code that allows you to make your own kernel. A vertical line is given as an example in the comments. Rerun the script with a kernel of your own design.

| :white_check_mark: CHECKOFF 2 :white_check_mark:   |
|:---------------------------------------------------|
| Show your custom kernel in action to a TA or LA. |

## 8 Optical Flow

Optical flow has several uses. The one we’ll present here is tracking an "object" as it moves through space. Hypothetically, if you used a series of morphological operations to isolate your object (as in section 7), and then placed trackers on the features present, you’d be able to use optical flow to track your object in space. In this case, we will be placing trackers on detected corners. To run the optical flow script, open and run `opticalFlow.py`. Note that the list of corners to track is initialized using the very first camera frame, so you should hold up your object to the camera before running the script. 

To tune the features tracked by the script, you can edit the variable `feature_params` by decreasing `qualityLevel` and increasing `maxCorners`. Tune these parameters so that when running this script, a corner is detected on your object.

| :white_check_mark: CHECKOFF 3 :white_check_mark:   |
|:---------------------------------------------------|
| Show the optical flow script in action to a TA or LA.|

## X AprilTags (Optional)

[AprilTags](https://ftc-docs.firstinspires.org/en/latest/apriltag/vision_portal/apriltag_intro/apriltag-intro.html) are a system of visual tags developed by researchers at the University of Michigan to provide low overhead, high accuracy localization for many different applications. In the term project field, we use them as landmarks, allowing you to determine the 6D pose of the camera (mounted to your mobile robot) relative to the AprilTag. All of the tags we use are part of the [36h11 family](https://triagechallenge.darpa.mil/docs/AprilTag_0-20_family36h11.pdf), which can be recognized by AprilTag's own detector as well as an alternative, fast detector included with OpenCV ([ArUco, see here](https://docs.opencv.org/4.x/d5/dae/tutorial_aruco_detection.html)).

Before we begin, we have to calculate the [camera matrix](https://docs.opencv.org/4.x/dc/dbb/tutorial_py_calibration.html). This matrix describes the mapping of a pinhole camera from 3D points in the world to 2D points in an image. We are particularly interested in four parameters of this matrix: focal lengths `f` and optical center `p`. This information can be used to remove distortion due to the lenses of a specific camera.  
  
<p align="center">
  <img src=.images/camera_matrix_details.png width="600">
</p>

The camera matrix is unique to each camera, so once calculated, it can be reused on other images taken by the same camera. We will use a standard test image known as a checkerboard to calibrate the camera.

1. Run `apriltag_camera_calibration.py`. If you're having issues with the camera, try commenting out lines 35-38 in the code. The frame rate may be very low, since the algorithm OpenCV uses to detect the checkerboard is fairly resource intensive.
2. Hold up the large checkerboard to the camera. If it is detected, you should see a series of colored lines, as shown below.

<p align="center">
  <img src=.images/calibration_checkerboard.svg  width="400">
</p>

3. Press `s` to save the current frame. Make sure you see "Chessboard corners found! Saving this frame." printed in the terminal.
4. Move the checkerboard to various positions: near the camera, far away, in each corner of the video feed, tilted and rotated relative to the camera, etc. Save at least 10 frames.
5. Press `c` to generate and save the calibration data. The camera matrix, along with some other data, will be saved as `camera_calibration_live.npz`.
6. Press `q` to exit the program.
7. Now, run `apriltag_pose.py`. (If you installed `pyapriltags` instead of `pupil-apriltags`, change line 3 of the code to read `import pyapriltags as apriltag`). Try holding up an AprilTag to the camera. You should see its 3D coordinates overlaid on the tag. If you have time, try measuring the actual distance between the AprilTag and the camera. Does it align with the distance calculated by the AprilTag detector? You may have to change the AprilTag size in line 35 of the code (the AprilTags on the white stands used in the final competition are 9.6 cm wide).
8. Press `q` to exit the program.

[^1]: Version 1 - 2016: Peter Yu, Ryan Fish and Kamal Youcef-Toumi  
  Version 2 - 2017: Luke Roberto, Yingnan Cui, Steven Yeung and Kamal Youcef-Toumi  
  Version 3 - 2019: Jerry Ng, Jacob Guggenheim  
  Version 4 - 2020: Jerry Ng, Rachel Hoffman, Steven Yeung, and Kamal Youcef-Toumi  
  Version 5 - 2020: Phillip Daniel  
  Version 6 - 2024: Jinger Chong  
  Version 7 - 2025: Roberto Bolli Jr., Kaleb Blake
