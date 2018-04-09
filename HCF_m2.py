# Python program to find the H.C.F of two input number

# define a function
def hcf(a,b):
	if(a>b):
		small = b
	else:
		small = a
	while(small!=0):
		hcf = small
		small = big%small
		
	print("HCF = "+str(hcf))
	
hcf(69,122)
