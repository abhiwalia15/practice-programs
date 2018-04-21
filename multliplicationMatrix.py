'''python program to perform matrix multliplication using nested lists.
if X[n*m] and Y[m*l] == result[n*l]'''

X = [[1,2,3],
     [4,5,6],
     [7,8,9]]
     
Y = [[9,8,7,3],
     [6,5,4,1],
     [3,2,1,3]]
     
result = [[0,0,0,0],
          [0,0,0,0],
          [0,0,0,0]]
          
#iterate through rows of X.          
for i in range(len(X)):
	#iterate through columns of Y.
	for j in range(len(Y[0])):
		#iterate through rows of y.
		for k in range(len(Y)):
			result[i][j] += X[i][k]*Y[k][j]
			
for r in result:
	print(r)
