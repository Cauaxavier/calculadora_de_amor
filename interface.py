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

frame_baixo = Frame(janela, width=510, height=250, bg=cor1, relief='solid')
frame_baixo.grid(row=1, column=0)

logo = Label(frame_cima, width=500, text='Calculadora de amor', font=('Fixedsys 25'), bg=cor7, fg=cor1, padx=80, anchor='nw')
logo.place(x=0, y=0)

imagem = Image.open('imagens/coracao3.png')
imagem = imagem.resize((150,150))
imagem = ImageTk.PhotoImage(imagem)

mostrar_imagem = Label(frame_cima, image=imagem, width=950, compound=LEFT, bg=cor1, fg=cor4, padx=5, anchor='nw')
mostrar_imagem.place(x=20, y=60)

msg = 'porcentagem de amor entre'
resultado1 = Label(frame_cima, width=65, text=msg, padx=20, anchor='nw', font='Verdana 12 bold ', bg=cor1, fg=cor0)
resultado1.place(x=180, y=80)

resultado2 = Label(frame_cima, width=25, text='resultado', padx=1, anchor=CENTER, font='Verdana 12 bold', bg=cor1, fg=cor5)
resultado2.place(x=180, y=110)

resultado3 = Label(frame_cima, width=10, text='95%', padx=10, anchor=CENTER, font='Verdana 25 bold', bg=cor1, fg=cor0)
resultado3.place(x=220, y=150)

janela.mainloop()
