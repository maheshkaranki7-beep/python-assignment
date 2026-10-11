# Python Assignment
# Name: Karanki Mahesh

# --------------------------------------------------
# Program 1:
# Find numbers between 2000 and 3200 which are
# divisible by 7 but are not multiples of 3.
# --------------------------------------------------

numbers = []

for i in range(2000, 3201):
    if i % 7 == 0 and i % 3 != 0:
        numbers.append(str(i))

print("1. Numbers divisible by 7 but not by 3:")
print(",".join(numbers))


# --------------------------------------------------
# Program 2:
# Convert a list of characters into a string.
# --------------------------------------------------

characters = ["C", "o", "d", "i", "n", "g"]

result = "".join(characters)

print("\n2. Converted string:")
print(result)


# --------------------------------------------------
# Program 3:
# Generate a dictionary containing (i, i*i)
# for numbers from 1 to n.
# --------------------------------------------------

n = int(input("\n3. Enter a number: "))

square_dictionary = {}

for i in range(1, n + 1):
    square_dictionary[i] = i * i

print("Dictionary:")
print(square_dictionary)
