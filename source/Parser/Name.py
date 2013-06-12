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
        name_type = env.variables.get(self.identifier.identifier.token_content, env.global_variables.get(self.identifier.identifier.token_content,False))
        if type(name_type)==bool:
            return 'BOOLEAN'
        name_type = name_type.type_mark.token_type
        if name_type:
            name_type = 'NUMBER' if name_type in ['INTEGER','FLOAT'] else name_type
            return name_type
        else:
            raise TypeCheckException('Error Variable Not Found',self.identifier.line_num)

    def get_line_number(self):
        return self.identifier.line_number

    def generate_code(self,env):
        statements = []
        if self.expression:
            new_statements,final_register1 = self.expression.generate_code(env)
            self.statements.extend(new_statements)
        next_register = env.get_next_register()
        statements.append('R[%s] = MM[%s%s]' % (next_register, env.get_mem_location(self.identifier.identifier.token_content), ('' if not self.expression else '8*R[%s]'%final_register1)))
        return statements,next_register
