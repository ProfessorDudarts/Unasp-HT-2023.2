'''
Receba n e mostre a soma dos quadrados de 1 até n - 1
'''
n = input('Digite um número inteiro')
n = int(n)

soma = 0
for x in range(1, n):
    soma += x ** 2

print(f'Com for - Total = {soma}')

soma = 0
while n > 1:
    n -= 1
    soma += n ** 2
print(f'Com while - Total = {soma}')

