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
        if self.op:
            relation_type = self.relation.get_type(env)
            if type( relation_type ) == tuple:
                relation_type = relation_type[1]
            if relation_type == term_type:
                return 'BOOLEAN',relation_type
            else:
                raise TypeCheckException('Relation Type Checking Failed',self.op.line_number)
        return term_type


RELATIONS = ["LESS_THAN","GREATER_THAN","LESS_THAN_EQUAL","GREATER_THAN_EQUAL","NOT_EQUAL","EQUAL",]
