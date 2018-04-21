#python program to sort the string alphabetically.

my_str = input("ENTER ANY STRING\n")
#make it suitable for case less comparison.
my_str = my_str.casefold()

#breakdown the string into a list of strings
#string() method splits the string at whitespaces and store them into a list.
words = my_str.split()

#sort the lsit.
words.sort()

#display the sorted list.
print("THE SORTED LIST IS:\n")
for word in words:
	print(word)
