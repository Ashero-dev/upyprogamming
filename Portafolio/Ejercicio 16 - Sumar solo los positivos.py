#16 suma de numeros positivos

numeros = [5, 10, -50, 70, -6, -5, -8]
t = 0
for n in numeros:
    if n < 0:
        continue
    t = t + n
    print(n)

print("total:", t)