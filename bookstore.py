author=['aleem','mutt']
book=['peer','murshid']

author_stock={'aleem':5,'mutt':7}
book_stock={'peer':9,'murshid':7}
while True:
 user=input("which book do you want ? ")
 if user in author:  
  if author_stock[user]>0:
    print(f"confirmed purchase for {user}")
    author_stock[user] -= 1
    print(f"Remaining stock for {user}: {author_stock[user]}")
  else:
   print("currently out of stock")
 
 elif user in book:
  if book_stock[user]>0:
   print(f"confirmed {user}")
   book_stock[user] -= 1
   print(f"Remaining stock for '{user}': {book_stock[user]}")
  else:
   print("currently out of stock")
else:
  print("invalid")
