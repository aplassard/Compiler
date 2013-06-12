class ActivationRecord(object):
    def __init__(self,return_location,name):
        self.name            = name
        self.return_location = return_location
        self.variables       = {}
        self.control_link    = 8 if not self.return_location else self.return_location + 8

    def add_argument(self,argument,out):
        self.variables[argument.identifier.to_string()] = out if out else self.control_link
        if not out: self.control_link += 8*(1 if not argument.array_size else int(argument.array_size.term.token_content))

    def __str__(self):
        o = '+-----  Activation Record for %s  -----+' % self.name
        o += '\n'
        o += ' The Stack Pointer to Return to is %s ' % self.return_location
        o += '\n'
        o += ' Variables:'
        for key in self.variables.keys():
            o += '\n'
            o += '   %s: MM[%s]' % (key,self.variables[key],)
        o += '\n'
        o += '+--------------------------------------+'
        return o

    def get_mem_location(self,key,offset=0):
        return self.variables[key] + offset*8
