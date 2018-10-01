#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np
import usefull as use

global fila

        
draw_line = False					# After that get two points
draw_continuos_line = False			# If there is only one point and you need
									# to draw the line between the frist point
									# and the mouse point at exactly moment
pmouse = use.Point(200, 200)			# To keep the actual mouse point and keep
									# the 'fila' empty
p1, p2 = use.Point(0, 0), use.Point(0, 0)
numero_linha = 1
fila = []

get_event = lambda event, x, y, flags, param: use.get_event(event, x, y, flags, param, fila)        

cap = cv2.VideoCapture(0)

cv2.namedWindow('Requisito 1')
cv2.setMouseCallback('Requisito 1', get_event)

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
				print("use.Point 1 = (x1, y1) = (" + str(p1.getX()) + ", " + str(p1.getY()) + ")")
				print("use.Point 2 = (x2, y2) = (" + str(p2.getX()) + ", " + str(p2.getY()) + ")")
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
		cv2.line(img, p1.to_tuple(), final_point.to_tuple(), use.RED, thickness=use.THICK)
		ponto_texto = (int((p1.getX()+final_point.getX())/2), int((p1.getY()+final_point.getY())/2))
		texto = "%.2f" % ((p1.getX()-final_point.getX())**2+(p1.getY()-final_point.getY())**2)**(1/2.)
		cv2.putText(img, texto, ponto_texto, use.FONT, use.FONT_SIZE, use.GREEN, 2,cv2.LINE_AA)
		cv2.putText(img, str(p1.to_tuple()), p1.to_tuple(), use.FONT, use.FONT_SIZE, use.GREEN, 2,cv2.LINE_AA)
		cv2.putText(img, str(final_point.to_tuple()), final_point.to_tuple(), use.FONT, use.FONT_SIZE, use.GREEN, 2,cv2.LINE_AA)
	cv2.imshow('Requisito 1', img)

cap.release()    
cv2.destroyAllWindows()
