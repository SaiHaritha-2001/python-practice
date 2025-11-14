# # # if,elif,nestedif,else
# # # a=int(input())
# # # # b=int(input())
# # # if(a>0):
# # #     print("The number id +ve ")
# # # else:
# # #     print("-ve")
# # a=int(input())
# # b=int(input())
# # if(a>b):
# #     print("a is greater")
# # else:
# #     print("b is greater")
# # the pbm statement is to write a code for put stars in middle of a letter that leave firs and lasst eg:hello----->h***o
# word=input()
# fc=word[0]
# length=len(word)
# lc=word[length-1]
# stars="*"*(length-2)
# res=fc+stars+lc
# print(res)
# number=input("enter the number")
# first=number[0]
# length=len(number)
# second=number[length-1]
# stars="$"*(length-2)
# print(first+stars+second)
word=input()
fchar=word[0]
length=len(word)
lchar=word[length-1]
star="*"*(length-2)
result=fchar+star+lchar
print(result)