#set the lower and upper limit.
upper = 20000
lower = 100

def armstrong():
	for num in range(lower,upper+1):
		
		#order of number
		order = len(str(num))
		
		#initiliaxe sum
		sum=0
		temp=num
		
		#find the usm of cube of each digit.
		while temp>0:
			digit = temp%10
			sum += digit**order
			temp //= 10
			
		if num == sum:
			print(num)
			
armstrong()
