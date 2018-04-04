def arm_strong(num):
	sum=0
	temp=num
	while temp > 0:
		digit = temp%10
		sum += digit**3
		temp //= 10
	
	if num == sum:
		print("NUMBER IS ARMSTRONG NUMBER\n")
	else:
		print("NOT AN ARMSTRONG numBER")
		
arm_strong(153)
