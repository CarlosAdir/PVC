#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import cv2
import sys
import os

BOARD_W, BOARD_H = 8, 6

BOARD_TOTAL = BOARD_W * BOARD_H
BOARD_SZ = (BOARD_W, BOARD_H)


if __name__ == "__main__":
	arquivos = []
	pasta = "../data/img_r2/"
	for i in range(1, 6):
		arquivos.append(pasta + str(i) + "_10.png")

	i = 0
	for arquivo in arquivos:
		frame = cv2.imread(arquivo,1)
		ret, corners = cv2.findChessboardCorners(frame, BOARD_SZ,None)
		if ret == True: # If it was possible to find the corners of Chessboard
			cv2.drawChessboardCorners(frame, BOARD_SZ, corners,ret)
			cv2.imwrite(str(i) + '.png', frame)
		i += 1