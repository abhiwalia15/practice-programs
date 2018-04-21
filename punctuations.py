#python program to remove punctuations from a string.

#define punctuations
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

my_str = "Hello!!!, he said ---and went."

#make a empty string to add the without punctu. strings
no_pun = ' '

for char in my_str:
	if char not in punctuations:
		no_pun += char
		
# display the unpunctuated string
print(no_pun)
