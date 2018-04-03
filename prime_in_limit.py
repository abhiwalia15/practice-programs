#set the lower limit
lower = 500
#set the higher limit
upper = 550

print("Prime numbers between",lower,"and",upper,"are:")

def prime():
	 
	for num in range(lower,upper + 1):
		
		for i in range(2,num):
			
			if (num % i) == 0:
				print(num)
prime()
'''



   # prime numbers are greater than 1
   if num > 1:
       
           
       else:
           print(num)
'''
