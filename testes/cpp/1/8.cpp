/* from https://www.opencv-srf.com/2018/02/change-brightness-of-images-and-videos.html */

#include <opencv2/opencv.hpp>
#include <iostream>


int main(int argc, char** argv)
{
	// Read the image file
	cv::Mat image = imread("../../input/img/lena.jpg");

	// Check for failure
	if (image.empty())
	{
		std::cout << "Could not open or find the image" << std::endl;
		std::cin.get(); //wait for any key press
		return -1;
	}

	cv::Mat imageBrighnessHigh50;
	image.convertTo(imageBrighnessHigh50, -1, 1, 50); //increase the brightness by 50

	cv::Mat imageBrighnessHigh100;
	image.convertTo(imageBrighnessHigh100, -1, 1, 100); //increase the brightness by 100

	cv::Mat imageBrighnessLow50;
	image.convertTo(imageBrighnessLow50, -1, 1, -50); //decrease the brightness by 50

	cv::Mat imageBrighnessLow100;
	image.convertTo(imageBrighnessLow100, -1, 1, -100); //decrease the brightness by 100

	//Defining window names for above images
	cv::String windowNameOriginalImage = "Original Image";
	cv::String windowNameBrightnessHigh50 = "Brightness Increased by 50";
	cv::String windowNameWithBrightnessHigh100 = "Brightness Increased by 100";
	cv::String windowNameBrightnessLow50 = "Brightness Decreased by 50";
	cv::String windowNameBrightnessLow100 = "Brightness Decreased by 100";

	//Create and open windows for above images
	cv::namedWindow(windowNameOriginalImage, WINDOW_NORMAL);
	cv::namedWindow(windowNameBrightnessHigh50, WINDOW_NORMAL);
	cv::namedWindow(windowNameWithBrightnessHigh100, WINDOW_NORMAL);
	cv::namedWindow(windowNameBrightnessLow50, WINDOW_NORMAL);
	cv::namedWindow(windowNameBrightnessLow100, WINDOW_NORMAL);

	//Show above images inside the created windows.
	cv::imshow(windowNameOriginalImage, image);
	cv::imshow(windowNameBrightnessHigh50, imageBrighnessHigh50);
	cv::imshow(windowNameWithBrightnessHigh100, imageBrighnessHigh100);
	cv::imshow(windowNameBrightnessLow50, imageBrighnessLow50);
	cv::imshow(windowNameBrightnessLow100, imageBrighnessLow100);

	cv::waitKey(0); // Wait for any key stroke

	cv::destroyAllWindows(); //destroy all open windows

	return 0;
}