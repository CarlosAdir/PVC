#include <opencv2/opencv.hpp>
#include <iostream>


int main(int argc, char* argv[])
{
    //Open the video file for reading
    cv::VideoCapture cap("../../input/video/hour.avi");
    cv::Mat frame;

    // if not success, exit the program
    if (cap.isOpened() == false)
    {
        std::cout << "Cannot open the video file" << std::endl;
        std::cin.get(); //wait for any key press
        return -1;
    }

    //Define the names of windows
    cv::String windowNameOfOriginalImage = "Original Video";
    cv::String windowNameOfHistogramEqualized = "Histogram Equalized Video";

    // Create windows with the above names
    cv::namedWindow(windowNameOfOriginalImage, cv::WINDOW_NORMAL);
    cv::namedWindow(windowNameOfHistogramEqualized, cv::WINDOW_NORMAL);

    while (true)
    {
        bool bSuccess = cap.read(frame); // Read a new frame from the video file 

         //Breaking the while loop at the end of the video
        if (bSuccess == false)
        {
            std::cout << "Found the end of the video" << std::endl;
            break;
        }

        //Convert the frame from BGR to YCrCb color space
        cv::Mat hist_equalized_image;
        cv::cvtColor(frame, hist_equalized_image, cv::COLOR_BGR2YCrCb);

        //Split the image into 3 channels; Y, Cr and Cb channels respectively and store it in a std::vector
        std::vector<cv::Mat> vec_channels;
        cv::split(hist_equalized_image, vec_channels);

        //Equalize the histogram of the Y channel 
        cv::equalizeHist(vec_channels[0], vec_channels[0]);

        //Merge 3 channels in the std::vector to form the color image in YCrCB color space. 
        cv::merge(vec_channels, hist_equalized_image);

        //Convert the histogram equalized image from YCrCb to BGR color space again
        cv::cvtColor(hist_equalized_image, hist_equalized_image, cv::COLOR_YCrCb2BGR);

        //show frames in the created windows
        cv::imshow(windowNameOfOriginalImage, frame);
        cv::imshow(windowNameOfHistogramEqualized, hist_equalized_image);

        //Wait for 10 ms until any key is pressed.  
        //If the 'Esc' key is pressed, break the while loop.
        //If the any other key is pressed, continue the loop 
        //If any key is not pressed within 10 ms, continue the loop
        if (cv::waitKey(5) == 27)
        {
            std::cout << "Esc key is pressed by the user. Stopping the video" << std::endl;
            break;
        }
    }

    cv::destroyAllWindows(); //Destroy all opened windows

    return 0;

}