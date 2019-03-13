n=int(input("How many numbers want to enter "))
lst=[]
for i in range(n):
    x=int(input())
    lst.append(x)
a=(sorted(lst,reverse=True)) 
print(a[0],a[1])

