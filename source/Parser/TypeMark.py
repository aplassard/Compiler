from Node import Node

class TypeMark(Node):
    def __init__(self,type_mark):
        self.type_mark = type_mark

    def to_string(self):
        return "Type Mark: { %s }" % self.type_mark.token_type

TYPE_MARKS = ["INTEGER","FLOAT","BOOLEAN","STRING"]
