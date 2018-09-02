/* from https://www.opencv-srf.com/2018/02/histogram-equalization.html */

#include <opencv2/opencv.hpp>
#include <iostream>


int main(int argc, char** argv)
{
    // Read the image file
    cv::Mat image = cv::imread("../../input/img/messi.jpg");

    // Check for failure
    if (image.empty())
    {
        std::cout << "Could not open or find the image" << std::endl;
        std::cin.get(); //wait for any key press
        return -1;
    }

    //change the color image to grayscale image
    cv::cvtColor(image, image, cv::COLOR_BGR2GRAY); 

    //equalize the histogram
    cv::Mat hist_equalized_image;
    cv::equalizeHist(image, hist_equalized_image); 
                                               
    //Define names of windows
    cv::String windowNameOfOriginalImage = "Original Image"; 
    cv::String windowNameOfHistogramEqualized = "Histogram Equalized Image";

    // Create windows with the above names
    cv::namedWindow(windowNameOfOriginalImage, cv::WINDOW_NORMAL);
    cv::namedWindow(windowNameOfHistogramEqualized, cv::WINDOW_NORMAL);

    // Show images inside created windows.
    cv::imshow(windowNameOfOriginalImage, image);
    cv::imshow(windowNameOfHistogramEqualized, hist_equalized_image);

    cv::waitKey(0); // Wait for any keystroke in one of the windows

    cv::destroyAllWindows(); //Destroy all open windows

    return 0;
}