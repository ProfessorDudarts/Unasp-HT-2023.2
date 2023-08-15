padrao = 7

'''
for i in range(1, padrao):
    print('*' * i)

for i in range(padrao, 0, -1):
    print('*' * i)
'''


for i in range(1, padrao):
    for j in range(1, i):
        print('*', end="")
    print()

for i in range(padrao, 0, -1):
    for j in range(i, 0, -1):
        print('*', end="")
    print()

print('Dudarts' * 10)