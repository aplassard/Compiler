from Node import Node

class Word(Node):
    def __init__(self,term):
        self.term = term

    def to_string(self):
        return 'Word: { %s }' % self.term.token_content

    def get_type(self,env):
        return self.term.get_type(env)
