#!/usr/bin/env python

import random
import os

clear = lambda: os.system('clear')
clear()

palavra = ''
letras = []
acertos = -1
vidas = 6

for numero in range(vidas):
    print('* ', end=" ")
print("")

#abre a lista de palavras e pega uma palavra aleatoriamente
with open('Lista.txt','r') as lista:
    linhas = lista.readlines()
    palavra = (linhas[random.randrange(0,len(linhas))])

#separa a palavra em letras
for char in palavra:
    letras.append(char)
    if (char != '-'): #conta as letras que precisam ser acertadas para vencer
        acertos += 1

#remove a ultima letra que é um espaço em branco
letras = letras[:-1]
letrasTestadas = []

#loop do jogo
while (acertos > 0):
    if (vidas <= 0):
        print('Voce perdeu, a palavra era:', end=" ")
        break

    print('')
    for char in letras:
       if (char != '-') & (char not in letrasTestadas): print('_', end=" ")
       elif (char in letrasTestadas): print(char,end=" ")
       else: print('-', end=" ")

    print('')
    teste = input('\nO que voce acha: ')
    
    clear()

    if (teste not in letrasTestadas) & (teste not in letras):
        vidas = vidas - 1

    if (teste in letrasTestadas):
        print('Letra ja testada ')
    else:
        letrasTestadas.append(teste)#adiciona o teste a lista de letras ja testadas
        for x in range(len(letras)):
            if (teste == letras[x]):#checa se a letra esta certa 
                acertos = acertos - 1 #conta o acerto

    for numero in range(vidas):
        print('* ', end=" ")

clear()
while (acertos == 0):
    clear()
    print('⠄⠄⠄⠄⠄⠄⠄⣠⣴⣶⣿⣿⡿⠶⠄⠄⠄⠄⠐⠒⠒⠲⠶⢄⠄⠄⠄⠄⠄⠄\n\
⠄⠄⠄⠄⠄⣠⣾⡿⠟⠋⠁⠄⢀⣀⡀⠤⣦⢰⣤⣶⢶⣤⣤⣈⣆⠄⠄⠄⠄⠄\n\
⠄⠄⠄⠄⢰⠟⠁⠄⢀⣤⣶⣿⡿⠿⣿⣿⣊⡘⠲⣶⣷⣶⠶⠶⠶⠦⠤⡀⠄⠄\n\
⠄⠔⠊⠁⠁⠄⠄⢾⡿⣟⡯⣖⠯⠽⠿⠛⠛⠭⠽⠊⣲⣬⠽⠟⠛⠛⠭⢵⣂⠄\n\
⡎⠄⠄⠄⠄⠄⠄⠄⢙⡷⠋⣴⡆⠄⠐⠂⢸⣿⣿⡶⢱⣶⡇⠄⠐⠂⢹⣷⣶⠆\n\
⡇⠄⠄⠄⠄⣀⣀⡀⠄⣿⡓⠮⣅⣀⣀⣐⣈⣭⠤⢖⣮⣭⣥⣀⣤⣤⣭⡵⠂⠄\n\
⣤⡀⢠⣾⣿⣿⣿⣿⣷⢻⣿⣿⣶⣶⡶⢖⣢⣴⣿⣿⣟⣛⠿⠿⠟⣛⠉⠄⠄⠄\n\
⣿⡗⣼⣿⣿⣿⣿⡿⢋⡘⠿⣿⣿⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠄⠄\n\
⣿⠱⢿⣿⣿⠿⢛⠰⣞⡛⠷⣬⣙⡛⠻⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⠿⠛⣓⡀⠄\n\
⢡⣾⣷⢠⣶⣿⣿⣷⣌⡛⠷⣦⣍⣛⠻⠿⢿⣶⣶⣶⣦⣤⣴⣶⡶⠾⠿⠟⠁⠄\n\
⣿⡟⣡⣿⣿⣿⣿⣿⣿⣿⣷⣦⣭⣙⡛⠓⠒⠶⠶⠶⠶⠶⠶⠶⠶⠿⠟⠄⠄⠄\n\
⠿⡐⢬⣛⡻⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡶⠟⠃⠄⠄⠄⠄⠄⠄\n\
⣾⣿⣷⣶⣭⣝⣒⣒⠶⠬⠭⠭⠭⠭⠭⠭⠭⣐⣒⣤⣄⡀⠄⠄⠄⠄⠄⠄⠄⠄\n\
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠄⠄⠄⠄⠄⠄⠄')
    acertos = acertos - 1
   
print(palavra)
