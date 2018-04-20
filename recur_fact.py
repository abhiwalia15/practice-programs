#python program to find the factorial of a number by using recursive function.

def recur_fact(n):
	'''recursive program to find the factorial.'''
	if n==1:
		return 1

	else:
		return (n*recur_fact(n-1))
		
num = int(input("ENTER ANY NUMBER"))

if num<0:
	print("ENTER A POSITIVE NUMBER")

elif num==0:
	print("THE FACTORIAL OF ) IS 1")
	
else:
	print("FACTORIAL of",num,"is ",recur_fact(num))
