
def main():
    renda_mensal = float(input('Digite o valor da sua renda mensal: '))
    valor_parcela = float(input('Digite o valor da parcela desejada: '))
    porcentagem_parcela = (valor_parcela / renda_mensal) * 100
    
    if renda_mensal > 2000 and porcentagem_parcela <= 30:
        print('Emprestimo aceito!')
    elif renda_mensal <= 2000 and porcentagem_parcela <= 30:
        print('Empréstimo negado: Renda abaixo do minimo.')
    elif renda_mensal > 2000 and porcentagem_parcela >= 30:
        print('Empréstimo negado: parcela acima de 30% da renda')
    else:
        print('Empréstimo negado: Renda abaixo do minimo e parcela acima de 30% da renda')
    
if __name__ == '__main__':
    main()