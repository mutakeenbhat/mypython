from collections import Counter
def is_vowel(x):
    if x.lower() in 'aeiou':
        print("character is a vowel")
    else:
        print("character is a consonant")
user=input("enter an alphabet ")
is_vowel(user)
