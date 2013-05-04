from DeclerationAnalyzer import DeclerationAnalyzer

class TypeChecker(object):
    def __init__(self,ast):
        self.ast = ast

    def run(self):
        print '------------------------------'
        print '---Starting Lexial Analysis---'
        print '------------------------------'
        print
        print 'Program Name: %s' % self.ast.program_header.identifier.identifier.token_content
        print
        print 'Program Declerations:'
        DA = DeclerationAnalyzer()
        for dec in self.ast.program_body.declerations:
            DA(dec)

        for stat in self.ast.program_body.statements:
           DA.test_statement(stat)
