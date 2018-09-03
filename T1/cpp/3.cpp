#include "elementos.hpp"

using namespace cv;

void CallBackFunc(int event, int x, int y, int flags, void *F)
{

	imagem *Figura = (imagem *)F;
	Pixel vermelho(255, 0, 0);
	Pixel referencia;
	int distancia = 13;
	if  ( event == cv::EVENT_LBUTTONDOWN )
	{
		referencia = Figura->getPixel(x, y);
		Figura->setReferencia(referencia);
		std::cout << "Ponto: (" << x << ", " << y << ") - ";
		if(Figura->isGray())
		{
			std::cout << "Intensidade = " << int(referencia.r) << std::endl;
		}
		else
		{
			std::cout << "rgb = " << referencia << std::endl;
		}
		Figura->PintaDistancia(distancia, vermelho);
	}
	else if  ( event == cv::EVENT_RBUTTONDOWN )
	{
		std::cout << "Right button of the mouse is clicked - position (" << x << ", " << y << ")" << std::endl;
	}
	else if  ( event == cv::EVENT_MBUTTONDOWN )
	{
		std::cout << "Middle button of the mouse is clicked - position (" << x << ", " << y << ")" << std::endl;
	}
	else if ( event == cv::EVENT_MOUSEMOVE )
	{
		//std::cout << "Mouse move over the window - position (" << x << ", " << y << ")" << std::endl;

	}
}

int main(int argc, char** argv)
{
	// Read image from file
	//std::string filename = "../img/colored/messi.jpg" ;
	imagem Figura;
	cv::Mat tmp;
	int key;
	bool grayscale = true;
	cv::VideoCapture cap("../video/hour.avi"); 

	// if not success, exit program
	if (cap.isOpened() == false)  
	{
		std::cout << "Cannot open the video file. \nPress a Key" << std::endl;
		std::cin.get(); //wait for any key press
		return -1;
	}

	double fps = cap.get(cv::CAP_PROP_FPS); 
	std::cout << "Frames per seconds : " << fps << std::endl;

	cv::String window_name = "My First Video";

	cv::namedWindow(window_name, cv::WINDOW_NORMAL); //create a window
	
	//set the callback function for any mouse event
	cv::setMouseCallback(window_name, CallBackFunc, &Figura);
	while(true)
	{
		bool bSuccess = cap.read(tmp);
		if (bSuccess == false) 
		{
			std::cout << "Found the end of the video" << std::endl;
			break;
		}
		if(grayscale)
		{
			//cvtColor(tmp, Figura.getImg(), CV_RGB2GRAY)
			Figura.setImg(tmp);
		}
		else
			Figura.setImg(tmp);
		cv::imshow(window_name, Figura.getImg());
		key = cv::waitKey(10);
		if(key == 27)
			break;
		else if(key == 'g')
		{
			grayscale = not grayscale;
			std::cout << "Changing the grayscale" << std::endl;
			// Figura.setImg(filename);
			// if(grayscale)
			// 	cvtColor(src, bwsrc, cv::COLOR_RGB2GRAY)
		}
	}
	std::cout << "Esc key was pressed by user." << std::endl;

	return 0;

}