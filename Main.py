<<<<<<< HEAD
# Задача 2
# n = int(input("Введите трёхзначное число"))
# sum = 0

=======
n = int(input())

# Задача 2
# sum = 0

>>>>>>> ced90b729194b2dc6799dcf32de609302dea543f
# while n>0:
#   ostatok = n%10
#   sum += ostatok
#   n //= 10

# print("Сумма цифр числа: ", sum)

#Задача 4
<<<<<<< HEAD
# n = int(input("Введите количество журавликов, которые сделали все ребята вместе"))
=======
>>>>>>> ced90b729194b2dc6799dcf32de609302dea543f
# res1 = (n/2)/3 + (n/2)
# print("Катя сделала " + str(int(res1)) + " журавликов, а Петя и Сережа по " + str(int((n/2)/3)) + " журавликов.")

# Задача 6
<<<<<<< HEAD
# n = int(input("Введите шестизначный номер билетика"))
# count = 0
# res1 = 0
# res2 = 0
# while n>0:
#     if count < 3:
#         res1 += n%10
#         n //= 10
#         count += 1
#     else:
#         res2 += n%10
#         n //= 10
#         count += 1
# if res1 == res2:
#     print("Билет счастливый!")
# else:
#     print("Повезёт в другой раз!")

# Задача 8
n = int(input("Введите первое число: "))
m = int(input("Введите второе число: "))
z = int(input("Введите, сколько долек нужно получить: "))

if ((m*n) > z) & ((z%n == 0) | (z%m == 0)):
    print("Можно!")
else:
    print("Нельзя!")
=======
count = 0
res1 = 0
res2 = 0
while n>0:
    if count < 3:
        res1 += n%10
        n //= 10
        count += 1
    else:
        res2 += n%10
        n //= 10
        count += 1
if res1 == res2:
    print("Билет счастливый!")
else:
    print("Повезёт в другой раз!")
>>>>>>> ced90b729194b2dc6799dcf32de609302dea543f
