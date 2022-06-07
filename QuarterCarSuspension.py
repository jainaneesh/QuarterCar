import numpy as np 
# from scipy import odeint
import math
import matplotlib.pyplot as plt 
from RoadProfile import roadprofile

def xr(   ):

	xr = roadprofile(idx)
	return xr
	

def G(A,B,qmatrix,t,idx):   
	return A.dot(qmatrix) + B*xr(idx)

def RK4(A,B,qmatrix,t,dt,idx):
	k1 = G(A,B,qmatrix,t,idx)	
	k2 = G(A,B,qmatrix+0.5*k1*dt,t+0.5*dt,idx)
	k3 = G(A,B,qmatrix+0.5*k2*dt,t+0.5*dt,idx)
	k4 = G(A,B,qmatrix+k3*dt,t+dt,idx)
	return dt*(k1+2*k2+2*k3+k4)/6


"""
# Acronyms for the vehicle parameters
ks      :     spring_stiffness
cs      :     damping
ms      :     sprung mass
kt      :     tire rate/tire stiffness
mus     :     unsprung mass   
dt      :     delta time or time step
"""

#Defining the parameters
ks    =    28000
cs    =    16000
ms    =    405
kt    =    250000
mus   =    90
q1    =    0      #sprung mass vertical position
q2    =    0      #sprung mass vertical velocity
q3    =    0      #unsprung mass vertical position
q4    =    0      #unsprung mass vertical velocity

starttime = 0
endtime = 6
num   =    801
dt    =    (endtime-starttime)/num
# time  =    np.arange(0,5,dt) 
time  =    np.linspace(starttime,endtime,num) 

A = np.array([[0, 1, 0, 0],[-ks/ms, -cs/ms, ks/ms, cs/ms],[0, 0, 0, 1],[ks/mus, cs/mus, -(ks+kt)/mus, -cs/mus]])
qmatrix = np.array([[q1], [q2], [q3], [q4]])
B = np.array([[0], [0], [0], [kt/mus]])
   

Qmatrix1 = []
Qmatrix2 = []

for idx,t in enumerate(time):
	# print(idx)
	qmatrix = qmatrix + RK4(A,B,qmatrix,t,dt,idx)
	Qmatrix1.append(0.5 + qmatrix[0])
	Qmatrix2.append(0.3 + qmatrix[2])
	# print(Qmatrix)


plt.plot(time,Qmatrix1)
plt.plot(time,Qmatrix2)
plt.grid(True)
plt.xlabel("Time [s]")
plt.ylabel("Displacement [m]")
plt.legend(["Sprung mass","Unsprung mass"],loc='lower right')
plt.show()