num=int(input("Enter the number"))
if num<2:
    print('Not a prime')
else:    
    for i in range(2,num//2):
        if(num%i==0):
            print('Number is not prime')
            break
    else:
        print('Number is prime')

