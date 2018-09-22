#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np

global fila

class Point():
    """docstring for Point"""
    def __init__(self, x, y):
        self.set(x, y)
    def to_tuple(self):
        return (self.x, self.y)
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def set(self, x, y):
        self.x = x
        self.y = y

        
class MouseEvent(object):
    """docstring for MouseEvent"""
    def __init__(self, x, y, event):
        self.x = x
        self.y = y
        self.e = event
    def setPoint(self, point):
        if type(point) == Point:
            self.x = point.getX()
            self.y = point.getY()
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getE(self):
        return self.e 
        
draw_line = False					# After that get two points
draw_continuos_line = False			# If there is only one point and you need
									# to draw the line between the frist point
									# and the mouse point at exactly moment
pmouse = Point(200, 200)			# To keep the actual mouse point and keep
									# the 'fila' empty
p1, p2 = Point(0, 0), Point(0, 0)
numero_linha = 1
fila = []

THICK = 3
FONT = cv2.FONT_HERSHEY_SIMPLEX
RED = (0,0,255)					# Blue Green Red
BLUE = (255,0,0)
GREEN = (0,255,0)
FONT_SIZE = 0.7

def get_point(event, x, y, flags, param): #funcao de callback do mouse
	global fila
	fila.append(MouseEvent(x, y, event))
        
        
cap = cv2.VideoCapture(0)

cv2.namedWindow('Requisito 1')
cv2.setMouseCallback('Requisito 1', get_point)

while(True):
	ret, img = cap.read()
	if cv2.waitKey(20) == 27 or ret == False:
		break

	while len(fila):
		evento = fila.pop(0)
		if evento.getE() == cv2.EVENT_MOUSEMOVE:
			pmouse.set(evento.getX(), evento.getY())
		# To treat the left button click event
		elif evento.getE() == cv2.EVENT_LBUTTONDOWN:
			if draw_continuos_line:
				p2.set(evento.getX(), evento.getY())
				draw_line = True
				draw_continuos_line = False
				print("Line #" + str(numero_linha))
				numero_linha += 1
				print("Point 1 = (x1, y1) = (" + str(p1.getX()) + ", " + str(p1.getY()) + ")")
				print("Point 2 = (x2, y2) = (" + str(p2.getX()) + ", " + str(p2.getY()) + ")")
				euc_dist = ((p1.getX()-p2.getX())**2 + (p1.getY() - p2.getY())**2)**(1/2.0)
				print("Euclidian Distance = " + str("%.4f" % euc_dist) + "\n")

			else:
				p1.set(evento.getX(), evento.getY())
				draw_line = False
				draw_continuos_line = True

		# EVENT_RBUTTONDOWN
		# EVENT_MBUTTONDOWN


	# To draw the line on the screen
	if draw_line or draw_continuos_line:
		if draw_line:
			final_point = p2
		else:
			final_point = pmouse
		cv2.line(img, p1.to_tuple(), final_point.to_tuple(), RED, thickness=THICK)
		ponto_texto = (int((p1.getX()+final_point.getX())/2), int((p1.getY()+final_point.getY())/2))
		texto = "%.2f" % ((p1.getX()-final_point.getX())**2+(p1.getY()-final_point.getY())**2)**(1/2.)
		cv2.putText(img, texto, ponto_texto, FONT, FONT_SIZE, GREEN, 2,cv2.LINE_AA)
		cv2.putText(img, str(p1.to_tuple()), p1.to_tuple(), FONT, FONT_SIZE, GREEN, 2,cv2.LINE_AA)
		cv2.putText(img, str(final_point.to_tuple()), final_point.to_tuple(), FONT, FONT_SIZE, GREEN, 2,cv2.LINE_AA)
	cv2.imshow('Requisito 1', img)

cap.release()    
cv2.destroyAllWindows()
