# jogo da velha

import tkinter

def set_tile(row, column):
    pass

def new_game():
    pass


cor_1 = 'RoyalBlue2'
cor_2 = 'yellow2'
cor_3 = 'PeachPuff3'
cor_4 = 'dark slade blue'

tabuleiro = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]

jog_X = 'X'
jog_O = 'O'
jog_atual = jog_X
#inicio = input(f'Quem irá começar? ')
#if inicio in'Xx':
#    jog_atual = jog_X
#    print('X')
#elif inicio in 'oO0':
#    jog_atual = jog_X
#    print('O')


window = tkinter.Tk()
window.title('Jogo da Velha')
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text='Turno de '+jog_atual, font=('fixedsys', 20),
                       background = cor_3, foreground='white')
label.grid(row=0, column=0, columnspan=3, sticky='we')

for row in range(3):
    for column in range(3):
        tabuleiro[row][column] = tkinter.Button(frame, text='', font=('fixedsys', 50, 'bold'),
                                                background= cor_3, foreground=cor_1, width=4, height=1,
                                                command=lambda row=row, column=column: set_tile(row, column))
        tabuleiro[row][column].grid(row = row + 1, column= column)

reiniciar = tkinter.Button(frame, text='Reiniciar', font=('fixedsys', 20), 
                           background=cor_3, foreground='white',
                           command=new_game)
reiniciar.grid(row=4, column=0, columnspan=3, sticky='we')


frame.pack()

window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenmmwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

window.geometry(f'{window_width}x{window_height}+{window_x}+{window_y}')

window.mainloop()