#include "elementos.hpp"

void exibe_resultado(imagem *Figura, Ponto *p)
{
	Pixel pix = Figura->getPixel(*p);
	std::cout << "Ponto: " << *p << " - ";
	if(Figura->isGray())
	{
		std::cout << "Intensidade = " << int(pix.r) << std::endl;
	}
	else
	{
		std::cout << "rgb = " << pix << std::endl;
	}
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
	Ponto last  = Ponto(-2, -1);
	imagem Figura;
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


	

	// Wait until user press some key
	while(true)
	{
		if(p.x != last.x || p.y != last.y)
		{
			exibe_resultado(&Figura, &p);
			last.x = p.x;
			last.y = p.y;
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