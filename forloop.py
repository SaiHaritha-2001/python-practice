# # # word="hello"
# # # for each_char in word:
# # #     print(each_char)
# # num=int(input())
# # for  i in range(num):
# #     print(i)
# n = int(input())
# count=1
# for num in range(4,n):
#     print("* "*(num+1))
#     count=count+1
# num= int(input())
# count=0
# for i in range(1,num+1):
#     print("* "*i)
#     count=count+1
a=input()
leng=len(a)
b=a[0]
for i in range(1,leng):
    b=b+"_"+a[i]
    print(b)