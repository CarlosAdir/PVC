#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np

#############
# CONSTANTS #
#############

# Drawing
THICK = 3
FONT = cv2.FONT_HERSHEY_SIMPLEX
RED = (0,0,255)                 # Blue Green Red
BLUE = (255,0,0)
GREEN = (0,255,0)
FONT_SIZE = 0.7

# Calibrate
CAMERA = 0
BOARD_W, BOARD_H = 8, 6
W, H = 1280, 720


######################
# The user interface #
######################

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
        

def get_event(event, x, y, flags, param, fila): #funcao de callback do mouse
	fila.append(MouseEvent(x, y, event))
        
def there_is(arch):
	try:
		arq = open(arch, "r")
		arq.close()
		return True
	except:
		return False

####################################
# To the 2nd, 3nd and 4nd requisit #
####################################

def number_images(pasta):
    n_pack, n_img = 0, []
    n_img_min = 0
    i = 1
    while i < 10:
        j = 1
        if not there_is(pasta+str(i) + "_" + str(j) + ".png"):
            n_pack = i-1
            break
        while j < 50:
            if not there_is(pasta+str(i) + "_" + str(j) + ".png"):
                n_img.append(j-1)
                break
            j += 1
        i += 1
    if len(n_img) == 0:
        return 0, 0
    n_img_min = min(n_img)
    if n_img_min == 0:
        n_pack = 0
    return n_pack, n_img_min

def get_points(pack, pasta, n_pack, n_img):
    '''
    This function gets all the points from on specific package, which we called pack
    '''
    global BOARD_W
    global BOARD_H
    
    #global criteria

    BOARD_TOTAL = BOARD_W * BOARD_H
    BOARD_SZ = (BOARD_W, BOARD_H)

    objp = np.zeros((BOARD_TOTAL,3), np.float32)
    objp[:,:2] = np.mgrid[0:BOARD_W,0:BOARD_H].T.reshape(-1,2)
    objpoints = [] # 3d point in real world space
    imgpoints = [] # 2d points in image plane.

    successes = 1

    while(successes <= n_img):
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
                #print("Interaction: [" + str(pack) + "/" + str(n_pack) + "] - [" + str(successes) + "/" + str(n_img) + "]")
                successes += 1

    return objpoints, imgpoints, gray

def get_matrices(pasta, n_pack, n_img):
    intr_list = []
    dist_list = []
    for pack in range(1, n_pack+1):
        if there_is(pasta + "intr_%d.npy" % pack) and there_is(pasta + "dist_%d.npy" % pack):
            intr = np.load(pasta + "intr_%d.npy" % pack)
            dist = np.load(pasta + "dist_%d.npy" % pack)
        else:
            objpoints, imgpoints, gray = get_points(pack, pasta, n_pack, n_img)
            print('Calibrating the camera now...')
            ret, intr, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1],None,None)
            #print('rvecs = ' + str(rvecs))
            #print('tvecs = ' + str(tvecs))
            #Save values to file
            np.save(pasta + 'intr_%d' % pack, intr)
            np.save(pasta + 'dist_%d' % pack, dist)
            del objpoints
            del imgpoints
        intr_list.append(intr)
        dist_list.append(dist)
    return tuple(intr_list), tuple(dist_list)

def get_extrinsic_parameters(pasta, n_pack, n_img, verbose = True):

    '''
    global BOARD_W
    global BOARD_H
    pack = 1
    
    #global criteria

    BOARD_TOTAL = BOARD_W * BOARD_H
    BOARD_SZ = (BOARD_W, BOARD_H)

    objp = np.zeros((BOARD_TOTAL,3), np.float32)
    objp[:,:2] = np.mgrid[0:BOARD_W,0:BOARD_H].T.reshape(-1,2)
    objpoints = [] # 3d point in real world space
    imgpoints = [] # 2d points in image plane.


    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

    pasta = "../data/img_r2/"
    n_pack, n_img = number_images(pasta)
    mtx, dist = get_statistics_matrices(pasta, n_pack, n_img, verbose = False)
    axis = np.float32([[3,0,0], [0,3,0], [0,0,-3]]).reshape(-1,3)

    successes = 1
    while(successes <= n_img):
        if not there_is(pasta + str(pack) + "_" + str(successes) + '.png'):
            print("Hey! There is no file called '" + pasta+str(pack)+"_"+str(successes)+'.png' + "'")
        else:
            gray = cv2.imread(pasta + str(pack) + "_" + str(successes) + '.png',0) # the 0 number means that the image will load at grayscale
            #frame = cv2.resize(frame, (1200//2, 720//2))
            ret, corners = cv2.findChessboardCorners(gray, BOARD_SZ,None)
            if ret == True:
                corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
                ret,rvecs, tvecs = cv2.solvePnP(objp, corners2, mtx, dist)
                imgpts, jac = cv2.projectPoints(axis, rvecs, tvecs, mtx, dist)
                successes += 1

    return rvecs, tvecs
    '''

    
    if not there_is(pasta + "rvecs.npy") and not there_is(pasta + "tvecs.npy"):
        objpoints, imgpoints, gray = get_points(1, pasta, n_pack, n_img)
        ret, intr, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1],None,None)
        np.save(pasta + "rvecs.npy", rvecs)
        np.save(pasta + "tvecs.npy", tvecs)
    else:
        rvecs = np.load(pasta + "rvecs.npy")
        tvecs = np.load(pasta + "tvecs.npy")
    rvec = np.mean(rvecs, axis = 0) 
    tvec = np.mean(tvecs, axis = 0)
    rvec_std = np.std(rvecs, axis = 0) 
    tvec_std = np.std(tvecs, axis = 0)
    if verbose == True:
        print("Rotation vector mean:")
        print(rvec)
        print("Rotation vector std:")
        print(rvec_std)
        print("Translation vector mean:")
        print(tvec)
        print("Translation vector std:")
        print(tvec_std)
    return rvec, tvec
    


def get_statistics_matrices(pasta, n_pack, n_img, verbose = True):
    intr_list, dist_list = get_matrices(pasta, n_pack, n_img)
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

    if verbose == True:
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