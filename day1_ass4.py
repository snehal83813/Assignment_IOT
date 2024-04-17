def find_largest_number(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

a = 10
b = 25
c = 15
largest = find_largest_number(a, b, c)
print("The largest number among", a, ",", b, "and", c, "is", largest)