# Accept a 4-digit number from the user
number = int(input("Enter a 4-digit number: "))

# Display face value of each decimal digit
print("a. Face value of each decimal digit:")
for digit in str(number):
    print(digit, end=" ")

# Display place value of each decimal digit
print("\nb. Place value of each decimal digit:")
place_value = 1000
while place_value >= 1:
    digit = number // place_value
    print(digit, "*", place_value, end=" + " if place_value != 1 else " = ", )
    number %= place_value
    place_value //= 10

# Display number in reverse order by changing decimal place values
print("\nc. Number in reverse order by changing decimal place values:")
reversed_number = 0
for i in range(4):
    digit = number % 10
    reversed_number += digit * (10 ** (3 - i))
    number //= 10

print(reversed_number)
