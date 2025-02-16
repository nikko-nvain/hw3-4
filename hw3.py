#первое задание
n = int(input())
for number in range(1, n + 1):
    digits = list(str(number))
    k = len(digits)
    sum_powers = sum(int(d)**k for d in digits)
    if sum_powers == number:
        print(number)

#второе задание
n = int(input())
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(factorial)

#третье задание
x = int(input())
divisors = set()
for i in range(1, int(x**0.5) + 1):
    if x % i == 0:
        divisors.add(i)
        divisors.add(x // i)
print(' '.join(map(str, sorted(divisors))))