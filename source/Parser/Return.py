from Node import Node

class Return(Node):
    def __init__(self,return_statement):
        self.return_statement = return_statement

    def to_string(self):
        return "Return: { RETURN }"
