from tkinter import *
from tkinter import ttk

cor1 = "#4C7972"   # VERDE
cor2 = "#915A3C"   # MARROM
cor3 = "#CFB79F"   # BEGE
cor4 = "#E8E6E7"   # bege claro
cor5 = "#FFAB40"   # Laranja escuro
cor6 = "#feffff"   # Branca
cor7 = "#ECEFF1"   # Cinzenta

janela =Tk()
janela.title("Calculadora")
janela.geometry("235x314")
janela.config(bg=cor1)

#Criando frames
frame_tela = Frame(janela, width=235, height=50, bg=cor3,)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)


todos_valores = ''

#Criando Label
valor_text = StringVar()

#Criando Função
def incluir_valores(event):
    global todos_valores
    todos_valores = todos_valores + str(event)


    #Passando valor para Label(tela)
    valor_text.set(todos_valores)

#Função para calcular
def calcular():
    global todos_valores
    resultado = eval(todos_valores)

    valor_text.set(str(resultado))

#Função Limpar tela
def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_text.set("")


app_label = Label(frame_tela, textvariable=valor_text, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18'), bg=cor4, fg=cor2)

app_label.place(x=0,y=0)

bt_1 = Button(frame_corpo, command=lambda:incluir_valores('M+'),text="M+", width=4, height=2, bg=cor7, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt_1.place(x=0, y=0)

bt_2 = Button(frame_corpo, command=lambda:incluir_valores('%'), text="%", width=4, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt_2.place(x=52, y=0)

bt_3 = Button(frame_corpo, command=lambda:incluir_valores('/'),text="/", width=4, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt_3.place(x=104, y=0)

bt_4 = Button(frame_corpo, command=limpar_tela, text="C", width=7, height=2, bg=cor1, fg=cor6, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt_4.place(x=156, y=0)

bt_5 = Button(frame_corpo, command=lambda:incluir_valores('7'),text="7", width=4, height=2, bg=cor7, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt_5.place(x=0, y=53)

bt_6 = Button(frame_corpo, command=lambda:incluir_valores('8'),text="8", width=4, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt_6.place(x=52, y=53)

bt_7 = Button(frame_corpo, command=lambda:incluir_valores('9'),text="9", width=4, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt_7.place(x=104, y=53)

bt_8 = Button(frame_corpo, command=lambda:incluir_valores('+'),text="+", width=7, height=2, bg=cor1, fg=cor6, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt_8.place(x=156, y=53)

bt_9 = Button(frame_corpo, command=lambda:incluir_valores('4'),text="4", width=4, height=2, bg=cor7, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt_9.place(x=0, y=106)

bt_10 = Button(frame_corpo, command=lambda:incluir_valores('5'),text="5", width=4, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt_10.place(x=52, y=106)

bt_11 = Button(frame_corpo, command=lambda:incluir_valores('6'),text="6", width=4, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt_11.place(x=104, y=106)

bt_12 = Button(frame_corpo, command=lambda:incluir_valores('-'),text="-", width=7, height=2, bg=cor1, fg=cor6, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt_12.place(x=156, y=106)

bt_13 = Button(frame_corpo, command=lambda:incluir_valores('1'),text="1", width=4, height=2, bg=cor7, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt_13.place(x=0, y=159)

bt_14 = Button(frame_corpo, command=lambda:incluir_valores('2'),text="2", width=4, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt_14.place(x=52, y=159)

bt_15 = Button(frame_corpo, command=lambda:incluir_valores('3'),text="3", width=4, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt_15.place(x=104, y=159)

bt_16 = Button(frame_corpo, command=lambda:incluir_valores('*'),text="*", width=7, height=2, bg=cor1, fg=cor6, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt_16.place(x=156, y=159)

bt_17 = Button(frame_corpo, command=lambda:incluir_valores('&'),text="&", width=4, height=2, bg=cor7, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt_17.place(x=0, y=211)

bt_18 = Button(frame_corpo, command=lambda:incluir_valores('0'),text="0", width=4, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt_18.place(x=52, y=211)

bt_19 = Button(frame_corpo, command=lambda:incluir_valores(','),text=",", width=4, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt_19.place(x=104, y=211)

bt_20 = Button(frame_corpo, command=calcular,text="=", width=7, height=2, bg=cor1, fg=cor6, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt_20.place(x=156, y=211)



janela.mainloop()