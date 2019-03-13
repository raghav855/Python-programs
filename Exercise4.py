gadgets = ["Python", "Java", 100, "Php", 310.28, "C#", 27.00,"Asp", 1000, "R", "Django"]
list1=[]
list2=[]
for i in gadgets:
    if type(i)==str:
        list1.append(i)
    elif type(i)==int or type(i)==float:
        list2.append(i)
print(list1)                                 #separate lists of strings.
print(list2)                                 #separate lists of numbers.
print(sorted(list1))                         #Sort the strings list in ascending order         
print(sorted(list1,reverse=True))            #Sort the strings list in descending order
print(sorted(list2))                         #Sort the number list from lowest to highest
print(sorted(list2,reverse=True))            #Sort the number list from highest to lowest