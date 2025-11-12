import tkinter as tk
from tkinter import simpledialog, messagebox

from lexer import Lexer
from parser import Parser
from display_tree import dibujar_arbol

# Gramática, atributos y conjuntos
gramatica = """
E → E + T | E - T | T
T → T * F | T / F | F
F → ( E ) | num
"""

atributos = """
Atributos:
- valor: valor numérico
- tipo: 'int' o 'float'
- nodo: nodo del AST decorado
"""

F = {'num', '+', '-', '*', '/', '(', ')'}
S = 'E'
P = [
    'E → E + T',
    'E → E - T',
    'E → T',
    'T → T * F',
    'T → T / F',
    'T → F',
    'F → ( E )',
    'F → num'
]

ventana = tk.Tk()
ventana.title("Evaluador y Árbol Decorado de Expresiones Aritméticas")

def mostrar_texto(titulo, texto):
    vent = tk.Toplevel()
    vent.title(titulo)
    txt = tk.Text(vent, wrap='word')
    txt.insert('1.0', texto)
    txt.config(state='disabled')
    txt.pack(expand=True, fill='both')

def mostrar_gramatica():
    mostrar_texto("Gramática", gramatica)

def mostrar_atributos():
    mostrar_texto("Atributos", atributos)

def mostrar_conjuntos():
    conjuntos_texto = f"F (Terminales): {F}\nS (Inicial): {S}\nP (Producciones):\n  " + '\n  '.join(P)
    mostrar_texto("Conjuntos F, S, P", conjuntos_texto)

def evaluar_expresion():
    expr = simpledialog.askstring("Entrada", "Ingrese expresión aritmética:")
    if expr:
        try:
            lexer = Lexer(expr)
            parser = Parser(lexer)
            res = parser.parse()
            if parser.current_token is not None:
                messagebox.showerror("Error", "Expresión con tokens extra no procesados")
                return
            arbol_str = dibujar_arbol(res.nodo)
            mostrar_texto("Resultado y Árbol Decorado", f"Resultado: {res.valor}\n\nÁrbol decorado:\n{arbol_str}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

tk.Button(ventana, text="Mostrar Gramática", command=mostrar_gramatica).pack(fill='x')
tk.Button(ventana, text="Mostrar Atributos", command=mostrar_atributos).pack(fill='x')
tk.Button(ventana, text="Mostrar Conjuntos", command=mostrar_conjuntos).pack(fill='x')
tk.Button(ventana, text="Calcular Expresión", command=evaluar_expresion).pack(fill='x')

ventana.mainloop()
