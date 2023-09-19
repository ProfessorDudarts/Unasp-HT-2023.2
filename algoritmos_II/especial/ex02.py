def soma_vetores(vetor1: list, vetor2:list) -> list:
    vetor_soma = []
    maior = max(len(vetor1), len(vetor2))
    for i in range(maior):
        valor1 = vetor1[i] if i < len(vetor1) else 0
        valor2 = vetor2[i] if i < len(vetor2) else 0

        vetor_soma.append(valor1 + valor2)
    return vetor_soma


l1 = [1, 2, 3]
l2 = [7, 8, 9, 6]
l3 = soma_vetores(l1, l2)
print(l3)