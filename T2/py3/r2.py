#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np
import sys



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
        

def get_point(event, x, y, flags, param, fila): #funcao de callback do mouse
	fila.append(MouseEvent(x, y, event))
        
def there_is(arch):
	try:
		arq = open(arch, "r")
		arq.close()
		return True
	except:
		return False

def number_images(pasta):
	n_pack, n_img = 0, []
	i = 1
	while i < 10:
		j = 1
		if not there_is(pasta+str(i) + "_" + str(j) + ".png"):
			n_pack = i-1
			break
		while j < 50:
			if not there_is(pasta+str(i) + "_" + str(j) + ".png"):
				n_img.append(j)
				break
			j += 1
		i += 1
	for i in range(1, n_pack+1):
		n_img_min = min(n_img)
	if n_img_min == 0:
		n_pack = 0
	return n_pack, n_img_min

def get_points(pack):
	'''
	This function gets all the points from on specific package, which we called pack
	'''
	global BOARD_W
	global BOARD_H
	global pasta
	global n_pack
	global n_img
	#global criteria

	BOARD_TOTAL = BOARD_W * BOARD_H
	BOARD_SZ = (BOARD_W, BOARD_H)

	objp = np.zeros((BOARD_TOTAL,3), np.float32)
	objp[:,:2] = np.mgrid[0:BOARD_W,0:BOARD_H].T.reshape(-1,2)
	objpoints = [] # 3d point in real world space
	imgpoints = [] # 2d points in image plane.

	successes = 1

	while(successes < n_img):
		if not there_is(pasta + str(pack) + "_" + str(successes) + '.png'):
			print("Hey! There is no file called '" + pasta+str(pack)+"_"+str(successes)+'.png' + "'")
		else:
			gray = cv2.imread(pasta + str(pack) + "_" + str(successes) + '.png',0) # the 0 number means that the image will load at grayscale
			#frame = cv2.resize(frame, (1200//2, 720//2))
			ret, corners = cv2.findChessboardCorners(gray, BOARD_SZ,None)
			if ret == True:
				objpoints.append(objp)
				#corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
				imgpoints.append(corners)
				print("Interaction: [" + str(pack) + "/" + str(n_pack) + "] - [" + str(successes) + "/" + str(n_img) + "]")
				successes += 1

	return objpoints, imgpoints, gray

def get_matrices():
	global pasta
	global n_pack
	global n_img
	intr_list = []
	dist_list = []
	print(pasta)
	for pack in range(1, n_pack+1):
		if there_is(pasta + "intr_%d.npy" % pack) and there_is(pasta + "dist_%d.npy" % pack):
			intr = np.load(pasta + "intr_%d.npy" % pack)
			dist = np.load(pasta + "dist_%d.npy" % pack)
		else:
			objpoints, imgpoints, gray = get_points(pack)
			print('Calibrating the camera now...')
			ret, intr, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1],None,None)
			print('rvecs = ' + str(rvecs))
			print('tvecs = ' + str(tvecs))
			#Save values to file
			np.save(pasta + 'intr_%d' % pack, intr)
			np.save(pasta + 'dist_%d' % pack, dist)
			del objpoints
			del imgpoints
		print(intr)
		intr_list.append(intr)
		dist_list.append(dist)
	return tuple(intr_list), tuple(dist_list)

def get_statistics_matrices():
	global pasta
	global n_pack
	global n_img	
	intr_list, dist_list = get_matrices()
	if there_is(pasta+"dist_std.npy"):
		intr_med = np.load(pasta+"intr_med.npy")
		intr_std = np.load(pasta+"intr_std.npy")
		dist_med = np.load(pasta+"dist_med.npy")
		dist_std = np.load(pasta+"dist_std.npy")
	else:
		intr_med = np.mean(intr_list, axis = 0)
		intr_std = np.std(intr_list, axis = 0)
		dist_med = np.mean(dist_list, axis = 0)
		dist_std = np.std(dist_list, axis = 0)
		np.save(pasta + 'intr_med.npy', intr_med)
		np.save(pasta + 'intr_std.npy', intr_std)
		np.save(pasta + 'dist_med.npy', dist_med)
		np.save(pasta + 'dist_std.npy', dist_std)

	print("Matriz intrinseca media:")
	print(intr_med)
	print("Matriz intrinseca desvio padrao:")
	print(intr_std)
	print("\n")

	print("Coeficientes de Distorcao medios:")
	print(dist_med)
	print("Coeficientes de Distorcao desvio padrao:")
	print(dist_std)
	print("\n\n\n")

	return intr_med, dist_med

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
		cv2.line(img, p1[last_event].to_tuple(), final_point.to_tuple(), RED, thickness=THICK)
		ponto_texto = (int((p1[last_event].getX()+final_point.getX())/2), int((p1[last_event].getY()+final_point.getY())/2))
		texto = "%.2f" % ((ponto_texto[0])**2+(ponto_texto[1])**2)**(1/2.)
		cv2.putText(img, texto, ponto_texto, FONT, FONT_SIZE, GREEN, 2,cv2.LINE_AA)
		cv2.putText(img, str(p1[last_event].to_tuple()), p1[last_event].to_tuple(), FONT, FONT_SIZE, GREEN, 2,cv2.LINE_AA)
		cv2.putText(img, str(final_point.to_tuple()), final_point.to_tuple(), FONT, FONT_SIZE, GREEN, 2,cv2.LINE_AA)

	return raw, und
	# EVENT_RBUTTONDOWN
	# EVENT_MBUTTONDOWN


# To the frist requisit
draw_line = False					# After that get two points
draw_continuos_line = False			# If there is only one point and you need
									# to draw the line between the frist point
									# and the mouse point at exactly moment
pmouse 	   = [Point(200, 200),\
			  Point(200, 200)]		# To keep the actual mouse point and keep		
									# the 'fila' empty
p1		   = [Point(0, 0), Point(0, 0)]
p2 		   = [Point(0, 0), Point(0, 0)]
filas      = [[], []]
numero_linha = 1
last_event = 1

THICK = 3
FONT = cv2.FONT_HERSHEY_SIMPLEX
RED = (0,0,255)					# Blue Green Red
BLUE = (255,0,0)
GREEN = (0,255,0)
FONT_SIZE = 0.7

# To the second
CAMERA = 0
BOARD_W, BOARD_H = 8, 6
W, H = 1280, 720

pastas = []
#pastas.append("../data/longe/")
#pastas.append("../data/medio/")
#pastas.append("../data/curto/")
pastas.append("../data/img/")

cap = cv2.VideoCapture(CAMERA)	# Open the camera
if not cap.isOpened():
	print("It was not possible to start the camera")
	sys.exit(1)

for pasta in pastas:
	cv2.namedWindow('Undistort Video')
	cv2.setMouseCallback('Undistort Video', lambda event, x, y, flags, param:get_point(event, x, y, flags, param, filas[0]))
	cv2.namedWindow('Raw Video')
	cv2.setMouseCallback('Raw Video', lambda event, x, y, flags, param:get_point(event, x, y, flags, param, filas[1]))

	n_pack, n_img = number_images(pasta)
	if n_pack == 0: # Ou seja, nao tem nenhum pacote
		print("Faltam imagens dentro da pasta " + str(pasta) + "para poder rodar o algoritmo!")
		print("Primeiro rode o algoritmo chamado get_images e coloque as imagens necessarias na pasta de interesse")
		sys.exit(1)
	else:
		print("Medidas para a pasta " + pasta)
		intr_med, dist_med = get_statistics_matrices()
		newcameramtx, roi = cv2.getOptimalNewCameraMatrix(intr_med,dist_med,(W,H),1,(W,H))
		

		w, h = W, H
		while(True):					# The main loop where the raw image and undistorted img are
			ret, frame = cap.read()
			#frame = cv2.resize(frame, (w, h))
			#gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

			#mapx,mapy = cv2.initUndistortRectifyMap(intr_med,dist_med,None,newcameramtx,(w,h),5)
			mapx,mapy = cv2.initUndistortRectifyMap(intr_med,dist_med,None,newcameramtx,(W,H),5)
			undst_img = cv2.remap(frame,mapx,mapy,cv2.INTER_LINEAR)

			# crop the image
			x, y, w,h = roi
			#undst_img = undst_img[y:y+h, x:x+w]
			undst_img = undst_img[0:H, 0:W]
			
			frame, undst_img = atualiza_filas_eventos(frame, undst_img)
			

			cv2.imshow('Raw Video', frame)
			cv2.imshow('Undistort Video',undst_img)

			if cv2.waitKey(1) == 27:
				break
	cv2.destroyAllWindows()

cap.release()



