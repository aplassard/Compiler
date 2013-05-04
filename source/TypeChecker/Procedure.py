from TypeCheckException import TypeCheckException
from Variable import Variable
import DeclerationAnalyzer

class Procedure(object):
    def __init__(self,node,env):
        self.name         = node.procedure_header.identifier.identifier
        self.declerations = DeclerationAnalyzer.DeclerationAnalyzer()
        for dec in node.procedure_body.declerations:
            self.declerations(dec)
        self.declerations.global_procedures = env.global_procedures
        self.declerations.global_variables  = env.global_variables
        for param in node.procedure_header.parameter_list.vals():
            param = Parameter(param)
            if param.IN:
                if self.declerations.variables.has_key(param.identifier.token_content):
                    raise TypeCheckException('Variable %s declared in parameter list and declerations of procedure %s' % (param.identifier.token_content,self.name.token_content,),self.name.line_number)
            self.declerations.variables[param.identifier.token_content] = param
        self._parse_statements(node.procedure_body.statements)

    def __str__(self):
        o  = self.name.token_content
        o += '\n'
        o += '\t'
        o += 'Available Declerations:'
        o += '\n\t\t'
        o += '\n\t\t'.join([a for a in self.declerations.iterate()])
        return o

    def test_statement(self,statement):
        pass

    def _parse_statements(self,statements):
        for stat in statements: self.test_statement(stat)


class Parameter(Variable):
    def __init__(self,param):
        Variable.__init__(self,param.variable_decleration)
        self.IN = param.IN


