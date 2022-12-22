# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

# variant

# n = input()
# summ = 0
# for i in n:
#     if i.isdigit():
#         summ+=int(i)
# print(summ)

# n = float(input())
# len_num = len(str(n))-1
# summ=0
# while n!=int(n):
#     n= round(n*10,len_num)
#     print(n)
# while n>0:
#     summ+=n%10
#     n = n//10
# print(summ)


number=float(input("Enter number->  "))

while number != int(number):
    number *= 10
number=abs(int(number))
print("Digitals->  "+str(number))
 
s = 0
number=abs(number)
while number > 0:
    s += number % 10
    number //= 10
    s=int(s)
print("Sum digitals->  "+str(s))