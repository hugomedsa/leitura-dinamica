# coding: iso-8859-1 -*-
# N�o apagar a linha acima, "coding". Caixa de script aberta at� a linha 25 quando pag = 26.
# Usar Pycharm tema Darcula, fonte Arial 17, espa�o 1.0)
# Settings > Editor > General > Scrolling > Marcar apenas "Keep the caret"...
from time import sleep, time
import simpleaudio
from tkinter import *
import wikipedia

def baixar_wikipedia():
    wikipedia.set_lang('pt')
    text = wikipedia.page("ci�ncia de dados").content.replace('\n',' ')
    return texto

strong_beat = simpleaudio.WaveObject.from_wave_file('sounds/strong_beat.wav')
weak_beat = simpleaudio.WaveObject.from_wave_file('sounds/weak_beat.wav')


menu_inicial = Tk()
menu_inicial.title("Leitura Din�mica")
menu_inicial.state("zoomed")
menu_inicial['bg'] = 'black'
# menu_inicial.mainloop()

margem = ''  # apenas para centralizar o texto e n�o formatar espa�os
pag = 27


with open('texto-rapido.txt','r') as file:
    arquivo = file.read().replace('\n',' ')
    if len(arquivo) < 5000:
        texto = baixar_wikipedia()
        with open('texto-rapido.txt', 'w') as filer:
            arquivo = filer.write(texto)
    else:
        with open('texto-rapido.txt', 'w') as filer:
            texto = arquivo[1000:]
            arquivo = filer.write(texto)

s = 0.22  # velocidade, quanto mais baixo, mais r�pido
len_linha = 40

texto = texto[:10000]

inicio = time()

for t in range(0, len(texto.split())//pag): #somat�rio de p�ginas

    for p in range(0, pag):

        if t == 0:
            iniciobloco = 0
            fimbloco = bp = len_linha
        else:
            iniciobloco = (pag*len_linha*t)+1  # pag*len_linha � o total de caracteres em cada p�gina exibida
            fimbloco = iniciobloco + len_linha
        for c in range(0, pag):
            if len(texto) > fimbloco + len_linha:
                bloco = texto[iniciobloco + texto[iniciobloco:].index(' '):fimbloco + texto[fimbloco:].index(' ')]
            else:
                bloco = texto[iniciobloco:fimbloco]

            if c != p:
                print('')
                print(f'\033[90m{bloco.center(200," ")}', end='\033[m')  # "20" � a margem n�o destacada
                #print(f'\033[33m{bloco:>130}', end='\033[m')  # "20" � a margem n�o destacada

            else:
                if bloco.replace(' ', '').replace('.', '') == '':
                    break
                print('')
                print(f'\033[33m{bloco.center(200," ")}', end='\033[m')
                #print(f'{bloco:>130}', end='\033[m')
                # print(f'{"["+bloco[1:]+"]":>131}', end='\033[m')
            iniciobloco += bp
            fimbloco += bp

        if bloco.replace(' ', '').replace('.', '') == '':
            break
        weak_beat.play()
        print('')
        sleep(s)

fim = time()

print(f'Voc� leu {len(texto.split())} palavras.')
print(f'Sua velocidade de leitura � de  {int(len(texto.split())*60/(fim-inicio))} p.p.m.')