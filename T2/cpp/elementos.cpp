#include "elementos.hpp"

EventoMouse::EventoMouse(const unsigned char x, const unsigned char y, const unsigned char t)
{
	this->set(x, y, t);
}
EventoMouse::EventoMouse()
{
	this->set(-1, -1, 0);
}
unsigned char EventoMouse::getX()
{
	return this->x;
}
unsigned char EventoMouse::getY()
{
	return this->y;
}
unsigned char EventoMouse::getT()
{
	return this->t;
}
EventoMouse EventoMouse::get()
{
	return EventoMouse(this->x, this->y, this->t);
}
void EventoMouse::setX(const unsigned char x)
{
	this->x = x;
}
void EventoMouse::setY(const unsigned char y)
{
	this->y = y;
}
void EventoMouse::setT(const unsigned char t)
{
	this->t = t;
}
void EventoMouse::set(const unsigned char x, const unsigned char y, const unsigned t)
{
	this->x = x;
	this->y = y;
	this->t = t;
}
std::ostream& operator<< (std::ostream& os, EventoMouse &evento)
{
	os << "(" << int(evento.x)  << ", " << int(evento.y) << ") = ";
	if(evento.t == cv::EVENT_MOUSEMOVE)
		os << "Move";
	else if(evento.t == cv::EVENT_LBUTTONDOWN)
		os << "Left Down";
	else if(evento.t == cv::EVENT_RBUTTONDOWN)
		os << "Right Down";
	else if(evento.t == cv::EVENT_MBUTTONDOWN)
		os << "Middle Down";
	else if(evento.t == cv::EVENT_LBUTTONUP)
		os << "Left Up";
	else if(evento.t == cv::EVENT_RBUTTONUP)
		os << "Right Up";
	else if(evento.t == cv::EVENT_MBUTTONUP)
		os << "Middle Up";
	else if(evento.t == cv::EVENT_LBUTTONDBLCLK)
		os << "Left Blclk";
	else if(evento.t == cv::EVENT_RBUTTONDBLCLK)
		os << "Right Blclk";
	else if(evento.t == cv::EVENT_MBUTTONDBLCLK)
		os << "Middle Blclk";
	return os;
}




void Color::set(unsigned char r, unsigned char g, unsigned char b)
{
	this->r = r;
	this->g = g;
	this->b = b;
}
Color::Color()
{
	this->set(0, 0, 0);
}
Color::Color(unsigned char r, unsigned char g, unsigned char b)
{
	this->set(r, g, b);
}
const unsigned char Color::getR()
{
	return this->r;
}
const unsigned char Color::getG()
{
	return this->g;
}
const unsigned char Color::getB()
{
	return this->b;
}
std::ostream& operator<< (std::ostream& os, Color &p)
{
	os << "(" << p.getR()  << ", " << p.getG() << ", " << p.getB() << ")";
	return os;
}






Imagem::Imagem()
{
	this->img = cv::Mat();
}

void Imagem::setImg(const cv::Mat temp)
{ 
	this->img = temp;
}
cv::Mat Imagem::getImg()
{
	return this->img;
}

Color Imagem::getColor(const int x, const int y)
{
	cv::Vec3b a = this->img.at<cv::Vec3b>(y, x);
	Color novo = Color(a[2], a[1], a[0]);
	return novo;
}

void Imagem::setColor(const int x, const int y, const Color p)
{
	Color k = p;
	this->img.at<cv::Vec3b>(y, x) = cv::Vec3b(k.getB(), k.getG(), k.getR());
}
Imagem::~Imagem()
{
	
}