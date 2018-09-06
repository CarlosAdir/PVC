Neste repositório contém os arquivos de implementação do Trabalho 1. Para saber mais sobre o [Trabalho 1](https://github.com/CarlosAdir/PVC/wiki/Trabalho1), visite o [Wiki](https://github.com/CarlosAdir/PVC/wiki/)

# Organização das pastas

Existem 4 pastas no trabalho e consistem em:

* **cpp**	- Contém todos os códigos implementados em C++
* **input**	- Agrupa todos os inputs dos códigos, podendo ser imagem, videos ou outros arquivos.
* **LaTeX** - Agrupa os arquivos necessários para se fazer o relatório em LaTeX
* **py3** 	- Contém os códigos implementados em python3.

## cpp

Dentro dessa pasta há 7 arquivos

* **makefile**: Para facilitar a compilação dos códigos
* **elementos.hpp**: As declarações das classes e funções auxiliares
* **elementos.cpp**: Implementações das classes e funções auxiliares
* **1.cpp**: Satisfaz o requisito 1 do trabalho. Para funcionamento e verificação do código, digitar no terminal o comando: ```make p1```. Para mudar a imagem trabalhada, basta mudar o nome do arquivo dentro do código ```1.cpp```, exatamente nas linhas 44 e 45.
* **2.cpp**: Satisfaz o requisito 2 do trabalho. Para funcionamento e verificação do código, digitar no terminal o comando: ```make p2```. Para mudar a imagem trabalhada, basta mudar o nome do arquivo dentro do código ```2.cpp```, exatamente nas linhas 49 e 50.
* **3.cpp**: Satisfaz o requisito 3 do trabalho. Para funcionamento e verificação do código, digitar no terminal o comando: ```make p3```. Para mudar o video trabalhado, basta mudar o nome do arquivo dentro do código ```3.cpp```, exatamente nas linhas 57. Como junto dos algoritmos não será mandado um video(devido ao peso do video), será necessário indicar o caminho corretamente. Para fazer isso, basta colocar o video dentro da pasta ```input/video/``` e alterar a linha 57.
* **4.cpp**: Satisfaz o requisito 4 do trabalho. Para funcionamento e verificação do código, digitar no terminal o comando: ```make p4```. Como não precisa de arquivo de input, o único problema acontecerá se a câmera não for iniciada. Para mudar a câmera de entrada, basta modificar na linha 57.
	

## input

Serve apenas para organização, sua estrutura não importa muito desde que os algoritmos sejam adaptados nas linhas especificadas.

Dentro dessa pasta contém duas pastas chamadas ```img``` e ```video```

Essas pastas servem para separar os videos das imagens bem como separar imagens coloridas das imagens em escala cinza.

## LaTeX

#### Dentro dessa pasta contém duas pastas:

* **img**: Contém as apenas as imagens necessárias para o LaTeX. O LaTeX não precisa das imagens dos inputs e vice-versa.
* **tex**: Contém os textos do relatório, separados nos tópicos do relatório.

#### E outros arquivos necessários para o LaTeX:

* **main.pdf**: É o arquivo PDF do relatório. É o objeto final da compilação do LaTeX;
* **main.tex**: É o arquivo LaTeX com a estrutura principal e inclui os arquivos dentro da pasta ```tex```.
* **makefile**: É o arquivo para fazer a compilação e execução do LaTeX;
* **refs.bib**: Arquivo que contém as referências;
* **arquivos restantes**: Arquivos necessários para o template LaTeX.

#### Para utilizar o código

Para compilar os arquivos LaTeX, os comandos são digitados através do terminal e se resumem a:

* pdflatex main
* bibtex main

Ou para facilitar a compilação e abertura do arquivo, utiliza-se o makefile:

* Para compilação automática, basta digitar no terminal o comando ```make```.
* Para retirada dos arquivos temporários gerados automaticamente pelo LaTeX, basta digitar ```make clean```.

Vale a pena dizer que as referências são corretamente adicionadas ao PDF após a terceira compilação. Isso acontece porque para ocorrer o link entre as referências e o arquivo LaTeX deve-se ter os arquivos temporários.


## py3

Não foi implementado quase nada em python para o problema, embora tenha se estudado e os algoritmos presentes dentro da pasta ```testes```.

Contém apenas um arquivo de abertura de uma imagem.


# Configurações do sistema

   Software    | Versão
-------------- | ------
OpenCV         | 4.0.0-pre
OS             | Ubuntu 16.04.10
Compilador C++ | g++ 5.4.0
Python3        | Python 3.5.2

Para compilador LaTeX

* TeX Live 2015/Debian
* pdfTeX 3.14159265-2.6-1.40.16
* BibTeX 0.99d
* kpathsea version 6.2.1


