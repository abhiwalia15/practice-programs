#python program to find if a string is palindrone or not.

my_str = input("ENTER ANY STRING:\t")

#make the string caseless for suitable comparison.
#it can be upper or lower case.
my_str = my_str.casefold()

#revese the string.
rev_str = reversed(my_str)

#store them in a list for comparison purpose.
if list(my_str) == list(rev_str):
	print("PALINDRONE STRING")
else:
	print("NOT A PALINDRONE STRING")
