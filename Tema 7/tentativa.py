import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Funções de cálculo de juros
def calcular_juros_simples(principal, taxa_de_juros, tempo):
    return principal * (1 + (taxa_de_juros / 100) * tempo)

def calcular_juros_compostos(principal, taxa_de_juros, tempo):
    return principal * ((1 + (taxa_de_juros / 100)) ** tempo)

# Função que lida com a submissão dos dados e plotagem do gráfico
def calcular_e_plotar():
    p = float(principal_entry.get())
    r = float(taxa_de_juros_entry.get())
    t = int(tempo_entry.get())

    tempos = np.arange(t + 1)
    montantes_simples = [calcular_juros_simples(p, r, ano) for ano in tempos]
    montantes_compostos = [calcular_juros_compostos(p, r, ano) for ano in tempos]

    # Limpar gráfico anterior
    ax.clear()
    ax.plot(tempos, montantes_simples, label='Juros Simples')
    ax.plot(tempos, montantes_compostos, label='Juros Compostos')
    ax.set_title('Crescimento do Investimento ao Longo do Tempo')
    ax.set_xlabel('Tempo (anos)')
    ax.set_ylabel('Montante')
    ax.legend()
    canvas.draw()

# Interface gráfica
app = tk.Tk()
app.title("Calculadora de Juros com Gráficos")

# Widgets para entrada de dados
ttk.Label(app, text="Principal:").grid(column=0, row=0)
principal_entry = ttk.Entry(app)
principal_entry.grid(column=1, row=0)

ttk.Label(app, text="Taxa de Juros (%):").grid(column=0, row=1)
taxa_de_juros_entry = ttk.Entry(app)
taxa_de_juros_entry.grid(column=1, row=1)

ttk.Label(app, text="Tempo (anos):").grid(column=0, row=2)
tempo_entry = ttk.Entry(app)
tempo_entry.grid(column=1, row=2)

# Botão para calcular e plotar
calcular_button = ttk.Button(app, text="Calcular e Plotar", command=calcular_e_plotar)
calcular_button.grid(column=1, row=3)

# Área de gráfico
fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=app)
canvas_widget = canvas.get_tk_widget()
canvas_widget.grid(column=0, row=4, columnspan=2)

app.mainloop()
