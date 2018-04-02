import math

def quadratic(a,b,c):
	
	d = (b**b)-(4*a*c)
	s1 = (-b-math.sqrt(d))/(2*a)
	s2 = (-b+math.sqrt(d))/(2*a)	
	print('The solution are {0} and {1}'.format(s1,s2))

ans=quadratic(2,4,6)

