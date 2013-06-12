from Node import Node

class LoopStatement(Node):
    def __init__(self,assignment_statement,expression,statements):
        self.assignment_statement = expression
        self.expression = expression
        self.statements = statements

    def to_string(self):
        o = 'LoopStatement: { '
        o += self.assignment_statement.to_string()
        o += ' '
        o += self.expression.to_string()
        o += ' Statements: {'
        for statement in self.statements:
            o += statement.to_string()
            o += ', '
        o += ' } }'
        return o

    def generate_code(self,env):
        statements = []
        for_number = env.get_next_for()
        statements.append('FOR%s:'%for_number)
        for stat in self.statements:
            loop_statements,final_register = stat.generate_code(env)
            statements.extend(['\t'+a for a in loop_statements])
            if final_register in env.active_registers: env.active_register.remove(final_register)
        if final_register in env.active_registers: env.active_register.remove(final_register)
        control_expressions,final_register = self.assignment_statement.generate_code(env)
        statements.extend(control_expressions)
        env.active_registers.remove(final_register)
        new_statements,final_register = self.expression.generate_code(env)
        statements.extend(new_statements)
        statements.append('if ( R[%s] ) goto FOR%s ;' % (final_register,for_number))
        env.active_registers.remove(final_register)
        return statements,0

