from lexer import Lexer
from parser import Parser
from DibujarArbol import dibujar_arbol

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

def mostrar_gramatica():
    print("\n" + gramatica + "\n")

def mostrar_atributos():
    print("\n" + atributos + "\n")

def mostrar_conjuntos():
    print(f"\nF (Terminales): {F}")
    print(f"S (Inicial): {S}")
    print("P (Producciones):")
    for p in P:
        print(f"  {p}")
    print()

def evaluar_expresion():
    expr = input("Ingrese expresión aritmética: ")
    try:
        lexer = Lexer(expr)
        parser = Parser(lexer)
        res = parser.parse()
        if parser.current_token is not None:
            print("Error: Expresión con tokens extra no procesados")
            return
        arbol_str = dibujar_arbol(res.nodo)
        print(f"\nResultado: {res.valor}\n")
        print("Árbol decorado:")
        print(arbol_str)
        print()
    except Exception as e:
        print(f"Error: {e}\n")

def menu():
    while True:
        print("\n--- Menú ---")
        print("1. Mostrar Gramática")
        print("2. Mostrar Atributos")
        print("3. Mostrar Conjuntos F, S, P")
        print("4. Calcular Expresión")
        print("5. Salir")
        opcion = input("Seleccione una opción (1-5): ")
        if opcion == '1':
            mostrar_gramatica()
        elif opcion == '2':
            mostrar_atributos()
        elif opcion == '3':
            mostrar_conjuntos()
        elif opcion == '4':
            evaluar_expresion()
        elif opcion == '5':
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
