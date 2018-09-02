#include "cv.h"
#include "highgui.h"

using namespace cv;

int main(int argc, char* argv[])
{
  Mat img, gray;
  int key = 0;
  img = imread("lena.jpg",1);
  imshow("Original", img);
  cvtColor(img,gray, COLOR_BGR2GRAY);
  GaussianBlur(gray, gray, Size(7,7), 1.5);
  Canny(gray, gray, 0, 50);
  imshow("Bordas", gray);

  while(key != 'q') {
    key = cvWaitKey(1);
  }

  return 0;
}
