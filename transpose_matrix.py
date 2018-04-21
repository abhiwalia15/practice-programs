#python program to find the transpose of a matrix using the nested lists.

X = [[1,2,3],
     [4,5,6],
     [7,8,9]]
     
transpose = [[0,0,0],
             [0,0,0],
             [0,0,0]]

     
#iterate through rows.
for i in range(len(X)):
	#iterate through columns:
	for j in range(len(X[0])):
		transpose[i][j] = X[j][i]

for t in transpose:
	print(t)
