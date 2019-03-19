a=input("Enter the Sentence : ")
count1=0
count2=0
for i in a:
    if i.isdigit()==True:
        count1=count1+1
    elif i.isalpha()==True:
        count2=count2+1
print("Letters " +str(count2))
print("Numbers " +str(count1))
