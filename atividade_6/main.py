def main():
    hora_atual = int(input('Digite a hora atual (formato 24 horas): '))
    
    if 8 <= hora_atual <= 18:
        print('Acesso Liberado.')
    else:
        print('Acesso negado.')

if __name__ == '__main__':
    main()