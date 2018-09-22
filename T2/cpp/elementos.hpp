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


class Color
{
private:
	unsigned char r, g, b;
public:
	Color();
	Color(unsigned char r, unsigned char g, unsigned char b);
	void set(unsigned char r, unsigned char g, unsigned char b);
	const unsigned char getR();
	const unsigned char getG();
	const unsigned char getB();
	friend std::ostream& operator<< (std::ostream& os, Color &p);
};


class Imagem
{
private:
	cv::Mat img;
public:
	Imagem();
	void setColor(const int x, const int y, const Color p);
	Color getColor(const int x, const int y);
	void setImg(const cv::Mat temp);
	cv::Mat getImg();
	~Imagem();
};

#endif