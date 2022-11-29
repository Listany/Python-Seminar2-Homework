# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число
n=int(input("Введите число N: "))
n_list=[]
for i in range(n*2+1):
    n_list.append(-n+i)    
print(n_list)
res=1
f=open('file.txt', 'r')
f_list=f.read().splitlines()
f.close()
print(f_list) 
for i in f_list:
    res=res*n_list[int(i)]      
print("Произведение указанных элементов равно", res)
