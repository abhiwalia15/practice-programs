#python program to convert decimal function to binary function using recursion function.

def ConvertToBinary(n):
	'''Recursive function to convert decimal to binary'''
	if n>1:
		ConvertToBinary(n//2)
	print(n%2,end ='')
	
#decimal number
dec = int(input("ENTER ANY NUMBER"))

ConvertToBinary(dec)
