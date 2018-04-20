#python program to find the sum of n natural numbers using recursion funciton

def recur_sum(n):
	'''recursive function to find sum of n-numbers'''
	if n<=1:
		return 1
	else:
		return n+recur_sum(n-1)
		
num = int(input("ENTER ANY NUMBER\n"))
 
if num < 0:
	print("ENTER ANY POSITIVE NUMBER")

else:
	print("THE SUM IS",recur_sum(num)) 
