print(" To Find Leap Year")
start=int(input("Enter the starting year:"))
end=int(input("Enter the ending year:"))
print("List of Leap year:")
for year in range(start,end+1):
    if(0==year%4)and(year%100!=0)or(0==year%400):
        print(year)
        
