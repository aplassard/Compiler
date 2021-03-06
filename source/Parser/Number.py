from Node import Node

class Number(Node):
    def __init__(self,number,negative=False):
        self.number = number
        self.negative = negative

    def to_string(self):
        o = 'Number: { '
        if self.negative:
            o += '-'
        o += self.number.token_content
        o += ' }'
        return o

    def get_type(self,env):
        return 'NUMBER'

    def get_line_number(self):
        return self.number.line_number

    def generate_code(self,env):
        final_register = env.get_next_register()
        statements = ['R[%s] = %s%s' % (final_register, '' if not self.negative else '-',self.number.token_content)]
        return statements, final_register
