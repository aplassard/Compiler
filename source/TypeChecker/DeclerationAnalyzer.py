from Parser.ProcedureDecleration import ProcedureDecleration
from Parser.VariableDecleration import VariableDecleration
from TypeCheckException import TypeCheckException
from Variable import Variable
from Procedure import Procedure
from Parser.AssignmentStatement import AssignmentStatement
from AssignmentStatement import AssignmentStatement as Assignment

class DeclerationAnalyzer(object):
    def __init__(self):
        self.variables         = {}
        self.procedures        = {}
        self.global_procedures = {}
        self.global_variables  = {}

    def __call__(self,dec):
        if type(dec) == ProcedureDecleration:
            self._parse_procedure(dec)
        elif type(dec) == VariableDecleration:
            self._parse_variable(dec)
        else:
            print 'not a known decleration type:',type(dec)

    def test_statement(self,statement):
        if type(statement)==AssignmentStatement:
            name = statement.destination.identifier.identifier.token_content
            if self.variables.has_key(name):
                print self.variables[name]
            elif self.global_variables.has_key(name):
                print self.global_variables[name],'global'
            else: raise TypeCheckException('Variable %s Not Found' % name,statement.destintation.identifier.identifier.line_number)
        else:
            print type(statement)

    def _parse_procedure(self,dec):
        name = dec.procedure_header.identifier.identifier.token_content
        line_num = dec.procedure_header.identifier.identifier.line_number
        if dec.GLOBAL:
            if self.global_procedures.has_key(name):
                raise TypeCheckException('Global Procedure %s was declared at multiple locations' % (name),line_num)
            self.global_procedures[name] = Procedure(dec)
        else:
            if self.procedures.has_key(name):
                raise TypeCheckException('Procedure %s was declared at multiple locations' % (name),line_num)
            dec = Procedure(dec,self)
            self.procedures[name] = dec
        print  'procedure: %s' % str(dec)


    def _parse_variable(self,dec):
        line_num  = dec.identifier.identifier.line_number
        name      = dec.identifier.identifier.token_content
        type_mark = dec.type_mark.type_mark.token_type
        if dec.GLOBAL:
            if self.global_variables.has_key(name):
                raise TypeCheckException('Global Variable %s was declared at multiple locations' %(name),line_num)
            self.global_variables[name] = Variable(dec)
        else:
            if self.variables.has_key(name):
                raise TypeCheckException('Variable %s was declared at multiple locations' %(name),line_num)
            self.variables[name] = Variable(dec)
        print 'variable:  %s' % str(Variable(dec))

    def iterate(self):
        for key in self.variables.keys():
            yield str(self.variables[key])
        for key in self.global_variables.keys():
            yield 'GLOBAL ' + str(self.global_variables[key])
        for key in self.procedures.keys():
            yield str(self.procedures[key])
        for key in self.global_procedures.keys():
            yield 'GLOBAL ' + str(self.global_procedures[key])

