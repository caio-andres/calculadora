#Importando o tkinter, uma biblioteca gráfica padrão do Python, tornando possível criar a janela da calculadora
from tkinter import *
from tkinter import ttk

#Cores
brown = "#964b00"
bege = "#f5f5dc"
blue = "#0000FF"
green = "#008000"
loyalBlue = "#4169e1"
white = "#FFFFFF"
black = "#0F0F0F"
orange = "#FFA500"
yellow = "#FFFF00"

#Janela
janela = Tk()
janela.title("Calculadora")
janela.geometry("235x310")
janela.config(bg=blue)

frame_tela = Frame(janela, width=235, height=50, bg=black)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)

#Funções
input_atual = "" #Caracteres que estão na label no momento
resultado = 0 #Resultado final da conta

def pressionar_botao(number): #Faz o botão aparecer na label assim que clica em algum botão
    global input_atual #global é utilizado para se referenciar a uma variável fora do local
    input_atual += str(number) #str é utilizado para transformar um tipo em String
    atualizar_display() #Função criada para atualizar o display
    
def clear_display(): #Limpa o label
    global input_atual
    input_atual = "" #Declara que input_atual é vazio, ou seja, demos clear
    atualizar_display()

def calcular(): #Calcula o resultado dependendo dos operadores
    global input_atual, resultado
    try:
        expressao = input_atual.replace('x', '*') #replace serve para que, na hora de imprimir, o primeiro caractere chamado seja trocado pelo segundo

        if expressao[-1] in ['+', '-', '*', '/']: #Condição para a calculadora funcionar mesmo se tiver mais algum operador depois da conta não finalizada (ex: 9+9+=18)
            expressao = expressao[:-1]

        if '%' in expressao: #Condição para criar a conta da porcentagem, já que em Python não há um cálculo automático para o operador "%"
            numero_sem_porcentagem = expressao.split('%')
            numero = float(numero_sem_porcentagem[0])
            porcentagem = float(numero_sem_porcentagem[1])
            resultado = (numero * porcentagem) / 100

        else: #Caso contrário, o resultado será imprimido (no caso de qualquer operador, menos o "%")
            resultado = str(eval(expressao))

        input_atual = resultado #No final, o input_atual se tornará no resultado, ou seja: o resultado aparecerá na label da calculadora
        atualizar_display()

    except Exception as e: #Exceção criada caso dê algum erro de sintaxe e etc
        input_atual = "Deu ruim" #Mensagem que aparecerá em caso de erro
        atualizar_display()

def atualizar_display(): #Função criada para atualizar o display, ou seja, o que aparece na label
    valor_texto.set(input_atual) #valor_texto foi criado para converter qualquer operador para o tipo String

#Label
valor_texto = StringVar() #Criando uma variável do tipo String para os operadores serem impressos na label

app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18'), bg=black, fg=white)
app_label.place(x=0, y=0)

#Botões
#Primeira coluna
clean = Button(frame_corpo, text="C", width=11, height=2, font=('Ivy 13 bold'), fg=yellow, relief=RAISED, overrelief=RIDGE, bg=loyalBlue)
clean.place(x=0, y=0)
clean.config(command=clear_display)

percentage = Button(frame_corpo, text="%", width=5, height=2, font=('Ivy 13 bold'), fg=yellow, relief=RAISED, overrelief=RIDGE, bg=loyalBlue)
percentage.place(x=118, y=0)
percentage.config(command=lambda: pressionar_botao("%"))

division = Button(frame_corpo, text="/", width=5, height=2, font=('Ivy 13 bold'), fg=loyalBlue, relief=RAISED, overrelief=RIDGE, bg=yellow)
division.place(x=177, y=0)
division.config(command=lambda: pressionar_botao("/"))

#Segunda coluna
seven = Button(frame_corpo, text="7", width=5, height=2, font=('Ivy 13 bold'), fg=yellow, relief=RAISED, overrelief=RIDGE, bg=loyalBlue)
seven.place(x=0, y=52)
seven.config(command=lambda: pressionar_botao("7"))

eight = Button(frame_corpo, text="8", width=5, height=2, font=('Ivy 13 bold'), fg=yellow, relief=RAISED, overrelief=RIDGE, bg=loyalBlue)
eight.place(x=59, y=52)
eight.config(command=lambda: pressionar_botao("8"))

nine = Button(frame_corpo, text="9", width=5, height=2, font=('Ivy 13 bold'), fg=yellow, relief=RAISED, overrelief=RIDGE, bg=loyalBlue)
nine.place(x=118, y=52)
nine.config(command=lambda: pressionar_botao("9"))

multiplication = Button(frame_corpo, text="x", width=5, font=('Ivy 13 bold'), height=2, fg=loyalBlue, relief=RAISED, overrelief=RIDGE, bg=yellow)
multiplication.place(x=177, y=52)
multiplication.config(command=lambda: pressionar_botao("x"))

#Terceira coluna
four = Button(frame_corpo, text="4", width=5, height=2, font=('Ivy 13 bold'), fg=yellow, relief=RAISED, overrelief=RIDGE, bg=loyalBlue)
four.place(x=0, y=104)
four.config(command=lambda: pressionar_botao("4"))

five = Button(frame_corpo, text="5", width=5, height=2, font=('Ivy 13 bold'), fg=yellow, relief=RAISED, overrelief=RIDGE, bg=loyalBlue)
five.place(x=59, y=104)
five.config(command=lambda: pressionar_botao("5"))

six = Button(frame_corpo, text="6", width=5, height=2, font=('Ivy 13 bold'), fg=yellow, relief=RAISED, overrelief=RIDGE, bg=loyalBlue)
six.place(x=118, y=104)
six.config(command=lambda: pressionar_botao("6"))

subtraction = Button(frame_corpo, text="-", width=5, font=('Ivy 13 bold'), height=2, fg=loyalBlue, relief=RAISED, overrelief=RIDGE, bg=yellow)
subtraction.place(x=177, y=104)
subtraction.config(command=lambda: pressionar_botao("-"))

#Quarta coluna
one = Button(frame_corpo, text="1", width=5, height=2, font=('Ivy 13 bold'), fg=yellow, relief=RAISED, overrelief=RIDGE, bg=loyalBlue)
one.place(x=0, y=156)
one.config(command=lambda: pressionar_botao("1"))

two = Button(frame_corpo, text="2", width=5, height=2, font=('Ivy 13 bold'), fg=yellow, relief=RAISED, overrelief=RIDGE, bg=loyalBlue)
two.place(x=59, y=156)
two.config(command=lambda: pressionar_botao("2"))

three = Button(frame_corpo, text="3", width=5, height=2, font=('Ivy 13 bold'), fg=yellow, relief=RAISED, overrelief=RIDGE, bg=loyalBlue)
three.place(x=118, y=156)
three.config(command=lambda: pressionar_botao("3"))

addition = Button(frame_corpo, text="+", width=5, font=('Ivy 13 bold'), height=2, fg=loyalBlue, relief=RAISED, overrelief=RIDGE, bg=yellow)
addition.place(x=177, y=156)
addition.config(command=lambda: pressionar_botao("+"))

#Última coluna
zero = Button(frame_corpo, text="0", width=11, height=2, font=('Ivy 13 bold'), fg=yellow, relief=RAISED, overrelief=RIDGE, bg=loyalBlue)
zero.place(x=0, y=208)
zero.config(command=lambda: pressionar_botao("0"))

point = Button(frame_corpo, text=".", width=5, height=2, font=('Ivy 13 bold'), fg=yellow, relief=RAISED, overrelief=RIDGE, bg=loyalBlue)
point.place(x=118, y=208)
point.config(command=lambda: pressionar_botao("."))

equal = Button(frame_corpo, text="=", width=5, height=2, font=('Ivy 13 bold'), fg=loyalBlue, relief=RAISED, overrelief=RIDGE, bg=yellow)
equal.place(x=177, y=208)
equal.config(command=calcular)

#Abrindo a janela
janela.mainloop()
