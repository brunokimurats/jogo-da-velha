# jogo da velha

import tkinter


jog_X = 'X'
jog_O = 'O'
inicio = input(f'Quem irá começar? ')
if inicio in'Xx':
    jog_atual = jog_X
    print('X')
elif inicio in 'oO0':
    jog_atual = jog_X
    print('O')

tabuleiro = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]

cor_1 = '#252f9c'
cor_2 = 'cfe5ff'
cor_3 = '7c1034'
cor_4 = 'd1dfbb'

window = tkinter.Tk()
window.title('Jogo da Velha')
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text='Turno de '+jog_atual, font=('Consolas', 20),
                       background = cor_3, foreground='white')
label.pack()


window.mainloop()