num = input("Enter any number\n");
found = 0

for n in num:
	n = int(n) 
	print(n)
	
key = input("enter the key value \n")
key = int(key)
	
for i in range (n,1):
	
	if (n==key):
		found += 1
		break
	
if (found==1):
	print(int(key) + ' is found.')
		
else:
	print('key not found')
	
