#include <opencv2/opencv.hpp>
#include <iostream>

int main(int argc, char** argv)
{
	// Read the image file
	cv::Mat image = cv::imread("../../input/img/lena.jpg");

	// Check for failure
	if (image.empty()) 
	{
		std::cout << "Could not open or find the image. Press some key" << std::endl;
		std::cin.get(); //wait for any key press
		return -1;
	}

	std::cout << "Do not close the window through the window's X." << std::endl;
	std::cout << "Press some key to close it." << std::endl;

	cv::String windowName = "Lena"; //Name of the window
	cv::namedWindow(windowName); // Create a window
	cv::imshow(windowName, image); // Show our image inside the created window.
	cv::waitKey(0); // Wait for any keystroke in the window.
					// O valor do argumento é a quantidade de milisegundos para esperar por alguma resposta
	cv::destroyWindow(windowName); //destroy the created window

	return 0;
}