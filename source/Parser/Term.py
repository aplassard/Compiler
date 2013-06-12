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

    def generate_code(self,env):
        statements = []
        if self.term:
            new_statements,final_register1 = self.term.generate_code(env)
            statements.extend(new_statements)
        new_statements, final_register2 = self.factor.generate_code(env)
        statements.extend(new_statements)
        if self.op:
            final_register = final_register1 if final_register1 < final_register2 else final_register2
            statements.append('R[%s] = R[%s] %s R[%s] ;' % (final_register, final_register1, self.op.token_content,final_register2))
            env.active_registers.remove(final_register1)
            env.active_registers.remove(final_register2)
            env.active_registers.add(final_register)
        else:
            final_register = final_register2
        return statements, final_register


