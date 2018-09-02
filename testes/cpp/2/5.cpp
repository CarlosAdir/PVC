/* from https://www.opencv-srf.com/2011/11/mouse-events.html */

#include "opencv2/highgui/highgui.hpp"
#include <iostream>


void CallBackFunc(int event, int x, int y, int flags, void* userdata)
{
     if  ( event == cv::EVENT_LBUTTONDOWN )
     {
          std::cout << "Left button of the mouse is clicked - position (" << x << ", " << y << ")" << std::endl;
     }
     else if  ( event == cv::EVENT_RBUTTONDOWN )
     {
          std::cout << "Right button of the mouse is clicked - position (" << x << ", " << y << ")" << std::endl;
     }
     else if  ( event == cv::EVENT_MBUTTONDOWN )
     {
          std::cout << "Middle button of the mouse is clicked - position (" << x << ", " << y << ")" << std::endl;
     }
     else if ( event == cv::EVENT_MOUSEMOVE )
     {
          std::cout << "Mouse move over the window - position (" << x << ", " << y << ")" << std::endl;

     }
}

int main(int argc, char** argv)
{
     // Read image from file 
     cv::Mat img = cv::imread("../../input/img/messi.jpg");

     //if fail to read the image
     if ( img.empty() ) 
     { 
          std::cout << "Error loading the image" << std::endl;
          return -1; 
     }

     //Create a window
     cv::namedWindow("My Window", 1);

     //set the callback function for any mouse event
     cv::setMouseCallback("My Window", CallBackFunc, NULL);

     //show the image
     cv::imshow("My Window", img);

     // Wait until user press some key
     cv::waitKey(0);

     return 0;

}