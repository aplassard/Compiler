from Node import Node

class VariableDecleration(Node):
    def __init__(self,type_mark,identifier,array_size=None,GLOBAL=False):
        self.type_mark = type_mark
        self.identifier = identifier
        self.array_size = array_size
        self.GLOBAL = GLOBAL

    def to_string(self):
        o = 'Variable Decleration: { '
        if self.GLOBAL:
            o += 'GLOBAL '
        o += self.type_mark.to_string()
        o += ' '
        o += self.identifier.to_string()
        if self.array_size:
            o += ' '
            o += self.array_size.to_string()
        o += ' }'
        return o
