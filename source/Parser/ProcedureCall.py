from Node import Node

class ProcedureCall(Node):
    def __init__(self,identifier,argument_list):
        self.identifier = identifier
        self.argument_list = argument_list

    def to_string(self):
        o = 'Procedure Call: { '
        o += self.identifier.to_string()
        o += ' '
        o += self.argument_list.to_string()
        o += ' }'
        return o
