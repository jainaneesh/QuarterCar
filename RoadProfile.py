import numpy as np 
import math
import matplotlib.pyplot as plt

def roadprofile(idx):
	theta0 = np.zeros((1,400))
	theta1 = np.linspace(270,315,200)
	theta2 = np.linspace(135,45,400)
	theta3 = np.linspace(225,270,200)
	x0 = np.zeros((1,len(theta0)))
	y0 = np.zeros((1,len(theta0)))
	x1 = np.zeros((1,len(theta1)))
	y1 = np.zeros((1,len(theta1)))
	x2 = np.zeros((1,len(theta2)))
	y2 = np.zeros((1,len(theta2)))
	x3 = np.zeros((1,len(theta3)))
	y3 = np.zeros((1,len(theta3)))
	
	# num = len(theta1)
	# print(num)
	# print(type(num))

	for i in range(len(theta1)):
		x1[0][i] = 0.5*np.cos(theta1[i]*math.pi/180)
		y1[0][i] = 0.05 + 0.05*np.sin(theta1[i]*math.pi/180)

	for j in range(len(theta2)):
		x2[0][j] = 1*np.cos(theta2[j]*math.pi/180)
		y2[0][j] = 0.1*np.sin(theta2[j]*math.pi/180)

	for k in range(len(theta3)):
		x3[0][k] = 0.5*np.cos(theta3[k]*math.pi/180)
		y3[0][k] = 0.05 + 0.05*np.sin(theta3[k]*math.pi/180)


	Y = np.hstack((y0,y1,y2,y3))

	return Y[0][idx]

