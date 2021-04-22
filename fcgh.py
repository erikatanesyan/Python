# write a function that computes the volume of a sphere given its radius
pi = 3.14
radius = 1
volume = (4/3)*pi*(radius**3)
print("The Volume of the sphere is:", volume)

# Write a function that checks whether a passed string is palindrome or not
def palindrome(x):
    return x == x[::-1]
x = input ("Enter a string:")
y = palindrome(x)
if y:
    print("String is Palindrome")
else:
    print("String is not Palindrome")



