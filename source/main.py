#!/usr/bin/env python
from LexicalAnalysis import LexicalAnalyzer
import sys

usage = '''
    python %s <input_file>
''' % 'main.py'

def main(argv):
    try:
        LA = LexicalAnalyzer(argv[1])
    except IndexError:
        print usage
        return 1
    return 0

def target(*args):
    return main,None

if __name__=='__main__':
    main(sys.argv)
