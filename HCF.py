#python program to find the hcf or greatest common divisor(GCD) of a number

def hcf(a,b):
	pro = a*b
	for i in range(1,pro,1):
		if((a%i==0)and(b%i==0)):
			hcf = i
	print("HCF = "+str(hcf))

hcf(21,49)
