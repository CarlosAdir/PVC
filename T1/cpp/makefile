all: programa1 clean executar

programa1: main.o elementos.o
	g++ main.o elementos.o -o executavel `pkg-config --cflags --libs opencv`

executar:
	./executavel

elementos.o:
	g++ -c -ggdb elementos.cpp -Wall -ansi -std=c++11

main.o: elementos.o
	g++ -c -ggdb main.cpp -Wall -ansi -std=c++11 -fpermissive

clean:
	rm *.o