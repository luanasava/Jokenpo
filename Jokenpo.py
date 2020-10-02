#Jogo
from random import randint
opc = ('Papel', 'Pedra', 'Tesoura')
pc = randint(1, 3)
print('''Opções:
-------------------------
[ 1 ] PAPEL
[ 2 ] PEDRA
[ 3 ] TESOURA
[ ? ] Qualquer outra opção, finalizará o jogo''')
usuario = 1
print('-' * 25)

#vetores
vetor_vitoria = [0]
vetor_derrota = [0]
vetor_empate = [0]

                        #Resultado
def soma():
    resultado = (len(vetor_empate) - 1) + (len(vetor_vitoria) - 1) + (len(vetor_derrota) - 1)
    return resultado
                        #% vitória
def pv():
    resultad1 = (len(vetor_vitoria) - 1) / soma() * 100
    return resultad1
                        #% derrota
def pd():
    resultad2 = (len(vetor_derrota) - 1) / soma() * 100
    return resultad2
                        #%%empate
def pe():
    resultad3 = (len(vetor_empate) - 1) / soma() * 100
    return resultad3

#Contador
contador = 0

                        #Resultado
while usuario < 4 and usuario > 0:
    usuario = int(input('Pedra, papel ou tesoura: '))
    pc = randint(1, 3)
    if usuario <= 0 or usuario > 3:
        print('-' * 25)
        print("JOGO ENCERRADO!")
        print('-' * 25)
        print('Vitórias: {}'.format(len(vetor_vitoria)-1))
        print('Derrotas: {}'.format(len(vetor_derrota)-1))
        print('Empates: {}'.format(len(vetor_empate)-1))
        print('Total de partidas: {}'.format(soma()))
        print('-' * 25)
        print('Resultado em % é:')
        print('Vitórias: {}'.format(pv()))
        print('Derrotas: {}'.format(pd()))
        print('Empates: {}'.format(pe()))
        break
    print('Você jogou {}'.format(opc[usuario-1]))
    print('O computador jogou {}'.format(opc[pc-1]))
    contador += 1

    if pc == 1: #pc jogou papel
        if usuario == 1:
            vetor_empate.append(1)
            print("Empatou!")
            print('-' * 25)
        elif usuario == 2:
            vetor_derrota.append(1)
            print("Você perdeu!")
            print('-' * 25)
        elif usuario == 3:
            vetor_vitoria.append(1)
            print("Você ganhou!")
            print('-' * 25)
        else:
            print("JOGO ENCERRADO!!")

    elif pc == 2: #pc jogou pedra
        if usuario ==1:
            vetor_vitoria.append(1)
            print("Você ganhou!")
            print('-' * 25)
        elif usuario == 2:
            vetor_empate.append(1)
            print("Empatou!")
            print('-' * 25)
        elif usuario == 3:
            vetor_derrota.append(1)
            print("Você perdeu!")
            print('-' * 25)
        else:
            print("JOGO ENCERRADO!!")

    elif pc == 3: #pc jogou tesoura
        if usuario == 1:
            vetor_derrota.append(1)
            print("Você perdeu!")
            print('-' * 25)
        elif usuario == 2:
            vetor_vitoria.append(1)
            print("Você ganhou!")
            print('-' * 25)
        elif usuario == 3:
            vetor_empate.append(1)
            print("Empatou!")
            print('-' * 25)
        else:
            print('JOGO ENCERRADO!!')