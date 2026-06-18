
import tkinter as tk #me traiga a tkinter mas desde agora vamos chamar tk
janela = tk.Tk() #Tk dentro de tk, () signfica executar
janela.title("Meu TarefaLingo") #.title() mexer no titulo da nossa variavel 
caixa_de_texto = tk.Entry(janela)
caixa_de_texto.pack()