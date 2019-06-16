# Write a Python program to test whether a passed letter is a vowel or not.


def isVowel(v):
    vowels = ("u", "e", "o", "a", "i")
    return v in vowels


vowel = input("Enter a letter: ")
if isVowel(vowel):
    print("This is a vowel")
else:
    print("This isn't a vowel")
