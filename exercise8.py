# Write a Code for checking the speed of drivers. This code should take one value: speed.
# If speed is less than 70, it should print “Ok”.
# Otherwise, for every 5km above the speed limit (70), it should give the driver one demerit point and print the total 
# number of demerit points. For example, if the speed is 80, it should print: “Points: 2”.
# If the driver gets more than 12 points, the function should print: “License suspended

speed=int(input("Enter the maximum speed : "))
demerit_points=0

if speed<=70:
    print("Ok")

elif speed>70 :
    a=(speed-70)//5
    demerit_points+=a
    print(demerit_points)
    if demerit_points>=12:
        print("License Expired")




