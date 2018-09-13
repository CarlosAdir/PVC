#include "elementos.hpp"
#include <cmath>
#include <queue>

using namespace std;
using namespace cv;

void CallBackFunc(int event, int x, int y, int flags, void *f)
{
	queue<EventoMouse> *fila = 	(queue<EventoMouse> *)f;
	EventoMouse novo_evento = EventoMouse(x, y, event);
	fila->push(novo_evento);
}

void line(Imagem *img, cv::Point p1, cv::Point p2, Pixel color, int thickness = 3)
{
	int i, j;
	int xe, xd; // x esquerdo e x direito
	int yi, ys; // y inferior e y superior
	double a, b, c, d;
	a = p2.y-p1.y;
	b = p2.x-p1.x;
	c = p1.x*p2.y-p2.x-p1.y;
	d = sqrt(a*a+b*b);
	std::cout << "a = " << a << std::endl;
	std::cout << "b = " << b << std::endl;
	std::cout << "c = " << c << std::endl;
	std::cout << "d = " << d << std::endl;
	if(p1.x > p2.x)
	{	
		xe = p2.x;
		xd = p1.x;
	}
	else
	{
		xe = p1.x;
		xd = p2.x;
	}
	if(p1.y > p2.y)
	{
		yi = p2.y;
		ys = p1.y;
	}
	else
	{
		yi = p1.y;
		ys = p2.y;
	}
	for(i = yi; i <= ys; i++)
	{
		for(j = xe; j <= xd; j++)
		{
			if(abs(a*j+b*i+c)/d < thickness)
			{
				std::cout << "some" << std::endl;
				img->setPixel(j, i, color);
			}
		}
	}


}

int main(int argc, char** argv)
{
	queue<EventoMouse> fila;
	EventoMouse evento;
	Imagem *img = new Imagem();
	cv::Mat tmp;
	cv::String window_name = "Video Requisito 1";
	int key;

	// Para definir as cores
	Pixel black = Pixel(0, 0, 0);

	// Para determinar os pontos iniciais e finais para se medir a distância
	int xa, ya, xb, yb;
	bool pa = false, pb = false, draw_line = false;

	cv::VideoCapture cap(0);

	if (cap.isOpened() == false)  
	{
		std::cout << "Cannot open the video file. \nPress a Key" << std::endl;
		std::cin.get(); //wait for any key press
		return -1;
	}

	cv::namedWindow(window_name, cv::WINDOW_NORMAL);
	cv::setMouseCallback(window_name, CallBackFunc, (void *)&fila);

	while(true)
	{

		bool bSuccess = cap.read(tmp);
		if (bSuccess == false) 
		{
			std::cout << "Found the end of the video" << std::endl;
			break;
		}
		img->setImg(tmp);
		if(pa == true && pb == true)
		{
			std::cout << "Ponto 1 = (" << xa << ", " << ya << ");  Ponto 2 = (" << xb << ", " << yb << ")" << std::endl;
			std::cout << "Distancia euclidiana: d = " << sqrt((xa-xb)*(xa-xb)+(ya-yb)*(ya-yb)) << "\n" << std::endl;
			pa = pb = false;
		}
		if(draw_line == true)
		{
			//line(img, cv::Point(xa, ya), cv::Point(xb, yb), black, 3);
		}
		cv::imshow(window_name, img->getImg());
		key = cv::waitKey(10);
		while(!fila.empty())
		{
			evento = fila.front();
			if(evento.getT() == cv::EVENT_LBUTTONDOWN)
			{
				if(pa != false && pb == false)
				{
					xb = evento.getX();
					yb = evento.getY();
					pb = true;
					draw_line = true;
				}
				else
				{
					xa = evento.getX();
					ya = evento.getY();
					pa = true;	
					draw_line = false;
				}
			}
			//std::cout << evento << std::endl;
			fila.pop();
		}
		if(key == 27)
			break;
	}
	std::cout << "Esc key was pressed by user." << std::endl;
	delete img;
	return 0;

}