# Do tutorial
# https://docs.opencv.org/trunk/dc/da5/tutorial_py_drawing_functions.html

import numpy as np
import cv2 as cv
# Create a black image
img = np.zeros((512,512,3), np.uint8)
# Draw a diagonal blue line with thickness of 5 px

def get_color(string):
	if string == 'red':
		return (0, 0, 255)
	elif string == 'blue':
		return (255, 0, 0)
	elif string == 'green':
		return (0, 255, 0)
	elif string == 'yellow':
		return (0, 255, 255)
	elif string == 'purple':
		return (255, 0, 255)
	elif string == 'anil':
		return (255, 255, 0)
	elif string == 'black':
		return (0, 0, 0)
	elif string == 'white':
		return (255, 255, 255)


# Desenhando uma reta
initial_point = (0, 0)
final_point = (511,511)
color = get_color('blue')
thickness = 5
cv.line(img,initial_point, final_point, color, thickness)


# Desenhando um retangulo
top_left_ver = (384, 0)
bot_righ_ver = (510, 128) 
color = get_color('green')
thickness = 3
cv.rectangle(img, top_left_ver, bot_righ_ver, color, thickness)


# Desenhando um circulo vermelho
color = get_color('red')
radius = 63
center = (447, 63)
thickness = -1 	# Se for -1, o circulo sera totalmente preenchido
				# Se for 0, será a mesma coisa que 1
				# Se for n, inteiro positivo, será a espessura em pixeis
cv.circle(img, center, radius, color, thickness)




# Desenhando uma elipse
center = (256, 256)
major = 100
minor = 50
axes_len = (major, minor)
rotation_elipse = 0
initial_angle = 0
final_angle = 180
thickness = -1	# O mesmo que para o circulo vermelho  
color = get_color('yellow')
cv.ellipse(img, center, axes_len, rotation_elipse, initial_angle, final_angle, color, thickness)







# Desenhando um poligono
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2)) # Se em vez de -1 for 4, ele faz a mesma coisa. Suponho que seja a mesma coisa de fazer array[-1]
color = get_color('purple')
close_polygon = True # É a mesma coisa que deixar o poligono fechado, colocar o ultimo ponto como o primeiro
cv.polylines(img,[pts], close_polygon, color)


# Um texto na tela
font = cv.FONT_HERSHEY_SIMPLEX
text = 'OpenCV Learning'
color = get_color('white')
bottom_left_text = (10, 500)
size = 1
thickness = 1
cv.putText(img, text, bottom_left_text, font, size, color, thickness, cv.LINE_AA)



cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()