# Exercicio do tutorial
# https://docs.opencv.org/trunk/dc/da5/tutorial_py_drawing_functions.html

import numpy as np
import cv2 as cv
# Create a black image
width = 1024
heigh = 512
img = np.zeros((heigh,width,3), np.uint8)
# Draw a diagonal blue line with thickness of 5 px


class point:
	"""docstring for point"""
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __add__(self, outro_ponto):
		return point(self.x+outro_ponto.x, self.y+outro_ponto.y)

	def __sub__(self, outro_ponto):
		return point(self.x-outro_ponto.x, self.y-outro_ponto.y)

	def to_list(self):
		return (self.x, self.y)
		

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
	else:
		return (128, 128, 128)


lado 		 = 200
center_green = point(100, 400)
raio_externo = 80
raio_interno = 40

center_blue = point(lado, 0)
center_blue = center_blue + center_green

center_red = point(int(lado/2.), -int(lado*np.sqrt(3)/2))
center_red = center_green + center_red


# Para limpar a tela
top_left_ver = (0, 0)
bot_righ_ver = (width-1, heigh-1) 
color = get_color('white')
thickness = -1
cv.rectangle(img, top_left_ver, bot_righ_ver, color, thickness)


major = raio_externo
minor = raio_externo
radius = raio_interno
axes_len = (major, minor)
thickness = -1  
initial_angle = 0
final_angle = 300


# Montando o logo

rotation_elipse = 0
center = center_green.to_list()
color = get_color('green')
cv.ellipse(img, center, axes_len, rotation_elipse, initial_angle, final_angle, color, thickness)

rotation_elipse = -60
center = center_blue.to_list()
color = get_color('blue')
cv.ellipse(img, center, axes_len, rotation_elipse, initial_angle, final_angle, color, thickness)

rotation_elipse = 120
center = center_red.to_list()
color = get_color('red')
cv.ellipse(img, center, axes_len, rotation_elipse, initial_angle, final_angle, color, thickness)

color = get_color('white')

center = center_green.to_list()
cv.circle(img, center, radius, color, thickness)

center = center_blue.to_list()
cv.circle(img, center, radius, color, thickness)

center = center_red.to_list()
cv.circle(img, center, radius, color, thickness)


# Montando o texto

# Um texto na tela
font = cv.FONT_HERSHEY_SIMPLEX
color = get_color('black')

text = 'OpenCV'
bottom_left_text = (400, int(2*heigh/5))
size = 5
thickness = 3
cv.putText(img, text, bottom_left_text, font, size, color, thickness, cv.LINE_AA)

size = 2
thickness = 2

text = 'Open Source'
bottom_left_text = (420, int(7*heigh/10))
cv.putText(img, text, bottom_left_text, font, size, color, thickness, cv.LINE_AA)
text = 'Computer Vision'
bottom_left_text = (420, int(9*heigh/10))
cv.putText(img, text, bottom_left_text, font, size, color, thickness, cv.LINE_AA)



cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()