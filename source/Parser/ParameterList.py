from Node import Node

class ParameterList(Node):
    def __init__(self,parameter,parameter_list):
        self.parameter = parameter
        self.parameter_list = parameter_list

    def to_string(self):
        o = 'Parameter List: {'
        o += self.parameter.to_string()
        if self.parameter_list:
            o += ' '
            o += self.parameter_list.to_string()
        o += ' }'
        return o

    def vals(self):
        yield self.parameter
        if self.parameter_list:
            yield self.parameter_list.vals()

