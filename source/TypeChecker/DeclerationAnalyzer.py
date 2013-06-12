from Parser.ProcedureDecleration import ProcedureDecleration
from Parser.VariableDecleration import VariableDecleration
from TypeCheckException import TypeCheckException
from Variable import Variable
from Procedure import Procedure
from Parser.AssignmentStatement import AssignmentStatement
from AssignmentStatement import AssignmentStatement as Assignment
from Parser.IfStatement import IfStatement
from collections import namedtuple
from Parser.LoopStatement import LoopStatement
from Parser.Return import Return
from Parser.ProcedureCall import ProcedureCall

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

    def test_statement(self,statement):  # This code is awful.  I should fix it
        if type(statement)==AssignmentStatement:
            name =statement.destination.identifier.identifier.token_content
            try:
                if self.variables.has_key(name):
                    var = self.variables.get(name)
                    exp = statement.expression.get_type(self)
                elif self.global_variables.has_key(name):
                    var = self.global_variables.get(name)
                    exp = statement.expression.get_type(self)
                else: raise TypeCheckException('Variable %s Not Found' % name,statement.destination.identifier.identifier.line_number)
                if MAPPINGS.get(Mapping(expression=exp,destination=var.type_mark.token_content)):
                    print '--The assignment statement for %s Type Checked Successfully at line %s--' % (name,statement.destination.identifier.identifier.line_number,)
                else:
                    raise TypeCheckException('Destination %s was declerared as %s but was set as %s' % (name,var.type_mark.token_content,exp,),statement.destination.identifier.identifier.line_number)
            except TypeCheckException as ex:
                print
                print ex.message,'at line',ex.line
                import sys
                sys.exit(0)
        elif type(statement) == IfStatement:
            try:
                expression_type = statement.expression.get_type(self)
                if expression_type != 'BOOLEAN': raise TypeCheckException('If Statement Expression did not contain a boolean',statement.expression.get_line_number())
                for stat in statement.then_statements:
                    self.test_statement(stat)
                for stat in statement.else_statements:
                    self.test_statement(stat)
            except TypeCheckException as ex:
                print ex.message,'at line',ex.line
                print 'Exitting'
                import sys
                sys.exit(0)
            print '--The If Statement starting at line %s type checked successfully--' % statement.expression.get_line_number()
        elif type(statement) == LoopStatement:
            try:
                self.test_statement(statement.assignment_statement)
                expression_type = statement.expression.get_type(self)
                if expression_type != 'BOOLEAN': raise TypeCheckException('Loop Statement Expression did not contain a boolean',statement.expression.get_line_number())
                for stat in statement.statements:
                    self.test_statement(stat)
            except TypeCheckException as ex:
                print
                print ex.message,'at line',ex.line
                import sys
                sys.exit(0)
            print '--The Loop Statement starting at line %s type check successfully--' % statement.expression.get_line_number()
        elif type(statement) == Return:
            print '--Return Statement Type Checked at line %s--' % statement.return_statement.line_number
        elif type(statement) == ProcedureCall:
            try:
                name = statement.identifier.identifier.token_content
                print '--Found Procedure Call Named %s--' % name
                proc = self.procedures.get(name,self.global_procedures.get(name,False))
                if not proc: raise TypeCheckException('Procedure %s not found in scope' % name, statement.identifier.identifier.line_number)
                if len(statement.argument_list) != len(proc.parameters):
                    raise TypeCheckException("Incorrect Number of Parameters Found for Procedure %s!  %s found and %s expected." % (name,len(statement.argument_list),len(proc.parameters)),statement.identifier.identifier.line_number)
                for i in xrange(len(statement.argument_list)):
                    if not MAPPINGS.get(Mapping(expression=statement.argument_list(i).get_type(self),destination=proc.parameters[i].get_type(self))):
                        raise TypeCheckException('Could not call procedure %s with variable of type %s when expected variable of class %s' % (name,statement.argument_list(i).get_type(self),proc.parameters[i].get_type(self),),statement.identifier.identifier.line_number)
                print '--Procedure Call at line %s Type Checked Successfully--' % statement.identifier.identifier.line_number
            except TypeCheckException as ex:
                print
                print ex.message,'at line',ex.line
                import sys
                sys.exit(0)

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

Mapping = namedtuple('Mapping',['destination','expression'])

MAPPINGS = {
        Mapping(expression='NUMBER',destination='integer'):True,
        Mapping(expression='NUMBER',destination='float'):True,
        Mapping(expression='QSTRING',destination='string'):True,
        Mapping(expression='BOOLEAN',destination='bool'):True,
}
