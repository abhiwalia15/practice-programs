#python program to count number of vowels in a string.

#string of vowels
vowels = 'aeiou'

#let user input any string.
my_str = input("ENTER ANY STRING\n")

#make it suitable for case les comparison.
my_str = my_str.casefold()

vow = 0 

for my_strs in my_str:
	for vowel in vowels:
		if vowel in my_strs:
			vow += 1
			
print(vow)

