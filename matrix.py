X = [[1,2,3],
     [4,5,6],
     [7,8,9]]
     
Y = [[9,8,7],
     [6,5,4],
     [3,2,1]]
     
result = [[0,0,0],
          [0,0,0],
          [0,0,0]]

'''print(len(X))=3
print(len(X[0]))=3'''

#iterate through rows.          
for i in range(len(X)):
	
	#iterate through columns.
	for j in range(len(X[0])):
		
		#add two matrices and store them in result.
		result[i][j] = X[i][j]+Y[i][j]
		
for r in result:
	print(r)

