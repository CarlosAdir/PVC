/* from https://www.opencv-srf.com/2018/01/save-images-and-videos-to-file.html */
#include <opencv2/opencv.hpp>
#include <iostream>


int main(int argc, char** argv)
{
	// Read the image file
	cv::Mat image = cv::imread("../../input/img/lena.jpg");

	// Check for failure
	if (image.empty())
	{
		std::cout << "Could not open or find the image. Press a key" << std::endl;
		std::cin.get(); //wait for any key press
		return -1;
	}

	/*
	Make changes to the image as necessary
	e.g.  
	1. Change brightness/contrast of the image
	2. Smooth/Blur image
	3. Crop the image
	4. Rotate the image
	5. Draw shapes on the image
	*/

	bool isSuccess = imwrite("../../output/img/lena.jpg", image); //write the image to a file as JPEG 
	//bool isSuccess = imwrite("D:/MyImage.png", image); //write the image to a file as PNG
	if (isSuccess == false)
	{
		std::cout << "Failed to save the image. Press a key" << std::endl;
		std::cin.get(); //wait for a key press
		return -1;
	}

	std::cout << "Image is succusfully saved to a file" << std::endl;

	cv::String windowName = "The Saved Image"; //Name of the window
	cv::namedWindow(windowName); // Create a window
	cv::imshow(windowName, image); // Show our image inside the created window.

	cv::waitKey(0); // Wait for any keystroke in the window

	cv::destroyWindow(windowName); //destroy the created window

	return 0;
}