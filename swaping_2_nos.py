x = input("Enter x\t")
y = input("Enter y\t")

#create an temporary variable
temp = x
x = y
y = temp
 
#now print the no's after swapping.
 
print("X and Y after swapping are {} and {}.".format(x,y))
