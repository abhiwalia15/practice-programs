#python program to display fibonacci series upto n-th term using recursive function

def recur_fibo(n):
	'''Recursive function to find fibonacci series'''
	if n<=1:
		return 1
		
	else:
		return (recur_fibo(n-1)+recur_fibo(n-2))
		
nterm = int(input("ENTER N-TH TERM\n"))

if nterm<=0:
	print("ENTER A POSITIVE NUMBER")

else:
	print("FIBONACCI SERIES")
	for i in range (nterm):
		print(recur_fibo(i))
	
