
def transpor(matriz: list) -> list:
    transposta = []

    for _ in range(len(matriz[0])):
        transposta.append([0 for _ in range(len(matriz))])
   
    for i, l in enumerate(matriz):  
        for j, v in enumerate(l): 
            transposta[j][i] = v

    return transposta


matriz = [
    [1, 7, 5],
    [8, 2, 1],
    [4, 9, 0],
    [2, 3, 9]
]

t = transpor(matriz)
print(t)
