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

int main(int argc, char** argv)
{
	queue<EventoMouse> fila;
	EventoMouse evento;
	Imagem *img = new Imagem();
	cv::Mat tmp;
	cv::String window_name = "Video Requisito 1";
	int key;

	// Para definir as cores
	//Color black = Color(0, 0, 0);
	const Scalar black = Scalar(0);
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
			// Nao ha a funcao linha na opencv, embora a documentacao fale que exista
			//cv::line(img->getImg(), cv::Point(xa, ya), cv::Point(xb, yb), black);
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