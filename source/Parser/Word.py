from Node import Node

class Word(Node):
    def __init__(self,term):
        self.term = term

    def to_string(self):
        return 'Word: { %s }' % self.term.token_content

    def get_type(self,env):
        if self.term.token_type in ['TRUE','FALSE']:
            return 'BOOLEAN'
        return self.term.get_type(env)

    def get_line_number(self):
        return self.term.line_number

    def generate_code(self,env):
        final_register = env.get_next_register()
        if self.term.token_type in ['TRUE','FALSE']:
            return ['R[%s] = %s' %( final_register, self.term.token_content)],final_register
