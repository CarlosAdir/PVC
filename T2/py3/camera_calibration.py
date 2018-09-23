import numpy as np
import cv2
import sys

def there_is(arch):
	try:
		arq = open(arch, "r")
		arq.close()
		return True
	except:
		return False

def is_that_state_realy(estate):
	# Test if there are all images needed to treat the data
	global pasta_img
	global pasta_mat
	global n_iter
	global n_boards

	if estate == 0:
		return 0
	if estate > 0:
		for i in range(1, n_iter+1):
			for j in range(n_boards):
				if not there_is(pasta_img + str(i) + "_" + str(j) + ".png"):
					return 0
	if estate == 1:
		return 1
	else:
		for i in range(1, n_iter+1):
			if not there_is(pasta_mat+"Distortion" + str(i) + ".npy"):
				return 1
			if not there_is(pasta_mat+"Intrinsic" + str(i) + ".npy"):
				return 1
	return 2

def new_calibration(cap):
	global board_w
	global board_h
	global board_total
	global board_sz
	global criteria

	objp = np.zeros((board_total,3), np.float32)
	objp[:,:2] = np.mgrid[0:board_w,0:board_h].T.reshape(-1,2)
	objpoints = [] # 3d point in real world space
	imgpoints = [] # 2d points in image plane.

	successes = 0
	actualframe = 0

	while(successes < n_boards):
		ret, frame = cap.read()
		frame = cv2.resize(frame, (w, h))
		#frame = cv2.resize(frame, (w, h))
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		actualframe += 1
		if(actualframe % frame_step == 0):
			ret, corners = cv2.findChessboardCorners(gray, board_sz,None)
			if ret == True: # If it was possible to find the corners of Chessboard
				cv2.imwrite(pasta_img + str(i) + "_" + str(successes) + '.png', frame)
				objpoints.append(objp)
				#corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
				imgpoints.append(corners)
				img2 = np.copy(frame)
				cv2.drawChessboardCorners(img2, board_sz, corners,ret)
				cv2.imshow('Snapshot', img2)
				successes += 1
				print("Interaction: [" + str(i) + "/" + str(n_iter) + "] - [" + str(successes) + "/" + str(n_boards) + "]")

			else:
				successes = 0
				
				cv2.imshow('Snapshot', gray)
			cv2.imshow('Raw Video', gray)


		if cv2.waitKey(1) & 0xFF == ord('q'):
			cap.release()
			cv2.destroyAllWindows()
			print("The user pressed the 'q' key and the program was finished")
			sys.exit(1)
	cap.release()
	cv2.destroyWindow('Snapshot')
	return objpoints, imgpoints, gray
def old_calibration():
	global board_w
	global board_h
	global board_total
	global board_sz
	global criteria

	objp = np.zeros((board_total,3), np.float32)
	objp[:,:2] = np.mgrid[0:board_w,0:board_h].T.reshape(-1,2)
	objpoints = [] # 3d point in real world space
	imgpoints = [] # 2d points in image plane.

	successes = 0

	while(successes < n_boards):
		gray = cv2.imread(pasta_img + str(i) + "_" + str(successes) + '.png',0) # the 0 number means that the image will load at grayscale
		#frame = cv2.resize(frame, (1200//2, 720//2))
		ret, corners = cv2.findChessboardCorners(gray, board_sz,None)
		if ret == True:
			objpoints.append(objp)
			#corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
			imgpoints.append(corners)
			successes += 1
			print("Interaction: [" + str(i) + "/" + str(n_iter) + "] - [" + str(successes) + "/" + str(n_boards) + "]")

	return objpoints, imgpoints, gray
	
NEW_CALIBRATION = 0
OLD_CALIBRATION = 1
PICK_MATRICES   = 2
CAMERA 			= 1
#CAMERA 		= "/dev/video1"

pasta_img = "../data/img/"
pasta_mat = "../data/mat/"
n_boards = 25
n_iter = 5
frame_step = 1
board_w, board_h = 8, 6
h, w = 720, 1280
#board_w, board_h = 12, 9
#board_w, board_h = 24, 19
if __name__ == "__main__":
	try:
		estate = int(sys.argv[1])
	except:
		estate = PICK_MATRICES
		# print("Digite algum dos numeros:")
		# print("0 - capturar imagens do padrao pela camera")
		# print("1 - para calcular as matrizes a partir de imagens ja salvas")
		# print("2 - para pegar direto as matrizes armazenadas")
		# sys.exit(1)
	estate = is_that_state_realy(estate)

	board_total = board_w * board_h
	board_sz = (board_w, board_h)
	criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 28, 0.001)

	if estate == NEW_CALIBRATION:
		cap = cv2.VideoCapture(CAMERA)
		if not cap.isOpened():
			print("It was not possible to start the camera")
			sys.exit(1)
		else:
			print("opened")
		get_points = lambda : new_calibration(cap)
	elif estate == OLD_CALIBRATION:
		get_points = lambda : old_calibration()

	if estate == NEW_CALIBRATION or estate == OLD_CALIBRATION:
		for i in range(1, n_iter+1): # The algorithm will pick n_inter packages of images to calibrate
			
			# Here we get the points of the corner of n_boards imgs
			print("chegou")
			objpoints, imgpoints, gray = get_points()
			print('\n\nCalibrating the camera now...\n')
			#Calibrate the camera
			ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1],None,None)
			#Save values to file
			np.save(pasta_mat + 'Intrinsic%d' % i, mtx)
			np.save(pasta_mat + 'Distortion%d' % i, dist)
			del objpoints
			del imgpoints
		if estate == NEW_CALIBRATION:
			del cap

	intr_list = []
	dist_list = []
	for i in range(1, n_iter+1):
		intr_list.append(np.load(pasta_mat + 'Intrinsic' + str(i) + '.npy'))
		dist_list.append(np.load(pasta_mat + 'Distortion' + str(i) + '.npy'))
	intr_list = tuple(intr_list)
	dist_list = tuple(dist_list)

	mtx = np.mean(intr_list, axis = 0)
	dist = np.mean(dist_list, axis = 0)
	mtx_std = np.std(intr_list, axis = 0)
	print('shape mtx_std  = ' + str(mtx_std.shape))
	dist_std = np.std(dist_list, axis = 0)
	print('shape dist_std = ' + str(dist_std.shape))

	print('Intrinsic matrix')
	print(mtx)
	print('Distortion matrix')
	print(dist)
	print('Intrinsic_std matrix')
	print(mtx_std)
	print('Distortion_std matrix')
	print(dist_std)

	np.save(pasta_mat + 'Intrinsic.npy', mtx)
	np.save(pasta_mat + 'Distortion.npy', dist)
	np.save(pasta_mat + 'Intrinsic_std.npy', mtx_std)
	np.save(pasta_mat + 'Distortion_std.npy', dist_std)

	print('Starting corrected display....')
	newcameramtx, roi=cv2.getOptimalNewCameraMatrix(mtx,dist,(w,h),1,(w,h))

	print('New Camera Matrix')
	print(newcameramtx)

	cap = cv2.VideoCapture(CAMERA)
	while(True):
	    ret, frame = cap.read()
	    frame = cv2.resize(frame, (w, h))
	    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	    cv2.imshow('Raw Video', gray)

	    # undistort
	    mapx,mapy = cv2.initUndistortRectifyMap(mtx,dist,None,newcameramtx,(w,h),5)
	    undst_img = cv2.remap(gray,mapx,mapy,cv2.INTER_LINEAR)

	    # crop the image
		x,y,w,h = roi
	    undst_img = undst_img[y:y+h, x:x+w]
	    cv2.imshow('Undistort',undst_img)

	    if cv2.waitKey(1) & 0xFF == ord('q'):
	        break

	cap.release()
	cv2.destroyAllWindows()
