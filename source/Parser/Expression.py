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

