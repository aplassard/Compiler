from Node import Node
from TypeChecker import TypeCheckException

class Expression(Node):
    def __init__(self,arith_op,op=None,expression=None):
        self.arith_op = arith_op
        self.op       = op
        self.expression = expression

    def to_string(self):
        o = 'Expression: { '
        o += self.arith_op.to_string()
        if self.op:
            o += ' '
            o += self.op.token_type
            o += ' '
            o += self.expression.to_string()
        o += ' }'
        return o

    def get_type(self,env):
        arith_op_type = self.arith_op.get_type(env)
        if self.expression:
            expression_type = self.expression.get_type(env)
            if expression_type == arith_op_type:
                return expression_type
            else:
                raise TypeCheckException('Error Parsing Expression',self.op.line_num)
        return arith_op_type

    def get_line_number(self):
        if self.op:
            return self.op.line_number
        else:
            return self.arith_op.get_line_number()

    def generate_code(self,env):
        statements = []
        if self.expression:
            new_statements, final_register1 = self.expression.generate_code(self,env)
            statements.extend(new_statements)
            self.env.active_registers.add(final_register)
        new_statements, final_register2 = self.arith_op.generate_code(env)
        statements.extend(new_statements)
        if self.op:
            then_number = env.get_next_then()
            statements.append('if(R[%s] = true %s R[%s] = true) goto THEN%s;' % (final_register1,self.op.token_content,final_register2,then_number))
            final_register = final_register1 if final_register1 < final_register2 else final_register2
            statements.append('R[%s] = false;'%final_register)
            statements.append('THEN%s:')
            statements.append('\tR[%s] = true;'%final_register)
            env.active_registers.remove(final_register1)
            env.active_registers.remove(final_register2)
            env.active_registers.add(final_register)
        else:
            final_register = final_register2
        return statements,final_register


