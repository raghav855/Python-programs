def div(a):
    if(a%3==0 and a%5==0):
        return "Fizz Buzz"
    elif(a%3==0):
        return "Fizz"
    elif (a%5==0):
        return "Buzz"
a=int(input("Enter the number:- "))
print(div(a))
