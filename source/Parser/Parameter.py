from Node import Node

class Parameter(Node):
    def __init__(self,variable_decleration,IN):
        self.variable_decleration = variable_decleration
        self.IN = IN

    def to_string(self):
        o = 'Parameter: {'
        o += self.variable_decleration.to_string()
        o += ' in' if self.IN else ' out'
        o += ' }'
        return o
