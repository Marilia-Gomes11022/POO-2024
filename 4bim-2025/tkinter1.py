from tkinter import *
import tkinter
from datetime import datetime

#cores

cor1 = '#000000' #preto 
cor2 = '#fafcff' #branco
cor3 = '#21c25c' #verde
cor4 = '#e50914' #vermelho
cor5 = '#dedcdc' #cinza
cor6 = '#3080f0' #azul
cor7 = '#9415e8' #roxo



fundo = cor1 
cor = cor7

janela = Tk()
janela.title('Relógio Digital')
janela.geometry("440x180")
janela.resizable(width=FALSE, height = FALSE)
janela.configure(bg = cor1)

def relogio():
    tempo = datetime.now()
    hora = tempo.strftime("%H:%M:%S")
    dia_semana = tempo.strftime("%A")
    dia = tempo.strftime("%d")
    mes = tempo.strftime("%b") #B maiusculo "Janeiro"; b minusculo "Jan"
    ano = tempo.strftime("%Y")

l1 = Label(janela, font=("Arial 80"), bg = fundo, fg = cor)
l1.grid(row = 0, column = 0, sticky = NW, padx=5)
relogio()

janela.mainloop()
