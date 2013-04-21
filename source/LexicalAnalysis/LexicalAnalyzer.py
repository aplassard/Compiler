import os

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
        self._cur = self.f.get_char
        if cur == '\n':
            self.line_num+=1
        while self._cur in whitespace:
            self._cur = self.f.get_char
        if self._cur == '"':
            pass
        elif self._cur in letters:
            pass
        elif self._cur in numbers:
            pass

    def _parse_string(self):
        pass

    def _parse_keyword(self):
        pass

    def _parse_number(self):
        pass

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
