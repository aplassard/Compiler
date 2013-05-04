from Node import Node

class Program(Node):
    def __init__(self,program_header,program_body):
        self.program_header = program_header
        self.program_body   = program_body

    def to_string(self):
        o = 'Program: { '
        o += self.program_header.to_string()
        o += ' '
        o += self.program_body.to_string()
        o += ' }'
        return o

