import numpy as np

#dimension
d = 2
#columns
M = 7
#rows
N = 6


#create an N x M array described by symbols
#correspond to figures on page 3
# o = 
# + = 
# ^ =
# > =
# | =
# - =

charar = np.chararray((N,M))
charar[:] = 'o'

ret = " " * (N-1) + "\n"

#display graph
for i in range(0,N-1):
	ret += " "
	for j in range(0,M-1):
		ret += charar[i][j]
		ret += " "
	if (i != N-2) :
		ret += "\n"	
	ret += " " * (N-1) + "\n"

print ret



