from Node import Node

class ProgramHeader(Node):
    def __init__(self,identifier):
        self.identifier = identifier

    def to_string(self):
        return 'Program Header: { %s }' % self.identifier.to_string()
