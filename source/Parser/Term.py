from Node import Node
from TypeChecker.TypeCheckException import TypeCheckException

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
        if self.term:
            term_type = self.term.get_type(env)
            if term_type == factor_type:
                return term_type
            else:
                raise TypeCheckException('Error Type Checking Term.  Term type was found to be %s and factor type was found to be %s' % (term_type,factor_type,),self.op.line_number)
        return factor_type

    def get_line_number(self):
        if self.op:
            return self.op.line_number
        else:
            return self.factor.get_line_number()

