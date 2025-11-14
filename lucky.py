num=int(input())
num1=str(num)
first=int(num1[0])
second=int(num1[1])
first1=(first==9)
second1=(second==9)
hi=first1 or second1
if((num % 9==0 ) or hi):
    print("lucky number")
else:
    print("unlucky number")