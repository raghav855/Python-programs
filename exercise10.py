a=input("Enter the words")
b=a.split(",")
b.sort()

for word in b:
    print(word,end=",")