from Node import Node

class Term(Node):
    def __init__(self,factor,op=None,term=None):
        self.factor = factor
        self.op     = op
        self.term   = term

    def to_string(self):
        o = 'Term: { '
        o += self.factor.to_string()
        if self.op:
            o += self.op.token_type
            o += ' '
            o += self.term.to_string()
        o += ' }'
        return o

    def get_type(self,env):
        factor_type = self.factor.get_type(env)
        if term:
            term_type = self.term.get_type(env)
            if term_type == factor_type:
                return term_type
            else:
                raise TypeCheckException('Error Type Checking Term',self.op.line_number)
        return factor_type


