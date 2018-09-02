/* from https://www.opencv-srf.com/2018/02/change-brightness-of-images-and-videos.html */

#include <opencv2/opencv.hpp>
#include <iostream>

int main(int argc, char** argv)
{
	//open the video file for reading
	cv::VideoCapture cap("../../input/video/cargo.avi");
	cv::Mat frame;

	// if not success, exit program
	if (cap.isOpened() == false)
	{
		std::cout << "Cannot open the video file" << std::endl;
		std::cin.get(); //wait for any key press
		return -1;
	}

	//Defining window names
	cv::String windowNameOriginalVideo = "Original Video";
	cv::String windowNameBrightnessHigh50 = "Brightness Increased by 50";
	cv::String windowNameWithBrightnessHigh100 = "Brightness Increased by 100";
	cv::String windowNameBrightnessLow50 = "Brightness Decreased by 50";
	cv::String windowNameBrightnessLow100 = "Brightness Decreased by 100";

	//Create and open windows for above window names
	cv::namedWindow(windowNameOriginalVideo, cv::WINDOW_NORMAL);
	cv::namedWindow(windowNameBrightnessHigh50, cv::WINDOW_NORMAL);
	cv::namedWindow(windowNameWithBrightnessHigh100, cv::WINDOW_NORMAL);
	cv::namedWindow(windowNameBrightnessLow50, cv::WINDOW_NORMAL);
	cv::namedWindow(windowNameBrightnessLow100, cv::WINDOW_NORMAL);

	while (true)
	{
		bool bSuccess = cap.read(frame); // read a new frame from video 

		//Breaking the while loop at the end of the video
		if (bSuccess == false)
		{
			std::cout << "Found the end of the video" << std::endl;
			break;
		}

		cv::Mat frameBrighnessHigh50;
		frame.convertTo(frameBrighnessHigh50, -1, 1, 50); //increase the brightness by 50

		cv::Mat frameBrighnessHigh100;
		frame.convertTo(frameBrighnessHigh100, -1, 1, 100); //increase the brightness by 100

		cv::Mat frameBrighnessLow50;
		frame.convertTo(frameBrighnessLow50, -1, 1, -50); //decrease the brightness by 50

		cv::Mat frameBrighnessLow100;
		frame.convertTo(frameBrighnessLow100, -1, 1, -100); //decrease the brightness by 100

		//Show above frames inside the created windows.
		cv::imshow(windowNameOriginalVideo, frame);
		cv::imshow(windowNameBrightnessHigh50, frameBrighnessHigh50);
		cv::imshow(windowNameWithBrightnessHigh100, frameBrighnessHigh100);
		cv::imshow(windowNameBrightnessLow50, frameBrighnessLow50);
		cv::imshow(windowNameBrightnessLow100, frameBrighnessLow100);

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