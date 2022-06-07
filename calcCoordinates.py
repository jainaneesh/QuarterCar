import numpy as np 
import math
import matplotlib.pyplot as plt 

x = []
y = []

def circleCoordinate(radius, num):
	circle = np.zeros((2,num))

	thetas = np.linspace(0,360,num)
	for i in range(0,num):
		x.append(radius*np.cos(thetas[i]))
		y.append(radius*np.sin(thetas[i]))
		

circleCoordinate(2,500)
plt.plot(x,y)
plt.grid(True)
plt.show()

