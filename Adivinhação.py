from random import randint
from time import sleep
computador = randint(0, 10) #faz o computador pensar
print('\033[1;33m-=-\033[m'*20)
print('\033[1;34m vou pensar em um número entre 0 e 10, tente advinhar...\033[m')
print('\033[1;33m-=-\033[m'*20)
jogador = int(input("em que numero eu pensei? ")) #jogador tenta advinhar
print("processando...")
sleep(1)
print("1%...")
sleep(2)
print("35%...")
sleep(1)
print("79%...")
sleep(1)
print("99%...")
sleep(3)
print("completo")
sleep(1)
if jogador == computador:
    print('Parabens, Você acertou')
else:
    print("ganhei, eu pensei no número {}, e não em {}".format(computador, jogador))
