# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

number=int(input("Enter number->  "))
array=[1 for i in range(number)]
j=1
k=1
print(array)
while j<number:
    k=k*(j+1)
    array[j]=array[j]*k
    print(array[j], end=' ')
    j=j+1
print()
print(k)
print(array)



# n = int(input())
# fact_list = []
# factorial = 1
# for i in range(1,n+1):
#     factorial*=i
#     fact_list.append(factorial)
# print(fact_list)
