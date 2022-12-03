# coding: iso-8859-1 -*-
# Não apagar a linha acima, "coding".
# Pycharm Color Scheme Font: tema Darcula, fonte Arial 16, espaço 1.0)
# Settings > Editor > General > Scrolling > Marcar apenas "Keep the caret"...
from time import sleep,time
import simpleaudio
import wikipedia

def baixar_wikipedia():
    wikipedia.set_lang('pt')
    texto = wikipedia.page("ciência de dados").content.replace('\n',' ')
    return texto


strong_beat = simpleaudio.WaveObject.from_wave_file('sounds/strong_beat.wav')
weak_beat = simpleaudio.WaveObject.from_wave_file('sounds/weak_beat.wav')

margem = ''  # apenas para centralizar o texto e não formatar espaços
pag = 52  # somatório de todas as meias linhas

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

s = 0.20 # velocidade: quanto mais baixa, mais rápido
texto = texto[:10000]
init = time()

for t in range(0, (len(texto)//(pag*40))+1):
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
                    if bloco.replace(' ', '').replace('.', '') == '':
                        break
                    weak_beat.play()
                    print(f'{margem:>35}\033[33m{bloco:>65}', end='\033[m')  # "35" é a margem não destacada
                    print(end='')
                else:
                    strong_beat.play()
                    print(f'\033[33m{bloco}', end='\033[m')
                    print('')

            else:
                if c % 2 == 0:
                    if bloco.replace(' ', '').replace('.', '') == '':
                        break
                    print(f'{bloco:>100}', end='\033[m')
                    print(end='')
                else:
                    print(f'{bloco}', end='\033[m')
                    print('')
            iniciobloco += bp
            fimbloco += bp
        sleep(s)
    #s -= 0.005   # vai aumentando a velocidade aos poucos. Opcional.
        print('')

fim = time()

print(f'Você leu {len(texto.split())} palavras.')
print(f'Sua velocidade de leitura foi {round(len(texto.split())*60/(fim-init),0)} p.p.m.')