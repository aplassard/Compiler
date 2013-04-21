
class Token(object):
    def __init__(self,token_type,token_content,line_number):
        self.token_type    = token_type
        self.token_content = token_content
        self.line_number   = line_number

class InvalidTokenException(Exception):
    def __init__(self,token_type,token_content,line_number):
        self.token_type    = token_type
        self.token_content = token_content
        self.line_number   = line_number
