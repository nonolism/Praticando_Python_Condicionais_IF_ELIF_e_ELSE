def receber_quantidade_vendida_produto(produto) -> int:
    quantidade = int(input(f'Digite a quantidade de {produto} vendidas: '))
    return quantidade

def comparar_vendas(maças,bananas):
    if maças > bananas :
        print('As maças tiveram mais vendas.')
    elif maças < bananas:
        print('As bananas tiveram mais vendas.')
    else:
        print('Os 2 produtos venderam a mesma quantidade.')

def main():
    maças = receber_quantidade_vendida_produto('maças')
    bananas = receber_quantidade_vendida_produto('bananas')
    comparar_vendas(maças,bananas)
    
if __name__ == '__main__':
    main()