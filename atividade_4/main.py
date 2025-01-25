def main():
    peso = float(input('Digite seu peso (kg): '))
    altura = float(input('Digite sua altura (m): '))
    imc = peso / (altura ** 2)
    
    if imc < 18.5:
        situacao = 'abaixo do peso'
    elif 18.5 <= imc < 25:
        situacao = 'peso normal'
    else:
        situacao = 'acima do peso'
    
    print(f'Seu IMC é: {imc:.2f}')
    print(f'Você está {situacao}.')
    
    
if __name__ == '__main__':
    main()