n = int(input())
sum = 0

while n>0:
  ostatok = n%10
  sum += ostatok
  n //= 10

print("Сумма цифр числа: ", sum)
