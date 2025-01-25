def main():
    temperatura_maxima = 25
    temperatura_atual = int(input('Digite a temperatura atual: '))
    if temperatura_atual > temperatura_maxima:
        print('Alerta! Temperatura acima do limite permitido.')
    
if __name__ == '__main__':
    main()