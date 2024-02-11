# [LP-A03] Escreva um programa em python que leia números inteiros do teclado.
# O programa deve ler os números até que o usuário digite 0 (zero).
# No final da execução, exiba a quantidade de números digitados, assim como a soma e a média aritmética.

numeros = []
soma = 0
quantidade = 0

while True:
    num = int(input("Digite um número inteiro (0 para sair): "))
    if num == 0:
        break
    numeros.append(num)
    soma += num
    quantidade += 1

media = soma / quantidade

print("Quantidade de números digitados:", quantidade)
print("Soma dos números:", soma)
print("Média aritmética:", media)