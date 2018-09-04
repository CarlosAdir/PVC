#ifndef ELEMENTOS_H_INCLUDED
#define ELEMENTOS_H_INCLUDED

#include "opencv2/highgui/highgui.hpp"
#include <iostream>

class ArquivoNaoExiste
{
private:
	std::string nomeArquivo;
public:
	ArquivoNaoExiste(std::string);
	void Msg();
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


class Ponto
{
public:
	int x, y;
	Ponto(int, int);
	Ponto();
	void setPonto(int x, int y);
	friend std::ostream& operator<< (std::ostream& os, Ponto &p);
};



int distancia_quadrado(Pixel p, Pixel q);


class imagem
{
private:
	std::string filename;
	cv::Mat img;
	int rows, cols;
	bool gray;
	bool isGrayScale();

	Pixel referencia;
	bool alreadyReferencia;
public:
	imagem();


	void setPixel(const Ponto q, const Pixel p);
	void setPixel(const int x, const int y, const Pixel p);
	Pixel getPixel(const Ponto p);
	Pixel getPixel(const int x, const int y);

	void setImg(const std::string filename);
	void setImg(const cv::Mat temp);
	cv::Mat getImg();
	
	bool isGray();
	
	void PintaDistancia(const int distancia, const Pixel nova_cor);

	void setReferencia(Pixel p);
	Pixel getReferencia();

	void reload();
	
};

#endif // DOMINIOS_H_INCLUDED
