from tkinter import *
from tkinter import Tk, ttk
from PIL import Image, ImageTk
from random import sample

cor0 = "#2e2d2b" # Preto
cor1 = "#feffff" # Branco
cor2 = "#4fa882" # verde 
cor3 = "#38576b" # cor do valor
cor4 = "#403d3d" # cor da letra
cor5 = "#e06636" # - profit
cor6 = "#038cfc" # azul
cor7 = "#3fbfb9" # verde


# abrindo as imagens de maneira dinâmica
def abrir_imagens(img_resultado, img_casal):
    global imagem_casal, imagem_resultado

    imagem_casal = Image.open(img_casal)
    imagem_casal = imagem_casal.resize((170,170))
    imagem_casal = ImageTk.PhotoImage(imagem_casal)
    mostrar_imagem['image'] = imagem_casal

    imagem_resultado = Image.open(img_resultado)
    imagem_resultado = imagem_resultado.resize((40,40))
    imagem_resultado = ImageTk.PhotoImage(imagem_resultado)
    botao_resultado['image'] = imagem_resultado

# modificando as imagens
def escolher():
    escolha1 = botao_select1.get()
    escolha2 = botao_select2.get()

    if escolha1 == 'Homem' and escolha2 == 'Mulher':
        img_casal = 'imagens/casal3.png' 
        img_resultado = 'imagens/coracao2.png'
    elif escolha1 == 'Mulher' and escolha2 == 'Mulher':
        img_casal = 'imagens/casal2.png'
        img_resultado = 'imagens/coracao1.png' 
    elif escolha1 == 'Homem' and escolha2 == 'Homem':
        img_casal = 'imagens/casal1.png'
        img_resultado = 'imagens/coracao1.png'
    else:
        img_casal = 'imagens/casal3.png' 
        img_resultado = 'imagens/coracao2.png'

    abrir_imagens(img_resultado, img_casal)

def aleatorio():
    # quais numeros pode ter no valor final
    valor_final = '0123456789'
    # quantidade de digitos que vai ter no resultado
    digitos = 2
    resultado = "".join(sample(valor_final, digitos))
    return resultado

# mostrando os resultados do cálculo
def calcular_amor():
    nome1 = seu_nome.get()
    nome2 = nome_parceiro.get()
    porcentagem = aleatorio()

    mensagem['text'] = 'Porcentagem de amor entre:'
    casal_nome['text'] = f'{nome1}&{nome2}'
    porcentagem_amor['text'] = f'{porcentagem}%'


# criando a janela
janela = Tk()
janela.title("")
janela.geometry('510x500')
janela.configure(background=cor1)
janela.resizable(width=FALSE, height=FALSE) # impossibilita a alteração do tamanho da janela.

# adiciona um estilo a janela------------------------------------------
estilo = ttk.Style(janela)
estilo.theme_use('clam')

frame_cima = Frame(janela, width=510, height=250, bg=cor1)
frame_cima.grid(row=0, column=0)
frame_meio = Frame(janela, width=510, height=250, bg=cor1, relief='solid')
frame_meio.grid(row=1, column=0)

logo = Label(frame_cima, width=500, text='Calculadora de amor', font=('Fixedsys 25'), bg=cor7, fg=cor1, padx=80, anchor='nw')
logo.place(x=0, y=0)

# abrindo a imagem do casal--------------------------------------------
imagem_casal = Image.open('imagens/coracao3.png')
imagem_casal = imagem_casal.resize((170,170))
imagem_casal = ImageTk.PhotoImage(imagem_casal)

mostrar_imagem = Label(frame_cima, image=imagem_casal, width=950, compound=LEFT, bg=cor1, fg=cor4, padx=5, anchor='nw')
mostrar_imagem.place(x=20, y=60)

# mensagens de resultado do cálculo----------------------------------------
mensagem = Label(frame_cima, width=65, text='', padx=20, anchor='nw', font=('Verdana 12 bold '), bg=cor1, fg=cor0)
mensagem.place(x=180, y=80)

casal_nome = Label(frame_cima, width=20, text='', padx=1, anchor=CENTER, font=('Verdana 12 bold'), bg=cor1, fg=cor5)
casal_nome.place(x=220, y=110)

porcentagem_amor = Label(frame_cima, width=10, text='', padx=10, anchor=CENTER, font=('Verdana 25 bold'), bg=cor1, fg=cor0)
porcentagem_amor.place(x=220, y=150)

# entrada dos nomes-------------------------------------------------------
label_nome = Label(frame_meio, text='Seu nome', anchor=NW, font=('Ivy 12 bold'), bg=cor1, fg=cor0)
label_nome.place(x=6, y=1)

seu_nome = Entry(frame_meio, width=16, font=('Ivy 17'), justify='center', relief='solid')
seu_nome.place(x=10, y=30)

botao_select1 = StringVar()

radio1 = Radiobutton(frame_meio, command=escolher, text='Homem', bg=cor1, font=('Ivy 12'), value='Homem', variable=botao_select1)
radio1.place(x=10, y=75)

radio2 = Radiobutton(frame_meio, command=escolher, text='Mulher', bg=cor1, font=('Ivy 12'), value='Mulher', variable=botao_select1)
radio2.place(x=10, y=100)

linha_sep = Label(frame_meio, width=1, height=12, anchor=NW, font=('Verdana 1'), bg=cor5, fg=cor1)
linha_sep.place(x=237, y=30)
linha_sep = Label(frame_meio, width=1, height=12, anchor=NW, font=('Verdana 1'), bg=cor3, fg=cor1)
linha_sep.place(x=247, y=30)

l_parceiro = Label(frame_meio, text='Nome do(a) parceiro(a)', font=('Ivy 12 bold'), anchor=NW, bg=cor1, fg=cor0)
l_parceiro.place(x=265, y=1)

nome_parceiro = Entry(frame_meio, width=16, font=('Ivy 17'), justify='center', relief='solid')
nome_parceiro.place(x=269, y=30)

# botões para a escolha do gênero-----------------------------------------------
botao_select2 = StringVar()

radio3 = Radiobutton(frame_meio, command=escolher, text='Homem', bg=cor1, font=('Ivy 12'), value='Homem', variable=botao_select2)
radio3.place(x=269, y=75)

radio4 = Radiobutton(frame_meio, command=escolher, text='Mulher', bg=cor1, font=('Ivy 12'), value='Mulher', variable=botao_select2)
radio4.place(x=269, y=100)

# botão para calcular o resultado 
imagem_resultado = Image.open('imagens/coracao2.png') 
imagem_resultado = imagem_resultado.resize((40, 40))
imagem_resultado = ImageTk.PhotoImage(imagem_resultado)

botao_resultado = Button(frame_meio, command=calcular_amor, image=imagem_resultado, compound=LEFT, width=250, text='calcular amor'.upper(), anchor=CENTER, font=('Ivy 11'), bg=cor2, fg=cor1)
botao_resultado.place(x=120, y=160)

janela.mainloop()
