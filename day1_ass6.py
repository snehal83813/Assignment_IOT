number = int(input("Enter a non-negative integer: "))
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# function calling
print("Factorial number", number, factorial(number))
