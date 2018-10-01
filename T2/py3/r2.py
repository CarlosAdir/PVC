#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np
import sys
import usefull as use



def atualiza_filas_eventos(raw, und):
	global last_event
	global p1
	global p2
	global pmouse
	global filas
	global draw_continuos_line
	global draw_line
	for i, fila in enumerate(filas):
		while len(fila):
			last_event = i
			evento = fila.pop(0)
			if evento.getE() == cv2.EVENT_MOUSEMOVE:
				pmouse[i].set(evento.getX(), evento.getY())
			# To treat the left button click event
			elif evento.getE() == cv2.EVENT_LBUTTONDOWN:
				if draw_continuos_line:
					p2[i].set(evento.getX(), evento.getY())
					draw_line = True
					draw_continuos_line = False
				else:
					p1[i].set(evento.getX(), evento.getY())
					draw_line = False
					draw_continuos_line = True


	if last_event == 1: # That means that the last event was on the raw screen
		img = raw
	else:
		img = und
	# To draw the line on the screen
	if draw_line or draw_continuos_line:
		if draw_line:
			final_point = p2[last_event]
		else:
			final_point = pmouse[last_event]
		cv2.line(img, p1[last_event].to_tuple(), final_point.to_tuple(), use.RED, thickness=use.THICK)
		ponto_texto = (int((p1[last_event].getX()+final_point.getX())/2), int((p1[last_event].getY()+final_point.getY())/2))
		texto = "%.2f" % ((ponto_texto[0])**2+(ponto_texto[1])**2)**(1/2.)
		cv2.putText(img, texto, ponto_texto, use.FONT, use.FONT_SIZE, use.GREEN, 2,cv2.LINE_AA)
		cv2.putText(img, str(p1[last_event].to_tuple()), p1[last_event].to_tuple(), use.FONT, use.FONT_SIZE, use.GREEN, 2,cv2.LINE_AA)
		cv2.putText(img, str(final_point.to_tuple()), final_point.to_tuple(), use.FONT, use.FONT_SIZE, use.GREEN, 2,cv2.LINE_AA)

	return raw, und
	# EVENT_RBUTTONDOWN
	# EVENT_MBUTTONDOWN


# To the frist requisit
draw_line = False					# After that get two points
draw_continuos_line = False			# If there is only one point and you need
									# to draw the line between the frist point
									# and the mouse point at exactly moment
pmouse 	   = [use.Point(200, 200),\
			  use.Point(200, 200)]		# To keep the actual mouse point and keep		
									# the 'fila' empty
p1		   = [use.Point(0, 0), use.Point(0, 0)]
p2 		   = [use.Point(0, 0), use.Point(0, 0)]
filas      = [[], []]
numero_linha = 1
last_event = 1

# To the second

# pastas = []
#pastas.append("../data/longe/")
#pastas.append("../data/medio/")
#pastas.append("../data/curto/")
# pastas.append("../data/img/")

pasta = "../data/img_r2/"

if __name__ == "__main__":
	cap = cv2.VideoCapture(use.CAMERA)	# Open the camera
	if not cap.isOpened():
		print("It was not possible to start the camera")
		sys.exit(1)

	get_event1 = lambda event, x, y, flags, param:use.get_event(event, x, y, flags, param, filas[0])
	get_event2 = lambda event, x, y, flags, param:use.get_event(event, x, y, flags, param, filas[1])
	cv2.namedWindow('Undistort Video')
	cv2.setMouseCallback('Undistort Video', get_event1)
	cv2.namedWindow('Raw Video')
	cv2.setMouseCallback('Raw Video', get_event2)

	n_pack, n_img = use.number_images(pasta)
	if n_pack == 0: # Ou seja, nao tem nenhum pacote
		print("Faltam imagens dentro da pasta " + str(pasta) + "para poder rodar o algoritmo!")
		print("Primeiro rode o algoritmo chamado get_images e coloque as imagens necessarias na pasta de interesse")
		sys.exit(1)
	else:
		print("Medidas para a pasta " + pasta)
		intr_med, dist_med = use.get_statistics_matrices(pasta, n_pack, n_img)
		newcameramtx, roi = cv2.getOptimalNewCameraMatrix(intr_med,dist_med,(use.W,use.H),1,(use.W,use.H))
		
		

		w, h = use.W, use.H
		while(True):					# The main loop where the raw image and undistorted img are
			ret, frame = cap.read()
			#frame = cv2.resize(frame, (w, h))
			#gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

			#mapx,mapy = cv2.initUndistortRectifyMap(intr_med,dist_med,None,newcameramtx,(w,h),5)
			mapx,mapy = cv2.initUndistortRectifyMap(intr_med,dist_med,None,newcameramtx,(use.W,use.H),5)
			undst_img = cv2.remap(frame,mapx,mapy,cv2.INTER_LINEAR)

			# crop the image
			x, y, w,h = roi
			#undst_img = undst_img[y:y+h, x:x+w]
			undst_img = undst_img[0:use.H, 0:use.W]
			
			frame, undst_img = atualiza_filas_eventos(frame, undst_img)

			cv2.imshow('Raw Video', frame)
			cv2.imshow('Undistort Video',undst_img)

			if cv2.waitKey(1) == 27:
				break
	cv2.destroyAllWindows()

	cap.release()



