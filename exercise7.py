# Write a Python program to accept a filename from the user and print
# the extension of that.
# Sample filename : abc.java
# Output : java

filename = input("Enter file name: ")
parts = filename.rsplit(".", 1)
print("Extension:" + parts[-1])

index = filename.rfind(".") + 1
print("Extension:" + filename[index:])
