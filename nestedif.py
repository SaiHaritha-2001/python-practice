# a=int(input())
# b= int(input())
# c=int(input())
# if(a>b and a>c):
#     print(" a is greater")
# elif(b>a and b>c):
#     print("b is greater ")
# else:
#     print("c is greater")
#the number is divisible by 5 or 10
# num=int(input())
# if((num%10==0)or(num%5==0)):
#     print("yes divesible")
# else:
#     print("not divisible")
num=int(input())
if(num%10==0):
    print("the number divisible by 10")
elif((num % 5==0)and (num%10 !=0)):
    print("the number is divisible by 5")
else:
    print("number is invalid")