from Node import Node

class LoopStatement(Node):
    def __init__(self,assignment_statement,expression,statements):
        self.assignment_statement = expression
        self.expression = expression
        self.statements = statements

    def to_string(self):
        o = 'LoopStatement: { '
        o += self.assignment_statement.to_string()
        o += ' '
        o += self.expression.to_string()
        o += ' Statements: {'
        for statement in self.statements:
            o += statement.to_string()
            o += ', '
        o += ' } }'
        return o
