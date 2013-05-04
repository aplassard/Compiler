
class Token(object):
    def __init__(self,token_type=None,token_content=None,line_number=None):
        self.token_type    = token_type
        self.token_content = token_content
        self.line_number   = line_number

    def to_string(self):
        return "Token Type: %s, Token Content: %s, Line Number: %s" % (self.token_type,self.token_content,self.line_number,)

