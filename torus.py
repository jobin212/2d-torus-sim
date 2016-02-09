import numpy as np

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



def step(ca):
	for i in range(N):
		for j in range(M):
			s = np.random.uniform(0,1,1)[0]
			print s
			print float(1)/6
			if(s < float(1)/6):
				ca[i][j] = '+'
				print 'hello'
				print ca[i][j]
	printarr(ca)



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