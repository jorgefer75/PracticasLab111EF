n=int(input("n: "))
binario = ''
while n // 2 != 0:
    binario = str(n % 2) + binario
    n = n // 2
print(str(n) + binario)