class NodoAST:
    def __init__(self, operador, hijos=None, valor=None, tipo=None):
        self.operador = operador
        self.hijos = hijos or []
        self.valor = valor
        self.tipo = tipo

    def to_str(self, nivel=0):
        s = '  ' * nivel + f"{self.operador} (valor={self.valor}, tipo={self.tipo})"
        for h in self.hijos:
            s += '\n' + h.to_str(nivel + 1)
        return s

def tipo_compatible(t1, t2):
    if 'float' in (t1, t2):
        return 'float'
    return 'int'
