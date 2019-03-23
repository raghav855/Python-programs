# Exercise 1
f=open('lines.txt','w')
for i in range(1,101):
   f.write("This is line "+str(i)+"\n")
f.close()
    

# Exercise 2

f=open('lines.txt','r')
count=0
for i in f:
    if count>=0 and count<10:
        print(i)
        count+=1
    elif count>=50 and count<60:
        print(i)
        count+=1
        
    elif count>=90 and count<100:
        print(i)
        count+=1
    else:
        count+=1    
 
# Exercise 3 

f=open('lines.txt','a')
for i in range(101,121):
  f.write("This is line "+str(i)+"\n")
 
# Exercise 4    
  
f=open('lines.txt','r+')
for i in range(1,13):
    a="lines"+str(i)+'.txt'
    f1=open(a,'w+')
    for i in range(10):
        b=f.readline()
        f1.write(b)
        
