l=int(input("Enter the limit:"))
a=[]
for i in range(l):
    a.append(int(input(str(i ) + "position:")))
print(a)
print("The positive set of elements in above  list:")
b=[]
for i in a:
    if i>=0:
     b.append(i)
print(b)
    
