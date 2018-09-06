Existem 4 pastas no trabalho. Primeiramente um breve resumo

*) cpp/		- Consiste na pasta em que contém os códigos implementados em C++
*) input/	- Consiste na pasta em que se coloca os inputs dos códigos, tanto imagens quanto videos.
*) LaTeX/ 	- Consiste na pasta em que agrupa os arquivos necessários para se fazer o relatório em LaTeX
*) py3/ 	- Consiste na pasta em que contém os códigos implementados em python3.

Na pasta cpp:
	Dentro da pasta cpp/, contém 7 arquivos: Um makefile para compilação dos códigos, uma biblioteca de declarações(elementos.hpp), a implementação da biblioteca(elementos.cpp), e 4 arquivos que satisfazem os requisitos do trabalho.
	Para encerramento de qualquer programa, basta apertar a tecla "ESC".
	Codigo 1.cpp:
		Satisfaz o requisito 1 do trabalho.
		Para funcionamento e verificação do código(ou seja, o código 1.cpp rodar), digitar no terminal o comando sem aspas: "make p1"
		Para mudar a imagem trabalhada, basta mudar o nome do arquivo dentro do código 1.cpp, exatamente nas linhas 44 e 45.
	Codigo 2.cpp:
		Satisfaz o requisito 2 do trabalho.
		Para funcionamento e verificação do código(ou seja, o código 2.cpp rodar), digitar no terminal o comando sem aspas: "make p2"
		Para mudar a imagem trabalhada, basta mudar o nome do arquivo dentro do código 2.cpp, exatamente nas linhas 49 e 50.
	Codigo 3.cpp:
		Satisfaz o requisito 3 do trabalho.
		Para funcionamento e verificação do código(ou seja, o código 3.cpp rodar), digitar no terminal o comando sem aspas: "make p3"
		Para mudar o video trabalhado, basta mudar o nome do arquivo dentro do código 3.cpp, exatamente nas linhas 57.
		Como junto dos algoritmos não será mandado um video(devido ao peso do video), será necessário indicar o caminho corretamente. Para fazer isso, basta colocar o video dentro da pasta "input/video/" e alterar a linha 57.
	Codigo 4.cpp:
		Satisfaz o requisito 4 do trabalho.
		Para funcionamento e verificação do código(ou seja, o código 4.cpp rodar), digitar no terminal o comando sem aspas: "make p4"
		Como não precisa de arquivo de input, o único problema acontecerá se a câmera não for iniciada. Para mudar a câmera de entrada, basta modificar na linha 57.

Na pasta input:
	Serve apenas para organização, sua estrutura não importa muito desde que os algoritmos sejam adaptados nas linhas especificadas.
	Dentro dessa pasta contém duas pastas chamadas img/ e video/
	Essas pastas servem para separar os videos das imagens.

Na pasta LaTeX:
	Contém duas pastas: uma chamada "img" e outra chamada "tex".
	Dentro da pasta "img" contém todas as imagens necessárias para o LaTeX. O LaTeX não precisa das imagens dos inputs e vice-versa.
	Dentro da pasta "tex" contém os textos do relatório, separados nos tópicos do relatório tais como introdução, resultados, conclusão, etc.

	Além disso, contém diversos arquivos necessários para o LaTeX:
	main.pdf:
		É o arquivo PDF do relatório. É o objeto final da compilação do LaTeX
	main.tex:
		É o arquivo LaTeX com a estrutura principal e inclui os arquivos dentro da pasta tex.
	makefile:
		É o arquivo para fazer a compilação e execução do LaTeX. Os comandos necessários se resumem a "pdflatex main", "bibtex main" e a chamada de um leitor de PDF. Para compilação automática, basta digitar no terminal "make". Para retirada dos arquivos temporários do LaTeX, basta digitar "make clean"
	refs.bib:
		Arquivo que contém as referências
	restantes:
		Arquivos necessários para o template LaTeX.


Na pasta py3:
	Não foi implementado quase nada em python para o problema, embora tenha se estudado. Contém apenas um arquivo de abertura de uma imagem

Sobre o sistema:
	OpenCV: 			4.0.0-pre
	Operational system: Ubuntu 16.04.10
	Compilador C++	  : g++ 5.4.0
	Versão do python3 : Python 3.5.2
	Meio de Compilação: mostrado no makefile 
	PDFLaTeX:			pdfTeX 3.14159265-2.6-1.40.16 (TeX Live 2015/Debian)
						kpathsea version 6.2.1
	BibTex:				BibTeX 0.99d (TeX Live 2015/Debian)
						kpathsea version 6.2.1
	Evince:				NOME Document Viewer 3.18.2


Link do GitHub:	https://github.com/CarlosAdir/PVC 
  Link do Wiki:	https://github.com/CarlosAdir/PVC/wiki