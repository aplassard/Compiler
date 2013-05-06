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

    def __len__(self):
        if not self.argument_list: return 1
        else: return 1 + len(self.argument_list)

    def __call__(self,n):
        return self.expression if n==0 else self.argument_list(n-1)
