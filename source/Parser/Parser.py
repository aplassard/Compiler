from Number import Number
from TypeMark import TypeMark, TYPE_MARKS
from QString import QString
from Identifier import Identifier
from Word import Word
from Term import Term
from Name import Name
from Relation import Relation, RELATIONS
from ArithOp import ArithOp
from Expression import Expression
from ArgumentList import ArgumentList
from Destination import Destination
from AssignmentStatement import AssignmentStatement
from ProcedureCall import ProcedureCall
from VariableDecleration import VariableDecleration
from IfStatement import IfStatement
from LoopStatement import LoopStatement
from Parameter import Parameter
from ParameterList import ParameterList
from ProcedureHeader import ProcedureHeader
from ProcedureBody import ProcedureBody
from ProcedureDecleration import ProcedureDecleration
from ProgramBody import ProgramBody
from ProgramHeader import ProgramHeader
from Program import Program
from Return import Return

class Parser(object):

    def __init__(self,lexical_analyzer):
        self._tokens = filter(lambda x: x.token_type != 'COMMENT',lexical_analyzer.get_tokens())
        self.next = 0
        self.program = None

    def run(self):
        print "parsing"
        while self.next < len(self._tokens):
            self.ast = self._parse()
        print "done parsing"
        print

    def _parse(self):
        node = self._parse_program()
        if node:
            print "Found Program"
        else:
            print "Something Went Wrong"
            import sys
            sys.exit(1)
        print node.to_string()
        return node

    def _parse_word(self,word):
        save = self.next
        if self._tokens[self.next].token_type==word:
            node = Word(self._tokens[self.next])
            self.next += 1
            return node
        else:
            return False

    def _parse_number(self):
        save = self.next
        if self._tokens[self.next].token_type=='NUMBER':
            node = Number(self._tokens[self.next])
            self.next += 1
            return node
        elif self._tokens[self.next].token_type=='MINUS':
            self.next += 1
            if self._tokens[self.next].token_type=='NUMBER':
                node = Number(self._tokens[self.next],negative=True)
                self.next += 1
                return node
        else:
            self.next = save
            return False

    def _parse_qstring(self):
        save = self.next
        if self._tokens[self.next].token_type=='QSTRING':
            node = QString(self._tokens[self.next])
            self.next += 1
            return node
        else:
            return False


    def _parse_identifier(self):
        save = self.next
        if self._tokens[self.next].token_type=='IDENTIFIER':
            node = Identifier(self._tokens[self.next])
            self.next += 1
            return node
        else:
            return False

    def _parse_type_mark(self):
        save = self.next
        if self._tokens[self.next].token_type in TYPE_MARKS:
            node = TypeMark(self._tokens[self.next])
            self.next +=1
            return node
        else:
            return False

    def _parse_factor(self):
        save = self.next
        if self._tokens[self.next].token_type=='OPEN_PAREN':
            self.next += 1
            node = self._parse_expression()
            if node:
                if self._tokens[self.next].token_type=='CLOSE_PAREN':
                    self.next +=1
                    return node
        self.next = save
        node = self._parse_name()
        if node:
            return node
        self.next = save
        node = self._parse_number()
        if node:
            return node
        self.next = save
        node = self._parse_qstring()
        if node:
            return node
        self.next = save
        node = self._parse_word("TRUE")
        if node:
            return node
        self.next = save
        node = self._parse_word("FALSE")
        if node:
            return node
        self.next = save
        return False

    def _parse_term(self):
        save = self.next
        factor = self._parse_factor()
        if factor:
            if self.next >= len(self._tokens):
                return Term(factor)
            save2 = self.next
            if self._tokens[self.next].token_type in ["MULTIPLY","DIVIDE"]:
                op = self._tokens[self.next]
                self.next += 1
                factor2 = self._parse_term()
                if factor2:
                    return Term(factor,op,factor2)
            self.next = save2
            return Term(factor)
        self.next = save
        return False

    def _parse_name(self,negative=False):
        save = self.next
        identifier = self._parse_identifier()
        if identifier:
            save = self.next
            if self.next >= len(self._tokens):
                return Name(identifier,negative=negative)
            if self._tokens[self.next].token_type=='OPEN_BRACKET':
                self.next += 1
                expression = self._parse_expression()
            else:
                return Name(identifier,negative=negative)
            if self._tokens[self.next].token_type=='CLOSE_BRACKET':
                self.next += 1
                return Name(identifier, expression,negative)
            return Name(identifier,negative=negative)
        self.next = save
        return False

    def _parse_relation(self):
        save = self.next
        term = self._parse_term()
        if term:
            save = self.next
            if self.next >= len(self._tokens):
                return Relation(term)
            if self._tokens[self.next].token_type in RELATIONS:
                op = self._tokens[self.next]
                self.next += 1
                relation = self._parse_relation()
                if relation:
                    return Relation(term,op,relation)
            self.next = save
            return Relation(term)
        self.next = save
        return False

    def _parse_arith_op(self):
        save = self.next
        relation = self._parse_relation()
        if relation and len(self._tokens) >  self.next:
            save = self.next
            if self._tokens[self.next].token_type in ["PLUS","MINUS"]:
                op = self._tokens[self.next]
                self.next += 1
                arith_op = self._parse_arith_op()
                if arith_op:
                    return ArithOp(relation,op,arith_op)
            self.next = save
            return ArithOp(relation)
        elif relation:
            return ArithOp(relation)
        else:
            self.next = save
            return False

    def _parse_expression(self):
        save = self.next
        arith_op = self._parse_arith_op()
        if arith_op and len(self._tokens) > self.next:
            save = self.next
            if self._tokens[self.next].token_type in ["AND","OR"]:
                op = self._tokens[self.next]
                self.next += 1
                expression = self._parse_expression()
                if expression:
                    return Expression(arith_op,op,expression)
                else:
                    self.next = save
                    return Expression(arith_op)
            else:
                self.next = save
                return Expression(arith_op)
        elif arith_op:
            return Expression(arith_op)
        else:
            return False

    def _parse_argument_list(self):
        save = self.next
        expression = self._parse_expression()
        if expression and len(self._tokens) > self.next:
            save = self.next
            if self._tokens[self.next].token_type == 'COMMA':
                self.next += 1
                argument_list = self._parse_argument_list()
                if argument_list:
                    return ArgumentList(expression,argument_list)
            self.next = save
            return ArgumentList(expression)
        elif expression:
            return ArgumentList(expression)
        else:
            self.next = save
            return False

    def _parse_return_statement(self):
        save = self.next
        if not self._tokens[self.next].token_type == 'RETURN':
            self.next = save
            return False
        return_statement = Return(self._tokens[self.next])
        self.next += 1
        return return_statement

    def _parse_destination(self):
        save = self.next
        identifier = self._parse_identifier()
        if identifier and len(self._tokens) > self.next:
            if not self._tokens[self.next].token_type=='OPEN_BRACKET':
                return Destination(identifier,None)
            self.next += 1
            expression = self._parse_expression()
            if not expression:
                self.next = save
                return False
            if self._tokens[self.next].token_type=='CLOSE_BRACKET':
                self.next += 1
                return Destination(identifier,expression)
        elif identifier:
            return Destination(Identifier,None)
        self.next = save
        return False

    def _parse_assignment_statement(self):
        save = self.next
        destination = self._parse_destination()
        if destination and len(self._tokens) > self.next and self._tokens[self.next].token_type == 'ASSIGNMENT':
            self.next +=1
            expression = self._parse_expression()
            if expression:
                return AssignmentStatement(destination,expression)
        self.next = save
        return False

    def _parse_procedure_call(self):
        save = self.next
        identifier = self._parse_identifier()
        if identifier and len(self._tokens) > self.next+1 and self._tokens[self.next].token_type=='OPEN_PAREN':
            self.next += 1
            argument_list = self._parse_argument_list()
            if argument_list and self._tokens[self.next].token_type=='CLOSE_PAREN':
                self.next += 1
                return ProcedureCall(identifier,argument_list)
        self.next = save
        return False

    def _parse_variable_decleration(self,GLOBAL=False):
        save = self.next
        type_mark = self._parse_type_mark()
        if type_mark:
            identifier = self._parse_identifier()
            if identifier and self._tokens[self.next].token_type == 'OPEN_BRACKET':
                self.next += 1
                array_size = self._parse_array_size()
                if array_size and self._tokens[self.next].token_type == 'CLOSE_BRACKET':
                    self.next += 1
                    return VariableDecleration(type_mark,identifier,array_size,GLOBAL=GLOBAL)
            else:
                return VariableDecleration(type_mark,identifier,None,GLOBAL=GLOBAL)
        self.next = save
        return False

    def _parse_array_size(self):
        save = self.next
        number = self._parse_word("NUMBER")
        return number if number else False

    def _parse_if_statement(self):
        save = self.next
        if self._tokens[self.next].token_type == 'IF':
            self.next += 1
            expression = self._parse_expression()
            if not expression:
                self.next = save
                return False
            if not self._tokens[self.next].token_type == 'THEN':
                self.next = save
                return False
            self.next += 1
            then_statements = self._parse_statement_list()
            if not then_statements:
                self.next = save
                return False
            else_statements = []
            if self._tokens[self.next].token_type == 'ELSE':
                self.next += 1
                else_statements = self._parse_statement_list()
                if not else_statements:
                    self.next = save
                    return False
            if not self._tokens[self.next].token_type == 'END' and not self._tokens[self.next+1].token_type == 'IF':
                self.next = save
                return False
            self.next += 2
            return IfStatement(expression,then_statements,else_statements)
        return False

    def _parse_statement(self):
        save = self.next
        assignment_statement = self._parse_assignment_statement()
        if assignment_statement:
            return assignment_statement
        if_statement = self._parse_if_statement()
        if if_statement:
            return if_statement
        loop_statement = self._parse_loop_statement()
        if loop_statement:
            return loop_statement
        return_statement = self._parse_return_statement()
        if return_statement:
            return return_statement
        procedure_call = self._parse_procedure_call()
        if procedure_call:
            return procedure_call
        return False

    def _parse_loop_statement(self):
        save = self.next
        if self._tokens[self.next].token_type != 'FOR':
            self.next = save
            return False
        self.next += 1
        if self._tokens[self.next].token_type != 'OPEN_PAREN':
            self.next = save
            return False
        self.next += 1
        assignment_statement = self._parse_assignment_statement()
        if not assignment_statement:
            self.next = save
            return False
        if self._tokens[self.next].token_type != 'SEMICOLON':
            self.next = save
            return False
        self.next += 1
        expression = self._parse_expression()
        if not expression:
            self.next = save
            return False
        if self._tokens[self.next].token_type != 'CLOSE_PAREN':
            self.next = save
            return False
        self.next += 1
        statements = self._parse_statement_list()
        if not statements:
            self.next = save
            return False
        if self._tokens[self.next].token_type != 'END':
            self.next = save
            return False
        self.next += 1
        if self._tokens[self.next].token_type != 'FOR':
            self.next = save
            return False
        self.next += 1
        return LoopStatement(assignment_statement,expression,statements)


    def _parse_statement_list(self):
        save = self.next
        statements = []
        statement = self._parse_statement()
        if not statement or not self._tokens[self.next].token_type == 'SEMICOLON':
            return statements
        while statement:
            statements.append(statement)
            if not statement or not self._tokens[self.next].token_type == 'SEMICOLON':
                return statements
            self.next += 1
            statement = self._parse_statement()
        return statements

    def _parse_parameter(self):
        save = self.next
        variable_decleration = self._parse_variable_decleration()
        if not variable_decleration:
            self.next = save
            return False
        n = self._tokens[self.next]
        self.next += 1
        if n.token_type == 'IN':
            return Parameter(variable_decleration,True)
        elif n.token_type == 'OUT':
            return Parameter(variable_decleration,False)
        else:
            self.next = save
            return False

    def _parse_parameter_list(self):
        save = self.next
        parameter = self._parse_parameter()
        if not parameter:
            self.next = save
            return False
        if self._tokens[self.next].token_type != 'COMMA':
            return ParameterList(parameter,None)
        self.next += 1
        parameter_list = self._parse_parameter_list()
        return ParameterList(parameter,parameter_list)

    def _parse_procedure_header(self):
        save = self.next
        if not self._tokens[self.next].token_type == 'PROCEDURE':
            self.next = save
            return False
        self.next += 1
        identifier = self._parse_identifier()
        if not identifier:
            self.next = save
            return False
        if not self._tokens[self.next].token_type == 'OPEN_PAREN':
            self.next = save
            return False
        self.next += 1
        parameter_list = self._parse_parameter_list()
        if not self._tokens[self.next].token_type == 'CLOSE_PAREN':
            self.next = save
            return False
        self.next += 1
        return ProcedureHeader(identifier,parameter_list)

    def _parse_procedure_decleration(self,GLOBAL=False):
        save = self.next
        procedure_header = self._parse_procedure_header()
        if not procedure_header:
            self.next = save
            return False
        procedure_body = self._parse_procedure_body()
        if not procedure_body:
            self.next = save
            return False
        return ProcedureDecleration(procedure_header,procedure_body,GLOBAL=GLOBAL)

    def _parse_procedure_body(self):
        save = self.next
        declerations = self._parse_declerations()
        if not self._tokens[self.next].token_type == 'BEGIN':
            self.next = save
            return False
        self.next += 1
        statements = self._parse_statement_list()
        if not self._tokens[self.next].token_type == 'END':
            self.next = save
            return False
        self.next += 1
        if not self._tokens[self.next].token_type == 'PROCEDURE':
            self.next = save
            return False
        self.next += 1
        return ProcedureBody(declerations,statements)

    def _parse_declerations(self):
        save = self.next
        declerations = []
        while True:
            GLOBAL = self._tokens[self.next].token_type == 'GLOBAL'
            if GLOBAL:
                self.next += 1
            decleration = self._parse_procedure_decleration(GLOBAL)
            if not decleration:
                decleration = self._parse_variable_decleration(GLOBAL)
            if not decleration:
                return declerations
            if self._tokens[self.next].token_type != 'SEMICOLON':
                self.next = save
                return False
            self.next += 1
            if decleration:
                declerations.append(decleration)
            else:
                break
        return declerations

    def _parse_program_body(self):
        save = self.next
        declerations = self._parse_declerations()
        if self._tokens[self.next].token_type!='BEGIN':
            self.next = save
            return False
        self.next += 1
        statements = self._parse_statement_list()
        print self._tokens[self.next].to_string()
        if self._tokens[self.next].token_type != 'END':
            self.next = save
            return False
        self.next += 1
        if self._tokens[self.next].token_type != 'PROGRAM':
            self.next = save
            return False
        self.next += 1
        return ProgramBody(declerations,statements)

    def _parse_program_header(self):
        save = self.next
        if self._tokens[self.next].token_type != 'PROGRAM':
            self.next = save
            return False
        self.next += 1
        identifier = self._parse_identifier()
        if not identifier:
            self.next = save
            return False
        if self._tokens[self.next].token_type != 'IS':
            self.next = save
            return False
        self.next += 1
        return ProgramHeader(identifier)

    def _parse_program(self):
        save = self.next
        program_header = self._parse_program_header()
        if not program_header:
            save = self.next
            return False
        print 'parsed program header'
        program_body = self._parse_program_body()
        if not program_body:
            return False
        print 'parsed program body'
        return Program(program_header,program_body)
