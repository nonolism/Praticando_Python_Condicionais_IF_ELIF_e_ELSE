def main():
    limite_orcamento = 3000
    despesas = float(input('Digite o total de despesas do mês (R$): '))
    if despesas > limite_orcamento:
        print('Atenção! Você ultrapassou o limite de orçamento')

if __name__ == '__main__':
    main()