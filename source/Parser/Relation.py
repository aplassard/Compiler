from Node import Node
from TypeChecker.TypeCheckException import TypeCheckException

class Relation(Node):
    def __init__(self,term,op=None,relation=None):
        self.term = term
        self.op   = op
        self.relation = relation

    def to_string(self):
        o = 'Relation: {'
        o += self.term.to_string()
        if self.op:
            o += ' '
            o += self.op.token_content
            o += ' '
            o += self.relation.to_string()
        o += ' }'
        return o

    def get_type(self,env):
        term_type = self.term.get_type(env)
        if term_type in NUMBER_TYPES:
            term_type = 'NUMBER'
        if self.op:
            relation_type = self.relation.get_type(env)
            if type( relation_type ) == tuple:
                relation_type = relation_type[1]
            if relation_type in NUMBER_TYPES:
                relation_type = 'NUMBER'
            if relation_type == term_type:
                return 'BOOLEAN','NUMBER'
            else:
                raise TypeCheckException('Relation Type Checking Failed',self.op.line_number)
        return term_type

    def get_line_number(self):
        if self.op:
            return self.op.line_number
        else:
            return self.term.get_line_number()

    def generate_code(self,env):
        statements = []
        if self.relation:
            new_statements, final_register1 = self.relation.generate_code(env)
            statements.extend(new_statements)
        new_statements, final_register2 = self.term.generate_code(env)
        statements.extend(new_statements)
        if self.op:
            final_register = final_register1 if final_register1 < final_register2 else final_register2
            then_number = env.get_next_then()
            statements.append('if (R[%s] %s R[%s]) goto THEN%s ;' % (final_register1, self.op.token_content, final_register2, then_number))
            statements.append('R[%s] = false; ' % final_register)
            statements.append('THEN%s:' % then_number)
            statements.append('\tR[%s] = true ;' % final_register)
            env.active_registers.remove(final_register1)
            env.active_registers.remove(final_register2)
            env.active_registers.add(final_register)
        else:
            final_register = final_register2
        return statements,final_register

NUMBER_TYPES = ["NUMBER","INTEGER","FLOAT"]
RELATIONS = ["LESS_THAN","GREATER_THAN","LESS_THAN_EQUAL","GREATER_THAN_EQUAL","NOT_EQUAL","EQUAL",]
