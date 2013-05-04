import os
from Token import *
from Scanner import *

class LexicalAnalyzer(object):
    def __init__(self,filename):
        self._scanner = Scanner(filename)
        self._tokens = []

    def run(self):
        while True:
            try:
                next_token = self._scanner.get_token()
                if not next_token:
                    break
                else:
                    print next_token.to_string()
                    self._tokens.append(next_token)
            except CharNotFoundException as e:
                print e.to_string()

    def get_tokens(self):
        return self._tokens
