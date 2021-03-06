/* From https://www.opencv-srf.com/2017/12/play-video-from-file-or-camera.html */

#include <opencv2/opencv.hpp>
#include <iostream>

int main(int argc, char* argv[])
{
	//open the video file for reading
	cv::VideoCapture cap("../../input/video/hour.avi"); 
	cv::Mat frame;

	// if not success, exit program
	if (cap.isOpened() == false)  
	{
		std::cout << "Cannot open the video file. \nPress a Key" << std::endl;
		std::cin.get(); //wait for any key press
		return -1;
	}

	//Uncomment the following line if you want to start the video in the middle
	//cap.set(CAP_PROP_POS_MSEC, 300); 

	//get the frames rate of the video
	double fps = cap.get(cv::CAP_PROP_FPS); 
	std::cout << "Frames per seconds : " << fps << std::endl;

	cv::String window_name = "My First Video";

	cv::namedWindow(window_name, cv::WINDOW_NORMAL); //create a window

	while (true)
	{
		bool bSuccess = cap.read(frame); // read a new frame from video 

		//Breaking the while loop at the end of the video
		if (bSuccess == false) 
		{
			std::cout << "Found the end of the video" << std::endl;
			break;
		}

		//show the frame in the created window
		cv::imshow(window_name, frame);

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