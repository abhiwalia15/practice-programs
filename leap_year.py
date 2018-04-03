def leap_year(year):
	if (year%4==0) and (year%100==0) and (year%400==0):
		print(str(year)+' is a leap year.')
	else:
		print("NOT A LEAP YEAR.")
	
leap_year(1900)
