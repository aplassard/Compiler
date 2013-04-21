import os
from Token import *

class LexicalAnalyzer(object):
    def __init__(self,filename):
        self._scanner = Scanner(filename)
        self._tokens = []

    def run(self):
        while True:
            next_token = self._scanner.get_token()
            if not next_token:
                break
            else:
                self._tokens.append(next_token)

class Scanner(object):
    def __init__(self,filename):
        self.f = FileReader(filename)
        self.line_num = 0

    def get_token(self):
        self._cur = self.f.get_char()
        if self._cur == '\n':
            self.line_num+=1
        while self._cur in whitespace:
            self._cur = self.f.get_char()
        if self._cur == '"':
            return self._parse_string()
        elif self._cur in letters:
            return self._parse_keyword()
        elif self._cur in numbers:
            return self._parse_number
        elif self._cur in symbols:
            return self._parse_symbol
        else:
            raise CharacterNotFound(self._cur)

    class CharacterNotFound(Exception):
        def __init__(self,char):
            self.char = char

        def __str__(self):
            return "Invalid Character Found: "+str(self.char)

    def _parse_string(self):
        token_text = ""
        while self._cur != '"' and self._cur != '\n':
            token_text += self._cur
            self._cur = self._f.get_char()
        if self._cur =='\n':
            self.line_num+=1
            raise InvalidTokenException("string",token_text,self.line_num)
        self._f.push_back()
        return Token("string",token_text,self.line_num)

    def _parse_keyword(self):
        token_text = ""
        while self._cur in letters or self._cur == "_":
            token_text += self._cur
            self._cur = self._f.get_char()
        self._f.push_back()
        return Token("keyword",token_text,self.line_num)

    def _parse_number(self):
        token_text = ""
        while self._cur in numbers:
            token_text += self._cur
            self._cur = self._f.get_char()
        if self._cur == '.':
            token_text += self._cur
            self._cur = self._f.get_char()
            while self._cur in numbers:
                token_text += self._cur
                self._cur = self._f.get_char()
        self._f.push_back()
        return Token("number",token_text,self.line_num

    def _parse_symbol(self):
        pass

class FileReader(object):
    '''
    Simple Class to implement pushback reader
    '''
    def __init__(self,filename):
        self._fp = os.open(filename,os.O_RDONLY,0777)
        self._buffer = None
        self._prev = None

    def get_char(self):
        if not self._buffer:
            self._prev = os.read(self._fp,1)
        elif self._buffer:
            self._prev = self._buffer
            self._buffer = None
        return self._prev

    def push_back(self):
        self._buffer = self._prev

letters = set(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","W","X","Y","Z"])
numbers = set(["1","2","3","4","5","6","7","8","9","0"])
string_symbols = set(["_",",",";",":",".","'"])
symbols = set([":",";",",","+","-","*","/","(",")","<","<=",">",">=","!=","=",":=","{","}"])
whitespace = set(["\n","\t"," "])
