from Node import Node

class Identifier(Node):
    def __init__(self,identifier):
        self.identifier = identifier

    def to_string(self):
        return self.identifier.token_content

    def get_type(self,env):
            identifier_type = env.variables(self.identifier.token_content)
            if not identifier_type:
                identifier_type = env.global_variables(self.identifier.token_content)
            if not identifier_type:
                raise TypeCheckException('Could not find identifier %s' % self.identifier.token_content,self.identifier.line_number)
            return identifier_type.type_mark
