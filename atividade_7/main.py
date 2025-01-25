def receber_nota(posicao_nota) -> float:
    nota = float(input(f'Digite a {posicao_nota} nota: '))
    return nota

def resultado_notas(media):
    if media < 5:
        resultado = 'Reprovado'
    elif 5 <= media < 7:
        resultado = 'Recuperação'
    else:
        resultado = 'Aprovado'
    return resultado

def main():
    nota_1 = receber_nota('primeira')
    nota_2 = receber_nota('segunda')
    nota_3 = receber_nota('terceira')
    
    media = (nota_1 + nota_2 + nota_3) / 3
    print(f'Média: {media:.2f}')
    resultado = resultado_notas(media)
    print(resultado)

    
if __name__ == '__main__':
    main()