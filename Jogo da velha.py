import tkinter

# Funções:
def set_tile(row, column):
    global jog_atual
    
    if (game_over):
        return
    
    #Impedir a sobreposição de valor
    if tabuleiro[row][column]['text'] != '':
        return

    tabuleiro[row][column]['text'] = jog_atual
    if jog_atual == jog_O:
        jog_atual = jog_X
    else:
        jog_atual = jog_O

    label['text'] = 'Turno de '+jog_atual

    check_winner()


def new_game():
    global turno, game_over

    turno = 0
    game_over =False
    label.config(text='Turno de '+jog_atual, foreground='white')

    for row in range(3):
        for column in range(3):
            tabuleiro[row][column].config(text='', foreground=cor_1, background= cor_3)

def check_winner():
    global turno, game_over
    turno += 1

    #Checar as linhas
    for row in range(3):
        if (tabuleiro[row][0]['text'] == tabuleiro[row][1]['text'] == tabuleiro[row][2]['text']
            and tabuleiro[row][0]['text'] != ''):
            label.config(text=tabuleiro[row][0]['text']+' é o vencedor!', foreground=cor_2)
            game_over = True
            return
        
    # Checar as coluas
    for column in range(3):
        if (tabuleiro[0][column]['text'] == tabuleiro[1][column]['text'] == tabuleiro[2][column]['text']
            and tabuleiro[0][column]['text'] != ''):
            label.config(text=tabuleiro[row][0]['text']+' é o vencedor!', foreground=cor_2)
            game_over = True
            return

    # Checar diagonais:
    if (tabuleiro[0][0]['text'] == tabuleiro[1][1]['text'] == tabuleiro[2][2]['text']
        and tabuleiro[0][0]['text']!= '')  or (tabuleiro[0][2]['text'] == tabuleiro[1][1]['text'] == tabuleiro[2][0]['text']
        and tabuleiro[1][1]['text']!= ''):
            label.config(text=tabuleiro[1][1]['text']+' é o vencedor!', foreground=cor_2)
            game_over = True
            return
    
    # Empate
    if (turno == 9):
        game_over = True
        label.config(text='Empate!!!', foreground=cor_2)
    

# Visual
cor_1 = 'RoyalBlue1' # Cor das teclas
cor_2 = 'firebrick1' # Cor do texto no resultado final
cor_3 = 'RoyalBlue4' # Cor do fundo

tabuleiro = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]

# Jogador
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

# Rodadas
turno = 0
game_over = False

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
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

window.geometry(f'{window_width}x{window_height}+{window_x}+{window_y}')

window.mainloop()