from tkinter import *
from tkinter import Tk, ttk
from PIL import Image, ImageTk

cor0 = "#2e2d2b" # Preto
cor1 = "#feffff" # Branco
cor2 = "#4fa882" # verde 
cor3 = "#38576b" # cor do valor
cor4 = "#403d3d" # cor da letra
cor5 = "#e06636" # - profit
cor6 = "#038cfc" # azul
cor7 = "#3fbfb9" # verde

# criando a janela
janela = Tk()
janela.title("")
janela.geometry('510x500')
janela.configure(background=cor1)
janela.resizable(width=FALSE, height=FALSE) # impossibilita a alteração do tamanho da janela.

# adiciona um estilo a janela.
estilo = ttk.Style(janela)
estilo.theme_use('clam')

frame_cima = Frame(janela, width=510, height=250, bg=cor1)
frame_cima.grid(row=0, column=0)
frame_meio = Frame(janela, width=510, height=250, bg=cor1, relief='solid')
frame_meio.grid(row=1, column=0)

logo = Label(frame_cima, width=500, text='Calculadora de amor', font=('Fixedsys 25'), bg=cor7, fg=cor1, padx=80, anchor='nw')
logo.place(x=0, y=0)

imagem = Image.open('imagens/coracao3.png')
imagem = imagem.resize((150,150))
imagem = ImageTk.PhotoImage(imagem)

mostrar_imagem = Label(frame_cima, image=imagem, width=950, compound=LEFT, bg=cor1, fg=cor4, padx=5, anchor='nw')
mostrar_imagem.place(x=20, y=60)

mensagem = Label(frame_cima, width=65, text='resultado', padx=20, anchor='nw', font=('Verdana 12 bold '), bg=cor1, fg=cor0)
mensagem.place(x=180, y=80)

casal_nome = Label(frame_cima, width=25, text='resultado', padx=1, anchor=CENTER, font=('Verdana 12 bold'), bg=cor1, fg=cor5)
casal_nome.place(x=180, y=110)

porcentagem_amor = Label(frame_cima, width=10, text='95%', padx=10, anchor=CENTER, font=('Verdana 25 bold'), bg=cor1, fg=cor0)
porcentagem_amor.place(x=220, y=150)

label_nome = Label(frame_meio, text='Seu nome', anchor=NW, font=('Ivy 12 bold'), bg=cor1, fg=cor0)
label_nome.place(x=6, y=1)

seu_nome = Entry(frame_meio, width=16, font=('Ivy 17'), justify='center', relief='solid')
seu_nome.place(x=10, y=30)

botao_select1 = StringVar()

radio1 = Radiobutton(frame_meio, text='Homem', bg=cor1, font=('Ivy 12'), value='Homem', variable=botao_select1)
radio1.place(x=10, y=75)

radio2 = Radiobutton(frame_meio, text='Mulher', bg=cor1, font=('Ivy 12'), value='Mulher', variable=botao_select1)
radio2.place(x=10, y=100)

linha_sep = Label(frame_meio, width=1, height=12, anchor=NW, font=('Verdana 1'), bg=cor5, fg=cor1)
linha_sep.place(x=235, y=30)
linha_sep = Label(frame_meio, width=1, height=12, anchor=NW, font=('Verdana 1'), bg=cor3, fg=cor1)
linha_sep.place(x=245, y=30)

l_parceiro = Label(frame_meio, text='Nome do parceiro', font=('Ivy 12 bold'), anchor=NW, bg=cor1, fg=cor0)
l_parceiro.place(x=265, y=1)

nome_parceiro = Entry(frame_meio, width=16, font=('Ivy 17'), justify='center', relief='solid')
nome_parceiro.place(x=265, y=30)

botao_select2 = StringVar()

radio3 = Radiobutton(frame_meio, text='Homem', bg=cor1, font=('Ivy 12'), value='Homem', variable=botao_select2)
radio3.place(x=265, y=75)

radio4 = Radiobutton(frame_meio, text='Mulher', bg=cor1, font=('Ivy 12'), value='Mulher', variable=botao_select2)
radio4.place(x=265, y=100)

janela.mainloop()
