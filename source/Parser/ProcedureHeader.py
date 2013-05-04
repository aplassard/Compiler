from Node import Node

class ProcedureHeader(Node):
    def __init__(self,identifier,parameter_list):
        self.identifier = identifier
        self.parameter_list = parameter_list

    def to_string(self):
        o = 'Procedure Header: {'
        o += self.identifier.to_string()
        o += ' '
        o += self.parameter_list.to_string()
        o += ' }'
        return o
