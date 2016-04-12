import numpy as np
import matplotlib.pyplot as plt
#dimension
d = 2
#columns
M = 3
#rows
N = 2


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
charar[:] = '.'

def main():
	print(charar)
	figure6(charar)
	print(charar)

	
	soa =np.array( [ [1,0,1,-1], [1,1,1,0],[0,0,1,3]]) 
	X,Y,U,V = zip(*soa)
	plt.figure()
	ax = plt.gca()
	ax.quiver(X,Y,U,V,angles='xy',scale_units='xy',scale=1)
	ax.set_xlim([0,M])
	ax.set_ylim([0,N])
	plt.draw()
	plt.show()
		


def figure6(ca):
	ca[1, 0] = '>'
	ca[1,1] = '^'
	ca[1,2] = '>'
	ca[0,2] = '^'


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