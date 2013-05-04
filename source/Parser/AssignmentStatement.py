from Node import Node

class AssignmentStatement(Node):
    def __init__(self,destination,expression):
        self.destination = destination
        self.expression  = expression

    def to_string(self):
        o = 'Assignment_Statement {'
        o += self.destination.to_string()
        o += ' '
        o += self.expression.to_string()
        o += ' }'
        return o
