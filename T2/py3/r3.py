import cv2
import numpy as np
import usefull as use
import sys

lado_quadrado   = 3
unidade         = "cm"

pastas = ["../data/img_longe_120cm/", "../data/img_medio_70cm/", "../data/img_perto_35cm/"]
#pastas = ["../data/img_r2/"]

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
last_event = 1


if __name__ == "__main__":
	get_event1 = lambda event, x, y, flags, param:use.get_event(event, x, y, flags, param, filas[0])
	get_event2 = lambda event, x, y, flags, param:use.get_event(event, x, y, flags, param, filas[1])
	cv2.namedWindow('Undistort Video')
	cv2.setMouseCallback('Undistort Video', get_event1)
	cv2.namedWindow('Raw Video')
	cv2.setMouseCallback('Raw Video', get_event2)
	for pasta in pastas:
		n_pack, n_img = use.number_images(pasta)
		if n_pack == 0: # Ou seja, nao tem nenhum pacote
			print("Faltam imagens dentro da pasta " + str(pasta) + "para poder rodar o algoritmo!")
			print("Primeiro rode o algoritmo chamado get_images e coloque as imagens necessarias na pasta de interesse")
			sys.exit(1)
		else:
			print("Medidas para a pasta " + pasta)
			intr_med, dist_med = use.get_statistics_matrices(pasta, n_pack, n_img, verbose = False) # The intrisic parameters
			rvec, tvec = use.get_extrinsic_parameters(pasta, n_pack, n_img) # The extrinsic parameters

			extrinsic_matrix = np.zeros((3, 4))
			dst, jacobian = cv2.Rodrigues(rvec)
			extrinsic_matrix[:,:3] = dst[:,:]
			extrinsic_matrix[:,3:4] = tvec[:]

			print("Matriz extrinseca:")
			print(extrinsic_matrix)

			


			#print(np.dot(intr_med, extrinsic_matrix))

