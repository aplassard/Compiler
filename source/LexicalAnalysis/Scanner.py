import os
from Token import *
from ReservedWords import reserved_words, symbols

class Scanner(object):
    def __init__(self,filename):
        self._f = FileReader(filename)
        self.line_number = 1

    def get_token(self):
        self._cur = self._f.get_char()
        while self._cur in whitespace:
            if self._cur == '\n':
                self.line_number +=1
            self._cur = self._f.get_char()
            if len(self._cur)==0: return None
        if len(self._cur)==0:
            return None
        elif self._cur =='"':
            T = self._parse_string()
        elif self._cur in numbers:
            T = self._parse_number()
        elif self._cur in letters:
            T = self._parse_keyword()
        elif self._cur in symbols.keys() or self._cur == '=':
            T = self._parse_symbol()
        else:
            raise CharNotFoundException(self._cur,self.line_number)
        return T

    def _parse_string(self):
        token_text = ""
        token_text += self._cur
        self._cur = self._f.get_char()
        while self._cur != '"':
            token_text += self._cur
            self._cur = self._f.get_char()
        token_text += self._cur
        return Token("QSTRING",token_text,self.line_number)

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
        return Token("NUMBER",token_text,self.line_number)

    def _parse_keyword(self):
        token_text = ""
        while self._cur in letters or self._cur == "_" or self._cur in numbers:
            token_text += self._cur
            self._cur = self._f.get_char()
        self._f.push_back()
        token_class = reserved_words.get(token_text,"IDENTIFIER")
        return Token(token_class,token_text,self.line_number)

    def _parse_symbol(self):
        token_text = ""
        if self._cur =='/':
            token_text = self._cur
            self._cur = self._f.get_char()
            if self._cur == '/':
                token_text += self._cur
                token_text += self._parse_comment()
                return Token("COMMENT",token_text,self.line_number)
            else:
                self._f.push_back()
                return Token(symbols[token_text],token_text,self.line_number)
        else:
            token_text = self._cur
            self._cur = self._f.get_char()
            try:
                symbols[token_text + self._cur]
                return Token(symbols[token_text+self._cur],token_text,self.line_number)
            except:
                self._f.push_back()
                return Token(symbols[token_text],token_text,self.line_number)

    def _parse_comment(self):
        token_text = ""
        self._cur = self._f.get_char()
        while self._cur != '\n':
            token_text += self._cur
            self._cur = self._f.get_char()
        self._f.push_back()
        return token_text


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

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
whitespace = "\n\t \r"

class CharNotFoundException(Exception):
    def __init__(self,text,line_number):
        self.char_text = text
        self.line_number = line_number

    def to_string(self):
        return "Invalid Character %s found at line %s" % (self.char_text, str(self.line_number),)
