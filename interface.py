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

logo = Label(frame_cima, width=500, text='Calculadora de amor', font=('Fixedsys 22'), bg=cor7, fg=cor1, padx=100, anchor='nw')
logo.place(x=0, y=0)

janela.mainloop()
