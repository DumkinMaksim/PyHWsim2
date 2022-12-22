# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.


import random

n = int(input('Enter N->  '))
list_num = [random.randint(-n,n) for i in range(n)]
print('List is range N='+str(n)+'  '+str(list_num))

file = open("File.txt","r")
multi = 1
list_str = file.readlines()
# print(list_str)
list_num2 = list(map(str.strip,list_str))
# print(list_num2)
list_num2 = list(map(int,list_num2))
print('Pozishion index in File.txt->  '+str(list_num2))
for i in range(len(list_num2)):
    multi*=list_num[list_num2[i]]
  
print('Composition numbers for pozishion File.txt->  '+str(multi))
