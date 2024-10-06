
def count_vowels(s):
   count=0
   for char in s.lower():
    if char in 'aeiou':
      count+=1
   return count
user=input("enter an string ")
print(f"Number of vowels: {count_vowels(user)}")