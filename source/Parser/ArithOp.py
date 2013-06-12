from Node import Node
from TypeChecker.TypeCheckException import TypeCheckException

class ArithOp(Node):
    def __init__(self,relation,op=None,arith_op=None):
        self.relation = relation
        self.op       = op
        self.arith_op = arith_op

    def to_string(self):
        o = 'Arith_Op {'
        o += self.relation.to_string()
        if self.op:
            o += ' '
            o += self.op.token_type
            o += ' '
            o += self.arith_op.to_string()
        o += ' }'
        return o

    def get_type(self,env):
        relation_type = self.relation.get_type(env)
        if type(relation_type) == tuple:
            relation_type = relation_type[0]
        if self.arith_op:
            arith_op_type = self.arith_op.get_type(env)
            if arith_op_type == 'NUMBER' and relation_type == 'NUMBER':
                return 'NUMBER'
            else:
                raise TypeCheckException('Arithmetic operation did not type check.  Arith_Op Type was found to be %s and Relation Type was found to be %s' % (arith_op_type,relation_type,),self.op.line_number)
        return relation_type

    def get_line_number(self):
        if self.op:
            return self.op.line_number
        else:
            return self.relation.get_line_number()

    def generate_code(self,env):
        statements = []
        if self.arith_op:
            new_statements, final_register1 = self.arith_op.generate_code(env)
            statements.extend(new_statements)
        new_statements, final_register2 = self.relation.generate_code(env)
        statements.extend(new_statements)
        if self.op:
            final_register = final_register1 if final_register1 < final_register2 else final_register2
            statements.append('R[%s] = R[%s] %s R[%s] ;' % (final_register,final_register1,self.op.token_content,final_register2))
            env.active_registers.remove(final_register1)
            env.active_registers.remove(final_register2)
            env.active_registers.add(final_register)
        else:
            final_register = final_register2
        return statements, final_register


