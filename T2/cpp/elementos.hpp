#ifndef ELEMENTOS_H_INCLUDED
#define ELEMENTOS_H_INCLUDED

#include "opencv2/highgui/highgui.hpp"
#include <iostream>

class EventoMouse
{
private:
	unsigned char x, y;
	unsigned char t;
public:
	EventoMouse();
	EventoMouse(const unsigned char x, const unsigned char y, const unsigned char t);
	unsigned char getX();
	unsigned char getY();
	unsigned char getT();
	EventoMouse get();
	void setX(const unsigned char x);
	void setY(const unsigned char y);
	void setT(const unsigned char t);
	void set(const unsigned char x, const unsigned char y, const unsigned t);
	friend std::ostream& operator<< (std::ostream& os, EventoMouse &evento);
};


class Pixel
{
private:
	void setColor(uchar r, uchar g, uchar b);
public:
	uchar r, g, b;
	bool isGray();
	Pixel();
	Pixel(uchar r, uchar g, uchar b);
	friend std::ostream& operator<< (std::ostream& os, Pixel &p);
};


class Imagem
{
private:
	cv::Mat img;
public:
	Imagem();
	void setPixel(const int x, const int y, const Pixel p);
	Pixel getPixel(const int x, const int y);
	void setImg(const cv::Mat temp);
	cv::Mat getImg();
	~Imagem();
};

#endif