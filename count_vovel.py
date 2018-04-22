#python program to count each of vowels.

my_str = input("ENTER ANY STRING")

#split the string into list
words = my_str.split()

#input the vowels and make is suitable for caseless comparison.
vowels = ['a','e','i','o','u']
vowel = vowels.casefold()

for word in words:
	if vowel in word:
		print(len(vowel))
