import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm

#dimension
d = 2
#columns
M = 6
#rows
N = 5


#create an N x M array described by symbols
#correspond to figures on page 3
#the six allowed types, 
#make sure to give each a weight w(o) = ??
#how to work with probabilities
# o = 
# + = 
# ^ =
# > =
# | =
# - =iv

sym_dict = {'o', '+' '^', '>', '|', '-'}

#create matrix of probabilities based on weights
#design matrix so that it can be dynamically adjusted as graph changes


#create an N x M array of symbols.  Initialize all points to nohting.
charar = np.chararray((N,M))
charar[:] = 'o'

def main():
	printarr(charar)
	step(charar)
	printarr(charar)

	Y, X = np.mgrid[-3:3:15j, -3:3:15j]
	U = -1 - np.cos(X**2 + Y)
	V = 1 + X - Y
	speed = np.sqrt(U**2 + V**2)
	UN = U/speed
	VN = V/speed

	plot1 = plt.figure()
	plt.quiver(X, Y, UN, VN, U, cmap = cm.seismic, headlength = 7)

	plt.colorbar()

	plt.title('Invariant Matrices')
	plt.show(plot1)

	#x = np.arange(0, 5, 0.1)
	#y = np.sin(x)
	#plt.plot(x, y)
	#plt.show()

	#T = range(charar.shape[0])
	#for i in range(charar.shape[1]):
	#	plt.plot(T, M[:i])
	#plt.show()

		




#iterates through every value in the array, and updates 
#according to probability distribution
def step(ca):
	for i in range(N):
		for j in range(M):

			#better way to get uniformly random variables?
			#create function transform
			s = np.random.uniform(0,1,1)[0]
			
			if(s < float(1)/6):
				ca[i,j] = '+'
			else:
				ca[i,j] = 'o'

#transform according to weight distribution	
#def transform


#create a graph of objects as seen in paper
#include arrow directions and lines
#can you create graph from symbols?
#def graph


def printarr(ca):
	#print the array with space for arrows
	ret = " " * (N-1) + "\n"

	for i in range(N):
		ret += " "
		for j in range(M):
			ret += ca[i][j]
			ret += " "
		if (i != N-1) :
			ret += "\n"	
		ret += " " * (N) + "\n"

	print ret





#need to take array of symbols and create visualization


if __name__ == '__main__':
	main()