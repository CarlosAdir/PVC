all: programa clean executar

p1: rename1 programa clean executar
	mv main.cpp 1.cpp

rename1:
	mv 1.cpp main.cpp

p2: rename2 programa clean executar
	mv main.cpp 2.cpp

rename2:
	mv 2.cpp main.cpp

p3: rename3 programa clean executar
	mv main.cpp 3.cpp

rename3:
	mv 3.cpp main.cpp

p4: rename4 programa clean executar
	mv main.cpp 4.cpp

rename4:
	mv 4.cpp main.cpp

programa: main.o elementos.o
	g++ main.o elementos.o -o executavel `pkg-config --cflags --libs opencv`

executar:
	./executavel

elementos.o:
	g++ -c -ggdb elementos.cpp -Wall -ansi -std=c++11

main.o: elementos.o
	g++ -c -ggdb main.cpp -Wall -ansi -std=c++11 -fpermissive

clean:
	rm *.o