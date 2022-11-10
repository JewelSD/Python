a=str(input("Enter the word"))
m=[]
for x in a:
    if x in ("a","e","i","o","u"):
      m.append(x)
print(list(set(m)))
