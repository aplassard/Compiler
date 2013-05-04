from Node import Node

class Destination(Node):
    def __init__(self,identifier,expression=None):
        self.identifier = identifier
        self.expression = expression

    def to_string(self):
        o = 'Destination { '
        o += self.identifier.to_string()
        if self.expression:
            o += ' '
            o += self.expression.to_string()
        o += ' }'
        return o

