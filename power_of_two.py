#Python Program to display the powers of 2 using anonymous function
def pow(n):
	
	for i in range (0,11,1):
		result = n ** i
		print("{} raised to the power {} is {}".format(n,i,result))
			
pow(2)
