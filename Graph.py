import matplotlib.pyplot as plt
import numpy as np
import csv

def getdata(name):
	
	xraw = []
	yraw = []
	
	with open(name, newline='') as raw:
		
		file = csv.reader(raw)
		
		for row in file:
			xraw.append(row[0])
			yraw.append(row[1])
			
	return xraw, yraw

def lobf(xr, yr):
	
	x = np.array(xr)
	y = np.array(yr)
	
	a, b = np.polyfit(x, y, 1)


xd, yd = getdata("descending.csv")
xa, ya = getdata("ascending.csv")

graddesc, interdesc = lobf(xd, yd)
gradasc, interasc = lobf(xa, ya)


plt.scatter(np.array(xd), np.array(yd))
plt.scatter(np.array(xa), np.array(ya))

plt.plot(np.array(xd), graddesc*np.array(xd)+interdesc)
plt.plot(np.array(xa), gradasc*np.array(xa)+interasc)

