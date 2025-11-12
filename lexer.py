import re

class Lexer:
    def __init__(self, text):
        self.tokens = re.findall(r'\d+\.\d+|\d+|[()+\-*/]', text)
        self.pos = 0

    def next_token(self):
        if self.pos < len(self.tokens):
            tok = self.tokens[self.pos]
            self.pos += 1
            return tok
        return None

    def peek(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None
