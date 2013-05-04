from Node import Node

class Name(Node):
    def __init__(self,identifier,expression=None, negative=False):
        self.identifier = identifier
        self.expression = expression
        self.negative   = negative

    def to_string(self):
        o = 'Name { '
        if self.negative:
            o += '-'
        o += self.identifier.to_string()
        o += ' '
        if self.expression:
            o += self.expression.to_string()
            o += ' '
        o += '}'
        return o

    def get_type(self,env):
        name_type = env.variables.get(self.identifier.token_content, env.global_variables.get(self.identifier.token_content,False))
        if name_type:
            return name_type
        else:
            raise TypeCheckException('Error Variable Not Found',self.identifier.line_num)
