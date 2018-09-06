#include "elementos.hpp"

using namespace cv;

void exibe_resultado(Imagem *Figura, Ponto *p)
{
	Pixel referencia = Figura->getPixel(*p);
	std::cout << "Ponto: " << *p << " - ";
	if(Figura->isGray())
	{
		std::cout << "Intensidade = " << int(referencia.r) << std::endl;
	}
	else
	{
		std::cout << "rgb = " << referencia << std::endl;
	}
	referencia = Figura->getPixel(*p);
	Figura->setReferencia(referencia);
}


void CallBackFunc(int event, int x, int y, int flags, void *point)
{

	Ponto *p = (Ponto *)point;
	if  ( event == cv::EVENT_LBUTTONDOWN )
	{
		p->setPonto(x, y);
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
	std::string filename = "../img/colored/messi.jpg" ;
	//std::string filename = "../img/grayscale/messi.jpg" ;
	Ponto p 	= Ponto(1, 1);
	Ponto last  = Ponto(-2, -1);
	Imagem Figura;
	cv::Mat tmp;
	const int distancia = 13;
	int key;
	bool grayscale = false;
	Pixel vermelho = Pixel(255, 0, 0);

	cv::VideoCapture cap(0);

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
	cv::setMouseCallback(window_name, CallBackFunc, &p);
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

		
		if(p.x != last.x || p.y != last.y)
		{
			exibe_resultado(&Figura, &p);
			last.x = p.x;
			last.y = p.y;
		}
		Figura.PintaDistancia(distancia, vermelho);
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