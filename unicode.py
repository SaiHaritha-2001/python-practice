for i in range(ord('a'),ord('z')+1):
    print(f"{chr(i)}---{i}")


'''
ord()----to find unicode with  char
chr()----to find char with unicode
uni code ranges:
48-57 ---------->  number digits(0-9)
65-90----------->  capital letters(A-Z)
97-122 --------->  small letters(a-z)
rest  -----> special charavcters,other languages
'''
# a=ord('!')
# print(a)
for i in range(2309,2329):
    print(f"{chr(i)}") 