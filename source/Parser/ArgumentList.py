from Node import Node

class ArgumentList(Node):
    def __init__(self,expression,argument_list=None):
        self.expression = expression
        self.argument_list = argument_list

    def to_string(self):
        o = 'Argument_List { '
        o += self.expression.to_string()
        if self.argument_list:
            o += ' '
            o += self.argument_list.to_string()
            o += ' '
        o += '}'
        return o

