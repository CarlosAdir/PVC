#include "opencv2/highgui/highgui.hpp"
#include <iostream>

void CallBackFunc(int event, int x, int y, int flags, void* userdata)
{
     if ( flags == (cv::EVENT_FLAG_CTRLKEY + cv::EVENT_FLAG_LBUTTON) )
     {
          std::cout << "Left mouse button is clicked while pressing CTRL key - position (" << x << ", " << y << ")" << std::endl;
     }
     else if ( flags == (cv::EVENT_FLAG_RBUTTON + cv::EVENT_FLAG_SHIFTKEY) )
     {
          std::cout << "Right mouse button is clicked while pressing SHIFT key - position (" << x << ", " << y << ")" << std::endl;
     }
     else if ( event == cv::EVENT_MOUSEMOVE && flags == cv::EVENT_FLAG_ALTKEY)
     {
          std::cout << "Mouse is moved over the window while pressing ALT key - position (" << x << ", " << y << ")" << std::endl;
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