all: programa clean executar

programa: main.o elementos.o
	g++ main.o elementos.o -o exe `pkg-config --cflags --libs opencv`

main.o: elementos.o
	g++ -c -ggdb main.cpp -Wall -ansi -std=c++11 -fpermissive

elementos.o:
	g++ -c -ggdb elementos.cpp -Wall -ansi -std=c++11

executar:
	./exe

clean:
	if [ "`ls -1 *.o 2>/dev/null | wc -l`" != 0 ]; then rm *.o; fi


