#python program to find the factors of a number.

def factors(n):
	print("THE FACTORS OF {} ARE -".format(str(n)))
	for i in range(1,n+1):
		if(n%i==0):
			print(i)
		
factors(511)
