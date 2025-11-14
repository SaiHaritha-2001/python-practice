number=int(input())
fact=0
for i in range(2,number):
    
    if number % i ==0:
        fact+=1
if fact==0:
     print("yes it is prime")
else:
     print("no it is not prime")

