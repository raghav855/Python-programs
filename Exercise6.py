products = {
                "SMART WATCH": 550,
                "PHONE" : 1000,
                "PLAYSTATION": 500,
                "LAPTOP" : 1550,
                "MUSIC PLAYER" : 600,
                "TABLET" : 400
            }
n=int(input("Enter the number"))
dict1={}
for i in products:
    if products[i]<=n:
        dict1[i]=products[i]
print(dict1)


    


    