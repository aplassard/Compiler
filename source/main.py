#!/usr/bin/env python
from LexicalAnalysis import LexicalAnalyzer
import sys
from Parser import Parser
from TypeChecker import TypeChecker
from CodeGeneration import CodeGenerator

usage = '''
    python %s <input_file>
''' % 'main.py'

def main(argv):
    try:
        LA = LexicalAnalyzer(argv[1])
    except IndexError:
        print usage
        return 1
    LA.run()
    P = Parser(LA)
    P.run()
    TC = TypeChecker(P.ast)
    TC.run()
    print
    print '---------------------------------------------------------------------------------------'
    print '-------------------------      Starting Code Generation       -------------------------'
    print '---------------------------------------------------------------------------------------'
    print
    CG = CodeGenerator(P)


    return 0

def target(*args):
    return main,None

if __name__=='__main__':
    main(sys.argv)
