def fac(a):
    l=[]
    for i in range(1,a+1):
        if a % i ==0:
            l.append(i)
    print(l)

def sun(a):
    s=0
    for i in range(1,a+1):
        s=s+i
    return (s*2)


n=int(input("Enter the number:"))
ch=int(input("Enter '0' for factors and '1' for sumof n numbers*2:"))
if ch==0:
  fac(n)
elif ch==1:
    print(sun(n))
else:
    print("Wrong choice")
