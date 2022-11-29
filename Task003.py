# Задайте словарь из n чисел последовательности (1 + (1/n))^n и выведите на экран их сумму.

n=int(input("Введите число N: "))

n_dict={}

for i in range (1, n+1):
    n_dict[i]=(1+(1/i))**i

res=0

for i in range(1, n+1):
    res+=n_dict[i]

print(res)