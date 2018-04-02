def area_of_triangle():	
	
	a=int(input("a\t"))
	b=int(input("b\t"))
	c=int(input("c\t"))
	
	s = (a+b+c)/2

	area = (s*(s-a)*(s-b)*(s-c))**0.5

	return area
	
ans=area_of_triangle()
print(ans)

#less time solution.
'''def area_of_triangle(a,b,c):	
	
	s = (a+b+c)/2

	area = (s*(s-a)*(s-b)*(s-c))**0.5

	return area
	
ans=area_of_triangle(3,2,4)
print(ans)'''
