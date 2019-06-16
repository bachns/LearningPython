# Write a Python program to count the number 4 in a given list.

# Enter sequence of comma-separated numbers:
numbers = input("Enter sequence of comma-separated numbers: ")
numlist = numbers.split(",")
count = 0
for num in numlist:
    if int(num) == 4:
        count = count + 1

print("Number of number 4: " + str(count))
