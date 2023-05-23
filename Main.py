n = int(input())

# Задача 2
# sum = 0

# while n>0:
#   ostatok = n%10
#   sum += ostatok
#   n //= 10

# print("Сумма цифр числа: ", sum)

#Задача 4
# res1 = (n/2)/3 + (n/2)
# print("Катя сделала " + str(int(res1)) + " журавликов, а Петя и Сережа по " + str(int((n/2)/3)) + " журавликов.")

# Задача 6
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