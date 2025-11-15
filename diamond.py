num = int(input())
left_space_count= num-1
left_space=" "*left_space_count
row_output = left_space + "*"
print(row_output)
hollo_space_count=-1
for i in range(2,num+1):
  left_space_count= num-i
  left_space=" "*left_space_count
  hollo_space_count=hollo_space_count+2
  hollo_space=" "*hollo_space_count
  row_output = left_space + "*"+ hollo_space+"*"
  print(row_output)
  
for row in range(1,num-1):
  left_space_count= row
  left_space=" "*left_space_count
  hollo_space_count=hollo_space_count-2
  hollo_space=" "*hollo_space_count
  row_output = left_space + "*"+ hollo_space+"*"
  print(row_output)
left_space_count= num-1
left_space=" "*left_space_count
row_output = left_space + "*"
print(row_output)
hollo_space_count=-1
  
  
  
  
  
  
  

  
  
  