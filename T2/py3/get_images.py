#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import cv2
import sys
import os

def cria_pasta(caminho):
	os.system('if [ ! -d "' + caminho + '" ]; then mkdir ' + caminho + '; fi')

def remove_todos_arquivos(arch):
	os.system('rm ' + arch)

def grava_grupo_imagens(cap):
	global board_w
	global board_h
	global frame_step
	global criteria
	global W
	global H

	board_total = board_w * board_h
	board_sz = (board_w, board_h)

	successes = 1
	actualframe = 0
	while(successes <= n_boards):
		ret, frame = cap.read()
		if ret == True:
			#frame = cv2.resize(frame, (W, H))
			gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
			actualframe += 1
			actualframe %= frame_step
			if(actualframe == 0):
				ret, corners = cv2.findChessboardCorners(gray, board_sz,None)
				if ret == True: # If it was possible to find the corners of Chessboard
					cv2.imwrite(pasta_img + str(i) + "_" + str(successes) + '.png', frame)
					img2 = np.copy(frame)
					cv2.drawChessboardCorners(img2, board_sz, corners,ret)
					cv2.imshow('Snapshot', img2)
					print("Interaction: [" + str(i) + "/" + str(n_iter) + "] - [" + str(successes) + "/" + str(n_boards) + "]")
					successes += 1
				else:
					successes = 1
					cv2.imshow('Snapshot', gray)
				cv2.imshow('Raw Video', gray)
		if cv2.waitKey(1) == 27:
			cap.release()
			cv2.destroyAllWindows()
			print("The user pressed the ESC key and the program was finished")
			sys.exit(1)
	cv2.destroyWindow('Snapshot')

CAMERA		= 0
pasta_img	= "../data/img/"
n_boards	= 10
n_iter		= 1
frame_step	= 15
H, W		= 720, 1280
board_w, board_h = 8, 6
#board_w, board_h = 12, 9
#board_w, board_h = 24, 19
if __name__ == "__main__":
	cria_pasta("../data/")
	cria_pasta("../data/img/")
	remove_todos_arquivos("../data/img/*.npy")
	if True:
		try:
			n_boards = int(sys.argv[2])
		except:
			n_boards = 10
		try:
			n_iter = int(sys.argv[1])
		except:
			n_iter = 1
	cap = cv2.VideoCapture(CAMERA)
	if not cap.isOpened():
		print("It was not possible to start the camera")
		sys.exit(1)
	for i in range(1, n_iter+1): # The algorithm will pick n_inter packages of images to calibrate
		grava_grupo_imagens(cap)
		print("Gravado o grupo de imagem " + str(i))
	cap.release()
	cv2.destroyAllWindows()
