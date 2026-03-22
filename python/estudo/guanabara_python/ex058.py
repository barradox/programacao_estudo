"""
Melhore o jogo do DESAFIO 28 onde o computador vai "pensar" em um
número entre 0 e 10. Só que agora o jogador vai tentar adivinhar
até acertar, mostrando no final quantos palpites foram necessários
para vencer.

"""

from random import randint

print('Vou pensar em um número entre 0 e 10.')
numero = int(input('Tente adivinhar o número que eu pensei: '))

computador = randint(0, 10)
tentativa = 1
while numero  != computador:
    if numero < computador:
        print ('Mais...')
    else:
        print ('Menos...')
    numero = int(input('Tente novamente '))
    tentativa += 1

print('Parabéns, você ACERTOU em {} tentativas. '.format(tentativa))
