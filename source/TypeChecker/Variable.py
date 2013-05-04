from TypeCheckException import TypeCheckException

class Variable(object):
    def __init__(self,var):
        self.identifier = var.identifier.identifier
        self.type_mark  = var.type_mark.type_mark
        self.array_size = var.array_size.term if var.array_size else None

    def __str__(self):
        o  = self.type_mark.token_content
        o += ' '
        o += self.identifier.token_content
        if self.array_size:
            o += '[%s]' % self.array_size.token_content
        return o
