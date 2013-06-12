from Node import Node

class IfStatement(Node):
    def __init__(self,expression,then_statements,else_statements):
        self.expression = expression
        self.then_statements = then_statements
        self.else_statements = else_statements

    def to_string(self):
        o = 'IfStatement: {'
        o += self.expression.to_string()
        o += ' ThenStatements: { '
        for statement in self.then_statements:
            o += statement.to_string()
            o += ', '
        o += ' }'
        o += ' ElseStatements: { '
        for statement in self.else_statements:
            o += statement.to_string()
            o += ', '
        o += ' } }'
        return o

    def generate_code(self,env):
        statements = []
        new_statements,final_register = self.expression.generate_code(env)
        statements.extend(new_statements)
        then_number = env.get_next_then()
        statements.append('if ( R[%s] ) goto THEN%s;'%(final_register,then_number))
        env.active_registers.remove(final_register)
        for stat in self.else_statements:
            new_statements,final_register = stat.generate_code(env)
            statements.extend(new_statements)
            if final_register in env.active_registers:
                env.active_registers.remove(final_register)
        statements.append('THEN%s:'%then_number)
        for stat in self.then_statements:
            new_statements,final_register = stat.generate_code(env)
            for s in new_statements:
                statements.append('\t'+s)
            if final_register in env.active_registers:
                env.active_registers.remove(final_register)
        return statements,0

