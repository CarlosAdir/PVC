#include "cv.h"
#include "highgui.h"

int main(int argc, char* argv[])
{
	cvNamedWindow( "Example3", CV_WINDOW_AUTOSIZE );
	CvCapture* capture = cvCreateFileCapture( "cargoPickupGantryTest1.avi" );
	IplImage* frame;
	while(1) {
		frame = cvQueryFrame( capture );
		if( !frame ) break;
		cvShowImage( "Example3", frame );
		char c = cvWaitKey(33);
		if( c == 27 ) break;
	}
	cvReleaseCapture( &capture );
	cvDestroyWindow( "Example2" );
	return 0;
}
