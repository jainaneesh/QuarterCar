import matplotlib.pyplot as plt 
from Coordinates import circleCoordinate, rectCoordinate, spring

#Calling the functions to get the initial coordinates of all the shaped
#Coordinates for the circle
xcircle, ycircle = circleCoordinate(2,500, center = (2,2))
#Coordinates for the rectangle

rect1 = rectCoordinate(2,5.5)
rect2 = rectCoordinate(1,2)
#For the y coordinate of the top and bottom mounts of spring
springtopmount = rect1[1][2]
springbottommount = (rect2[1][1] + rect2[1][2])/2
# freelength = springtopmount - springbottommount
"""
For x coordinate of the spring
This x coordinate is a reference for both the top and the bottom mounts
Taking xmid as the average value from the unsprung mass or the rect2 coordinates
"""
xmid = (rect2[0][0] + rect2[0][1])/2
nodes = spring(0,6.5,xmid,0.5,springtopmount,springbottommount)
num = len(nodes[0])
# print(num)

plt.title("Quarter Car Model")
#Plotting tire
plt.plot(xcircle,ycircle,linewidth = 0.2,color ='black')

#Plotting sprung mass
plt.plot([rect1[0][0],rect1[0][1]],[rect1[1][0],rect1[1][1]],'-',linewidth = 2,color = 'black')
plt.plot([rect1[0][1],rect1[0][2]],[rect1[1][1],rect1[1][2]],'-',linewidth = 2,color = 'black')
plt.plot([rect1[0][2],rect1[0][3]],[rect1[1][2],rect1[1][3]],'-',linewidth = 2,color = 'black')
plt.plot([rect1[0][3],rect1[0][0]],[rect1[1][3],rect1[1][0]],'-',linewidth = 2,color = 'black')

#Plotting unsprung mass
plt.plot([rect2[0][0],rect2[0][1]],[rect2[1][0],rect2[1][1]],'-',linewidth = 2,color = 'black')
plt.plot([rect2[0][1],rect2[0][2]],[rect2[1][1],rect2[1][2]],'-',linewidth = 2,color = 'black')
plt.plot([rect2[0][2],rect2[0][3]],[rect2[1][2],rect2[1][3]],'-',linewidth = 2,color = 'black')
plt.plot([rect2[0][3],rect2[0][0]],[rect2[1][3],rect2[1][0]],'-',linewidth = 2,color = 'black')

#Plotting spring
for i in range(1,num-1):
	plt.plot([nodes[0][i-1],nodes[0][i]],[nodes[1][i-1],nodes[1][i]],'-',linewidth = 2,color = 'black')

plt.axis('equal')
plt.show()
