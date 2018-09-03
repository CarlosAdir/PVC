#include "elementos.hpp"

ArquivoNaoExiste::ArquivoNaoExiste(std::string arch)
{
	this->nomeArquivo = arch;
}
void ArquivoNaoExiste::Msg()
{
	std::cout << "O arquivo " << nomeArquivo << " nao existe\n\n";
}





void Pixel::setColor(uchar r, uchar g, uchar b)
{
	this->r = r;
	this->g = g;
	this->b = b;
}
Pixel::Pixel()
{
	this->setColor(0, 0, 0);
}
Pixel::Pixel(uchar r, uchar g, uchar b)
{
	this->setColor(r, g, b);
}
std::ostream& operator<< (std::ostream& os, Pixel &p)
{
	os << "(" << int(p.r)  << ", " << int(p.g) << ", " << int(p.b) << ")";
	return os;
}
int distancia_quadrado(Pixel p, Pixel q)
{
	int dr, dg, db;
	dr = int(p.r)-q.r;
	dg = int(p.g)-q.g;
	db = int(p.b)-q.b;
	/*
	if(dr == dg && dg == db):
		return dr*dr;
	*/
	return dr*dr + dg*dg + db*db; 
}







imagem::imagem()
{
	this->img = cv::Mat();
	this->rows = 0;
	this->cols = 0;
	alreadyReferencia = false;
}

bool imagem::isGrayScale()
{
	int i, j;
	this->rows = this->img.rows;
	this->cols = this->img.cols; 
	cv::Vec3b a;
	for(i = 0; i < this->rows; i++)
		for(j = 0; j < this->cols; j++)
		{
			a = this->img.at<cv::Vec3b>(i, j);
			if(a[0] != a[1] or a[1] != a[2])
				return false;
		}
	return true;
}

void imagem::setImg(const std::string filename)
{
	this->filename = filename;
	cv::Mat temp = cv::imread(filename);
	if(temp.empty())
		throw ArquivoNaoExiste(filename); 
	this->img = temp;
	this->gray = this->isGrayScale();
}
void imagem::setImg(const cv::Mat temp)
{; 
	this->img = temp;
	this->gray = this->isGrayScale();
}
bool imagem::isGray()
{
	return this->gray;
}
cv::Mat imagem::getImg()
{
	return this->img;
}

Pixel imagem::getPixel(const int x, const int y)
{
	cv::Vec3b a = this->img.at<cv::Vec3b>(y, x);
	Pixel p(a[2], a[1], a[0]);
	return p;
}
void imagem::setPixel(const int x, const int y, const Pixel p)
{
	this->img.at<cv::Vec3b>(y, x) = cv::Vec3b(p.b, p.g, p.r);
}
void imagem::PintaDistancia(const int distancia, const Pixel nova_cor)
{
	int x, y;
	if(change)
		for(y = 0; y < this->rows; y++)
			for(x = 0; x < this->cols; x++)
				if(  distancia_quadrado(this->getPixel(x, y), this->referencia) < distancia*distancia)
					this->setPixel(x, y, nova_cor);
}
void imagem::setReferencia(Pixel p)
{
	this->alreadyReferencia = true;

	this->referencia.r = p.r;
	this->referencia.g = p.g;
	this->referencia.b = p.b;
}
Pixel imagem::getReferencia()
{
	return this->referencia;
}