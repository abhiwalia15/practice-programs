# Python Program to find numbers divisible by thirteen from a list using anonymous function

# Take a list of numbers
my_list = [12, 65, 54, 39, 102, 339, 221,13]

def num_divisible_by_num(n):
	
	for i in my_list:
		if (i%n == 0):
			print(i)
		
num_divisible_by_num(13)
