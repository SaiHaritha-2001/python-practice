# name=input()
# length=len(name)
# for i in range(1,length+1):
#     print(name[ :i])
'''# shuffled number
s=input()
shuffled_s=""
for i in range(len(s)):
    index=int(input())
    shuffled_s += s[index]
print(shuffled_s)'''
#prime number
number=int(input())
factors=0
for i in range(2,number):
    if number % i ==0:
        factors+=1
if factors==0:
    print("prime")
else:
    print("not prime")        
