class TypeCheckException(Exception):
    def __init__(self,message,line):
        self.message = message
        self.line    = line
