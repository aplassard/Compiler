
class AssignmentStatement(object):
    def __init__(self,stat):
        self.destination = stat.destination
        self.expression  = stat.expression
        self._evaluate()

    def evaluate(self):
        pass
