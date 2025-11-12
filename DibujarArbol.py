def dibujar_arbol(nodo):
    def _display_aux(node):
        if len(node.hijos) == 0:
            line = f'{node.operador}({node.valor})'
            width = len(line)
            height = 1
            mid = width // 2
            return [line], width, height, mid

        if len(node.hijos) == 1:
            lines, n, p, x = _display_aux(node.hijos[0])
            s = f'{node.operador}({node.valor})'
            u = len(s)
            first_line = (x+1)*' ' + '_'*(n - x - 1) + s
            second_line = x*' ' + '/' + ' '*(n - x - 1 + u)
            lines = [line + u*' ' for line in lines]
            return [first_line, second_line] + lines, n + u, p + 2, n + u//2

        if len(node.hijos) == 2:
            l, n, p, x = _display_aux(node.hijos[0])
            r, m, q, y = _display_aux(node.hijos[1])
            s = f'{node.operador}({node.valor})'
            u = len(s)
            first_line = (x+1)*' ' + '_'*x + s + '_'*y
            second_line = x*' ' + '/' + ' '*(n - x - 1 + u + y) + '\\' + ' '*(m - y - 1)
            if p < q:
                l += [' ' * n] * (q - p)
            elif q < p:
                r += [' ' * m] * (p - q)
            lines = [first + ' ' * u + second for first, second in zip(l, r)]
            return [first_line, second_line] + lines, n + m + u, max(p, q) + 2, n + u // 2

        return [], 0, 0, 0

    lines, _, _, _ = _display_aux(nodo)
    return '\n'.join(lines)
