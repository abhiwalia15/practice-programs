n = input('enter any number\n')
n=int(n)
i = 1
count = 0
while i<=n:
	if (n%i == 0):
		count += 1
	i +=1
	
if (count == 2):
	print(str(n)+' is an prime number')
	
else:
	print(str(n)+' is not an prime number')
