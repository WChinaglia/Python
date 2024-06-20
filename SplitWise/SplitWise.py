import numpy as np

print("--------- Divisão de Contas ---------")
print("---- Wildson Chinaglia 19/02/2024 ---")
print("-------------------------------------")

split = {}
while True:
    pessoa = input('Digite o nome: ')
    reais = float(input('Insira o valor gasto: '))
    split[pessoa] = reais
    loop = input('Adicionar mais pessoas? "s" ou "n": ')
    if loop == 's':
        print('OK!')
    else:
        print()
        print('Total de participantes da conta:')
        for show in split:
            print(show, split[show], sep=' - ')
        print()
        break


def somar_sobra(dici):
    divisao = extra
    while divisao != 0:
        for ad in dici.keys():
            if dici[ad] > 0:
                mais = np.round(dici[ad] + 0.01, 2)
                dici[ad] = mais
                divisao = np.round(divisao - 0.01, 2)
                if divisao == 0:
                    break
            else:
                menos = np.round(dici[ad] - 0.01, 2)
                dici[ad] = menos
                divisao = np.round(divisao + 0.01, 2)
                if divisao == 0:
                    break


# Ordenar dicionário "split_order" por valor mais alto a baixo
split_order = {}
valores = list(split.values())
maximo = np.max(valores)
while valores:
    for chave in split.keys():
        valor = split[chave]
        if valor == maximo:
            split_order[chave] = valor
            valores.remove(valor)
            if valores:
                maximo = np.max(valores)
            else:
                break

# Total gasto por todos juntos
soma = np.round(sum(split_order.values()), 2)
print(f'Total gasto: {soma}')

# Valor por cabeça
quant = len(split_order.items())
individual = np.round(soma / quant, 2)
print(f'Por pessoa: {individual}')

# Valor que sobra de contas não exatas.
# Negativo = a pagar | Positivo = a receber
extra = np.round((individual * quant) - soma, 2)

# PRINT PARA TESTAR O CÓDIGO:
# print(f'EXTRA (conta não exata): {extra}')
# print()

# Dividir pessoas em dois dicionários, quem deve pagar/quem deve receber
pagar = {}
receber = {}
for v in split_order.keys():
    valor = np.round(split_order[v] - individual, 2)
    if valor > 0:
        receber[v] = valor
    else:
        pagar[v] = valor

# PRINT PARA TESTAR O CÓDIGO:
# print(f'Valores a pagar: {pagar}')
# print(f'Valores a receber: {receber}')
print('-' * 40)

# Dividir valor extra entre devedores ou credores
if extra > 0:
    somar_sobra(receber)
elif extra < 0:
    somar_sobra(pagar)
else:
    pass

print(f'Valores a pagar: {pagar}')
print(f'Valores a receber: {receber}')
print()

# Divisão de valores a pagar entre pessoas a receber
for p in pagar:
    pago = pagar[p] * (-1)
    for r in receber:
        if pago == 0:
            continue
        else:
            saldo = np.round(receber[r] - pago, 2)
            if saldo < 0:
                pago = np.round(pago + saldo, 2)
                if receber[r] > 0:
                    print(f'{p} deve pagar {pago} a {r}')
                receber[r] = 0
                saldo = saldo * (-1)
                pago = saldo
            else:
                receber[r] = saldo
                print(f'{p} deve pagar {pago} a {r}')
                pago = 0
