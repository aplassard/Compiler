from Node import Node

class AssignmentStatement(Node):
    def __init__(self,destination,expression):
        self.destination = destination
        self.expression  = expression

    def to_string(self):
        o = 'Assignment_Statement {'
        o += self.destination.to_string()
        o += ' '
        o += self.expression.to_string()
        o += ' }'
        return o

    def generate_code(self,env):
        final_location = env.get_mem_location(self.destination.identifier.identifier.token_content)
        statements,final_register = self.expression.generate_code(env)
        statements.append('MM[%s] = R[%s]' % (final_location,final_register))
        env.active_registers.remove(final_register)
        return statements, final_register

