from Node import Node

class ProcedureBody(Node):
    def __init__(self,declerations,statements):
        self.declerations = declerations
        self.statements   = statements

    def to_string(self):
        o = 'Procedure Body { '
        o += 'Declerations: { '
        for dec in self.declerations:
            o += dec.to_string()
            o += ', '
        o += '} Statements: { '
        for stat in self.statements:
            o += stat.to_string()
            o += ', '
        o += '} }'
        return o
