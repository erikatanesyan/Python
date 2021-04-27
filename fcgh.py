# Write a function that will return the factorial of a given number
def factorial(number):
    sum = 2
    if 0 <= number <= 2:
        sum = number
    else:
        for x in range(2, number, 1):
            sum = sum * (x+1)
    return sum
print(factorial(3))

# Write a function that will return the count of given character in the given string
def char_num(string_1, char_1):
    count = 0
    for character in string_1:
        if character == char_1:
            count += 1
    return count
print(char_num("barev dez gegeckuhi", "b"))

# Write a function that will return count of characters till the given one
def a(string_2, char_2):
    count = 0
    for b in string_2:
        if b != char_2:
            count += 1
        else:
            break
        return count
print(a("ahbbbasdf", "b"))