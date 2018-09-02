to compile 1.cpp

g++ -Wall -ansi -ggdb 1.cpp -o teste `pkg-config --cflags --libs opencv` -std=c++11