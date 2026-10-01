"""
Esse projeto tem como objetivo auxiliar os pequenos empreendedores e moradores de cidades pequenas e/ou grandes a
economizarem em suas contas de luz. O intuito é que seja um app simples, de fácil acesso e manuseio.
Busco com isso ajudar o maior número de pessoas possíveis.
"""
"""
This project aims to help small business owners and residents of small and large cities save on their electricity bills. 
The goal is to create a simple app that is easy to access and use. Through this, I seek to help as many people as 
possible.
"""
from models import Aparelho

aparelhos = []

print("== CADASTRO DE APARELHOS ==")

while True:
    continuar = input("Deseja adicionar um novo aparelho? S/N").strip().upper()

    if continuar != "S":
        break

    nome = input(str("Insira o nome do aparelho:").strip())
    potencia = float(input("Insira o valor de potencia do aparelho em watts: "))
    horas = float(input("Insira o valor de horas utilizando o aparelho: "))
    dias = int(input("Insira o valor de Dias utilizando o aparelho: "))

    aparelho = Aparelho(nome, potencia, horas, dias)
    aparelhos.append(aparelho)

if aparelhos:
    print("\n" + "=" * 50)
    print("RELATÓRIO ENERGÉTICO DO ESTABELECIMENTO")
    print("-" * 50)

    consumo_total = 0
    custo_total = 0

    for aparelho in aparelhos:
        consumo = aparelho.calcular_consumo_mensal()
        custo = aparelho.calcular_custo_mensal()
        classificacao = aparelho.obter_classificacao()

        print(
            f"- {aparelho.nome}: "  f"{consumo:.2f} | " f" R$ {custo:.2f} | " f"[{classificacao}]")

        consumo_total += consumo
        custo_total += custo

    print("-" * 50)
    print(f"Consumo total: {consumo_total:.2f} kWh")
    print(f'Custo total: R$ {custo_total:.2f}')
    print("=" * 50)
else:
    print("\n Nenhum aparelho foi cadastrado")




