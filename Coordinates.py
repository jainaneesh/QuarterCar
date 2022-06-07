import numpy as np 
import math
import matplotlib.pyplot as plt 

xcircle = []
ycircle = []


def circleCoordinate(radius, num, center= (0,0)):	

	thetas = np.linspace(0,360,num)
	for i in range(0,num):
		xcircle.append(center[0]+radius*np.cos(thetas[i]))
		ycircle.append(center[1]+radius*np.sin(thetas[i]))

	return xcircle, ycircle		


def rectCoordinate(height,hcog):
	rect = np.zeros((2,4))

	x1 = min(xcircle) - 0.5
	y1 = hcog + height/2

	x2 = max(xcircle) + 0.5
	y2 = hcog + height/2

	x3 = max(xcircle) + 0.5
	y3 = hcog - height/2

	x4 = min(xcircle) - 0.5
	y4 = hcog - height/2

	rect[0] = [x1,x2,x3,x4]
	rect[1] = [y1,y2,y3,y4]

	# print(rect)
	return rect

def spring(deflection,numofturns,xmid,L,springtopmount,springbottommount):

	wholeturns = math.floor(numofturns)
	# print(wholeturns)
	nodes = np.zeros((2,2*wholeturns+4))
	freelength = springtopmount - springbottommount
	pitch = (freelength - deflection)/numofturns
	halfpitch = (pitch)/2
	theta = math.asin((halfpitch/2)/(L/2))
	springright = (L/2)*math.cos(theta)
	springrightside = xmid + springright
	springleftside = xmid - springright 
	#Doing the remaining operations for the spring
	#Base nodes
	xbasenode1 = springrightside
	ybasenode1 = springbottommount
	xbasenode2 = springleftside
	ybasenode2 = springbottommount
	nodes[0][0] = xbasenode1
	nodes[1][0] = ybasenode1
	nodes[0][1] = xbasenode2
	nodes[1][1] = ybasenode2
	#For the bottom or first half turn of the spring coil
	xnode1 = springrightside
	nodes[0][2] = xnode1
	ynode1 = springbottommount + halfpitch 
	nodes[1][2] = ynode1
	#Calculations for the remaining full turns of the spring
	for i in range(3,2*wholeturns+4):
		#default value of numofturns is 4.5 and hence wholeturns would be 4
		j = 0
		if (i%2!=0):
		 	nodes[j][i] = springleftside
		 	nodes[j+1][i] = nodes[j+1][i-1] + pitch/2
		else:
		 	nodes[j][i] = springrightside
		 	nodes[j+1][i] = nodes[j+1][i-1] + pitch/2


	return nodes

