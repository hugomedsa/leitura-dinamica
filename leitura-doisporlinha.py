# coding: iso-8859-1 -*-
# N�o apagar a linha acima, "coding".
# Pycharm Color Scheme Font: tema Darcula, fonte Arial 16, espa�o 1.0)
# Settings > Editor > General > Scrolling > Marcar apenas "Keep the caret"...
from time import sleep,time
import simpleaudio
import wikipedia
import _thread

def baixar_wikipedia():
    wikipedia.set_lang('pt')
    texto = wikipedia.page("aprendizado de m�quina").content
    return texto.replace('\n',' ')

#strong_beat = simpleaudio.WaveObject.from_wave_file('sounds/strong_beat.wav')
weak_beat = simpleaudio.WaveObject.from_wave_file('sounds/weak_beat.wav')
margem = ''  # apenas para centralizar o texto e n�o formatar espa�os
pag = 54  # somat�rio de todas as meias linhas
s = 0.21 # velocidade: quanto mais baixa, mais r�pido


with open('texto-rapido.txt','r',encoding="utf-8") as file:
    arquivo = file.read().replace('\n',' ')
    if len(arquivo) < 5000:
        text = baixar_wikipedia().replace('=','.')
        with open('texto-rapido.txt', 'w', encoding="utf-8") as filer:
            arquivo = filer.write(text)
    else:
        with open('texto-rapido.txt', 'w', encoding="utf-8") as filer:
            text = arquivo[5000:]
            arquivo = filer.write(text)

try:
    texto = text[:5000]
except UnicodeEncodeError:
    texto = text

init = time()

for t in range(0, (len(texto)//(pag*40)+1)):
    for p in range(0, pag):
        if t == 0:
            iniciobloco = 0
            fimbloco = bp = 40
        else:
            iniciobloco = (pag*40*t)+1
            fimbloco = iniciobloco + 40
        for c in range(0, pag):
            if len(texto) > fimbloco + 40:
                bloco = texto[iniciobloco + texto[iniciobloco:].index(' '):fimbloco + texto[fimbloco:].index(' ')]
            else:
                bloco = texto[iniciobloco:fimbloco]
            if c == p:
                if c % 2 == 0:
                    print(f'{margem:>45}\033[33m{bloco:>75}', end='\033[m')  # "35" � a margem n�o destacada
                    print(end='')
                    weak_beat.play()
                else:
                    print(f'\033[33m{bloco}', end='\033[m')
                    print('')


            else:
                if c % 2 == 0:
                    print(f'\033[m{bloco:>120}', end='\033[m') #33[90m � cinza 33[33m � verde
                    print(end='')
                else:
                    print(f'\033[m{bloco}', end='\033[m')
                    print('')

            if c==p and bloco == '':
                print('')
                break
            iniciobloco += bp
            fimbloco += bp

        if c == p and bloco == '':
            print('')
            break
        sleep(s)
        print('')

fim = time()

print(f'Voc� leu {len(texto.split())} palavras.')
print(f'Sua velocidade de leitura foi {round(len(texto.split())*60/(fim-init),0)} p.p.m.')