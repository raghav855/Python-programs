num=input("Enter the input : ")
rev_str=''
a=num.lower()
for i in a:
    rev_str=i+rev_str
if rev_str==a:
    print(num + ' is Palindrome')
else:
    print(num +' is not Palindrome')

