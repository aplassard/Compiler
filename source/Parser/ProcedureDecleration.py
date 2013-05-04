from Node import Node

class ProcedureDecleration(Node):
    def __init__(self,procedure_header,procedure_body,GLOBAL=False):
        self.procedure_header = procedure_header
        self.procedure_body   = procedure_body
        self.GLOBAL = GLOBAL

    def to_string(self):
        o = 'Procedure Decleration: {'
        o += self.procedure_header.to_string()
        o += ' '
        o += self.procedure_body.to_string()
        o += ' }'
        return o
