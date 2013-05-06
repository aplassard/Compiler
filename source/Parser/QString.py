from Node import Node

class QString(Node):
    def __init__(self,qstring):
        self.qstring = qstring

    def to_string(self):
        o = 'QString: { '
        o += self.qstring.token_content
        o += ' }'
        return o

    def get_type(self,emv):
        return 'QSTRING'

    def get_line_number(self):
        return self.qstring.line_number
