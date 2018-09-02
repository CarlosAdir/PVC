#include <opencv2/opencv.hpp>
//#include <iostream>

int main(int argc, char** argv)
{
 //create a new image which consists of 
 //3 channels 
 //image depth of 8 bits 
 //800 x 600 of resolution (800 wide and 600 high)
 //each pixels initialized to the value of (100, 250, 30) for Blue, Green and Red planes respectively.
 cv::Mat image(600, 800, CV_8UC3, cv::Scalar(100, 250, 30)); 
 
 cv::String windowName = "Window with Blank Image"; //Name of the window

 cv::namedWindow(windowName); // Create a window

 cv::imshow(windowName, image); // Show our image inside the created window.

 cv::waitKey(0); // Wait for any keystroke in the window

 cv::destroyWindow(windowName); //destroy the created window

 return 0;
}