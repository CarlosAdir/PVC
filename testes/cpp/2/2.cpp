/* from https://www.opencv-srf.com/2018/02/change-contrast-of-images-and-videos.html */

#include <opencv2/opencv.hpp>
#include <iostream>


int main(int argc, char** argv)
{
	//open the video file for reading
	cv::VideoCapture cap("../../input/video/hour.avi");
	cv::Mat frame;

	// if not success, exit program
	if (cap.isOpened() == false)
	{
		std::cout << "Cannot open the video file" << std::endl;
		std::cin.get(); //wait for any key press
		return -1;
	}

	//Defining window names for above images
	cv::String windowNameOriginalImage = "Original Image";
	cv::String windowNameContrastHigh2 = "Contrast Increased by 2";
	cv::String windowNameContrastHigh4 = "Contrast Increased by 4";
	cv::String windowNameContrastLow0_5 = "Contrast Decreased by 0.5";
	cv::String windowNameContrastLow0_25 = "Contrast Decreased by 0.25";

	//Create and open windows for above images
	cv::namedWindow(windowNameOriginalImage, cv::WINDOW_NORMAL);
	cv::namedWindow(windowNameContrastHigh2, cv::WINDOW_NORMAL);
	cv::namedWindow(windowNameContrastHigh4, cv::WINDOW_NORMAL);
	cv::namedWindow(windowNameContrastLow0_5, cv::WINDOW_NORMAL);
	cv::namedWindow(windowNameContrastLow0_25, cv::WINDOW_NORMAL);

	while (true)
	{
		bool bSuccess = cap.read(frame); // read a new frame from video 

		//Breaking the while loop at the end of the video
		if (bSuccess == false)
		{
			std::cout << "Found the end of the video" << std::endl;
			break;
		}

		cv::Mat frameContrastHigh2;
		frame.convertTo(frameContrastHigh2, -1, 2, 0); //increase the contrast by 2

		cv::Mat frameContrastHigh4;
		frame.convertTo(frameContrastHigh4, -1, 4, 0); //increase the contrast by 4

		cv::Mat frameContrastLow0_5;
		frame.convertTo(frameContrastLow0_5, -1, 0.5, 0); //decrease the contrast by 0.5

		cv::Mat frameContrastLow0_25;
		frame.convertTo(frameContrastLow0_25, -1, 0.25, 0); //decrease the contrast by 0.25

		//Show above images inside the created windows.
		cv::imshow(windowNameOriginalImage, frame);
		cv::imshow(windowNameContrastHigh2, frameContrastHigh2);
		cv::imshow(windowNameContrastHigh4, frameContrastHigh4);
		cv::imshow(windowNameContrastLow0_5, frameContrastLow0_5);
		cv::imshow(windowNameContrastLow0_25, frameContrastLow0_25);

		//wait for for 10 ms until any key is pressed.  
		//If the 'Esc' key is pressed, break the while loop.
		//If the any other key is pressed, continue the loop 
		//If any key is not pressed withing 10 ms, continue the loop
		if (cv::waitKey(10) == 27)
		{
			std::cout << "Esc key is pressed by user. Stoppig the video" << std::endl;
			break;
		}
	}

	return 0;
}