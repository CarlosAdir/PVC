#include "elementos.hpp"


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
	std::string filename = "../img/grayscale/messi.jpg" ;
	imagem Figura;
	int key;

	//Create a window
	cv::namedWindow("My Window", 1);

	//set the callback function for any mouse event
	cv::setMouseCallback("My Window", CallBackFunc, &Figura);

	// Wait until user press some key
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
	while(true)
	{
		cv::imshow("My Window", Figura.getImg());
		key = cv::waitKey(10);
		if(key == 27)
			break;
		else if(key == 'r')
			Figura.setImg(filename);
	}
	std::cout << "Esc key was pressed by user." << std::endl;

	return 0;

}