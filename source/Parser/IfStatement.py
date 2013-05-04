from Node import Node

class IfStatement(Node):
    def __init__(self,expression,then_statements,else_statements):
        self.expression = expression
        self.then_statements = then_statements
        self.else_statements = else_statements

    def to_string(self):
        o = 'IfStatement: {'
        o += self.expression.to_string()
        o += ' ThenStatements: { '
        for statement in self.then_statements:
            o += statement.to_string()
            o += ', '
        o += ' }'
        o += ' ElseStatements: { '
        for statement in self.else_statements:
            o += statement.to_string()
            o += ', '
        o += ' } }'
        return o
