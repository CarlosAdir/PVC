all: programa clean executar

programa: main.o elementos.o
	g++ main.o elementos.o -o executavel `pkg-config --cflags --libs opencv`

executar:
	./executavel

elementos.o:
	g++ -c -ggdb elementos.cpp -Wall -ansi -std=c++11

main.o: elementos.o
	g++ -c -ggdb main.cpp -Wall -ansi -std=c++11 -fpermissive

clean:
	if [ "`ls -1 *.o 2>/dev/null | wc -l`" != 0 ]; then rm *.o; fi