
def informar_tempo(atividade):
    tempo = int(input(f'Informe os dias para a atividade {atividade}: '))
    return tempo

def main():
    atividade_A = informar_tempo('A')
    atividade_B = informar_tempo('B')
    atividade_C = informar_tempo('C')
    
    if atividade_A < 0 or atividade_B < 0 or atividade_C < 0:
        print('Erro: Os dias não podem ser negativos.')
    else:
        tempo_total = atividade_A + atividade_B + atividade_C
        print(f'A quantidade total de dias para terminar as atividades é de {tempo_total} dias.')
        
if __name__ == '__main__':
    main()