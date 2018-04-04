def fibonacci(n):
	#set the first two ters of the series to 0 and 1 and print them.
	a=0
	b=1
	print(str(a)+'\n'+str(b))
	
	for c in range(3,n+1):
		#the third sum will be the sum of the last two terms and then print it.
		c=a+b
		print(c)
		
		#now swap the two terms.
		a=b
		b=c
		
fibonacci(10000)
