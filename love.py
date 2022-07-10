name1 = input("Your name: ")
name2 = input("Their name: ")

name1 = name1.strip()
name2 = name2.strip()

l = len(name1) + len(name2)

if l%2 == 0:
  print("love")
else:
  print("uhuh")
  
