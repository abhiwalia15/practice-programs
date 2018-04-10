#python program to find the LCM of a number

def lcm(a,b):
	pro = a*b
	for i in range(1,pro,1):
		if((a%i==0)and(b%i==0)):
			hcf = i
		lcm = pro//hcf
	print("HCF = "+str(hcf))
	print("LCM = "+str(lcm))

lcm(12,5)

