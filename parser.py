import re
from types import SimpleNamespace
from lexer import Lexer
from ast import NodoAST, tipo_compatible
from DibujarArbol import dibujar_arbol

class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.next_token()

    def eat(self, token):
        if self.current_token == token:
            self.current_token = self.lexer.next_token()
        else:
            raise SyntaxError(f"Se esperaba {token} pero se encontró {self.current_token}")

    def parse(self):
        return self.parse_E()

    def parse_E(self):
        node = self.parse_T()
        while self.current_token in ('+', '-'):
            op = self.current_token
            self.eat(op)
            right = self.parse_T()
            valor = node.valor + right.valor if op=='+' else node.valor - right.valor
            tipo = tipo_compatible(node.tipo, right.tipo)
            node = SimpleNamespace(
                valor=valor,
                tipo=tipo,
                nodo=NodoAST(op, [node.nodo, right.nodo], valor, tipo)
            )
        return node

    def parse_T(self):
        node = self.parse_F()
        while self.current_token in ('*', '/'):
            op = self.current_token
            self.eat(op)
            right = self.parse_F()
            valor = node.valor * right.valor if op=='*' else node.valor / right.valor
            tipo = tipo_compatible(node.tipo, right.tipo)
            node = SimpleNamespace(
                valor=valor,
                tipo=tipo,
                nodo=NodoAST(op, [node.nodo, right.nodo], valor, tipo)
            )
        return node

    def parse_F(self):
        if self.current_token == '(':
            self.eat('(')
            node = self.parse_E()
            self.eat(')')
            return node
        elif re.match(r'\d+(\.\d+)?', self.current_token):
            valor = float(self.current_token) if '.' in self.current_token else int(self.current_token)
            tipo = 'float' if isinstance(valor, float) else 'int'
            token = self.current_token
            self.eat(token)
            nodo = NodoAST('num', valor=valor, tipo=tipo)
            return SimpleNamespace(valor=valor, tipo=tipo, nodo=nodo)
        else:
            raise SyntaxError(f"Token inesperado: {self.current_token}")
