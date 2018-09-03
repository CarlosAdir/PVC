#include "elementos.hpp"


void CallBackFunc(int event, int x, int y, int flags, void *F)
{

	imagem *Figura = (imagem *)F;
	Pixel p(255, 0, 0);
	if  ( event == cv::EVENT_LBUTTONDOWN )
	{
		p = Figura->getPixel(x, y);
		std::cout << "Ponto: (" << x << ", " << y << ") - ";
		if(Figura->isGray())
		{
			std::cout << "Intensidade = " << int(p.r) << std::endl;
		}
		else
		{
			std::cout << "rgb = " << p << std::endl;
		}
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
	std::string filename = "../img/grayscale/messi.jpg" ;
	imagem Figura;
	try
	{
		Figura.setImg(filename);
	}
	catch (ArquivoNaoExiste A)
	{
		A.Msg();
		return 0;
	}

	if(Figura.isGray())
		std::cout << "A imagem eh preta e branca" << std::endl;
	else
		std::cout << "A imagem eh colorida" << std::endl;

	//Create a window
	cv::namedWindow("My Window", 1);

	//set the callback function for any mouse event
	cv::setMouseCallback("My Window", CallBackFunc, &Figura);

	// Wait until user press some key
	do
	{
		cv::imshow("My Window", Figura.getImg());
	}while(cv::waitKey(0) != 27);
	std::cout << "Esc key was pressed by user." << std::endl;
	
	return 0;

}