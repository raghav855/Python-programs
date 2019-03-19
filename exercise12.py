a=input("Enter the numbers : ")
b=a.split(",")
lst=[]
for i in b:
    if int(i)%2!=0:
        lst.append(i)
print(lst)



