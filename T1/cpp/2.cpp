#include "elementos.hpp"

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
	Ponto p 	= Ponto(-1, -1);
	Ponto last  = Ponto(-1, -1);
	Pixel vermelho = Pixel(255, 0, 0);
	int distancia = 13;
	Imagem Figura;
	int key;

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
	cv::setMouseCallback("My Window", CallBackFunc, (void *)(&p));


	
	cv::imshow("My Window", Figura.getImg());
	// Wait until user press some key
	while(true)
	{
		if(p.x != last.x || p.y != last.y)
		{
			Figura.reload();
			exibe_resultado(&Figura, &p);
			last.x = p.x;
			last.y = p.y;
			Figura.PintaDistancia(distancia, vermelho);
			cv::imshow("My Window", Figura.getImg());
		}
		key = cv::waitKey(10);
		if(key == 27)
			break;
		else if(key == 'r')
			Figura.setImg(filename);
	}
	std::cout << "Esc key was pressed by user." << std::endl;
	
	return 0;

}