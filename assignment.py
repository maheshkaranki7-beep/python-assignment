# Python Programming Assignment
# Name: Karanki Mahesh


# --------------------------------------------------
# Question 1
# Find all numbers between 2000 and 3200 which are
# divisible by 7 but are not multiples of 3.
# --------------------------------------------------

numbers = []

for i in range(2000, 3201):
    if i % 7 == 0 and i % 3 != 0:
        numbers.append(str(i))

print("Question 1 Output:")
print(",".join(numbers))


# --------------------------------------------------
# Question 2
# Given a list of characters, convert it into a string.
# Input is given by the user.
# --------------------------------------------------

characters = input("\nEnter characters separated by spaces: ").split()

result = "".join(characters)

print("Question 2 Output:")
print(result)


# --------------------------------------------------
# Question 3
# Generate a dictionary containing (i, i*i).
# Input n is given by the user.
# --------------------------------------------------

n = int(input("\nEnter a number: "))

result = {}

for i in range(1, n + 1):
    result[i] = i * i

print("Question 3 Output:")
print(result)
