from ActivationRecord import ActivationRecord
from Parser.VariableDecleration import VariableDecleration
from Parser.AssignmentStatement import AssignmentStatement
from Parser.LoopStatement import LoopStatement
from Parser.IfStatement import IfStatement

class CodeGenerator(object):
    def __init__(self,program,next_register=1,previous_registers=set([0])):
        self.active_registers = previous_registers
        self.next_active_register = next_register
        self.program_activation = ActivationRecord(0,program.ast.program_header.identifier.to_string())
        self.then_labels = -1
        self.for_labels = -1
        self.statements = []
        for dec in program.ast.program_body.declerations:
            if type(dec) == VariableDecleration:
                self.program_activation.add_argument(dec,None)
        print str(self.program_activation)
        for stat in program.ast.program_body.statements:
            if type(stat)==AssignmentStatement:
                self.active_registers = previous_registers
                print 'Assigning a value to variable %s at location MM[%s]' %(stat.destination.identifier.identifier.token_content,self.program_activation.get_mem_location(stat.destination.identifier.identifier.token_content,offset = (0 if not stat.destination.expression else int(stat.destination.expression.arith_op.relation.term.factor.number.token_content))))
                new_statements,final_register = stat.generate_code(self)
                self.statements.extend(new_statements)
            elif type(stat) == IfStatement:
                new_statements,final_register = stat.generate_code(self)
                self.statements.extend(new_statements)
            elif type(stat) == LoopStatement:
                new_statements,final_register = stat.generate_code(self)
                self.statements.extend(new_statements)
            else:
                print 'something else:', type(stat)
            if final_register in self.active_registers:
                self.active_registers.remove(final_register)
        print '-------------- Code ---------------'
        print
        print '\n'.join(self.statements)
        print
        print '==================================='

    def get_mem_location(self,name):
        return self.program_activation.get_mem_location(name)

    def get_next_then(self):
        self.then_labels += 1
        return self.then_labels

    def get_next_register(self):
        if len(list(self.active_registers)) > 0:
            n = max(list(self.active_registers)) + 1
        else:
            n = 0
        self.active_registers.add(n)
        return n

    def get_next_for(self):
        self.for_labels += 1
        return self.for_labels
