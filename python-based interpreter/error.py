#Daniel Gallab
#CPSC 326-02
#Assignment 2 
#when an error is found in the lexer,
#this class is called, and a message
#describing the error is printed


class Error(Exception):
    def __init__ (self, message, line, column): #message should specify error
        self.message = message
        self.line = line
        self.column = column
    def __str__(self): #prints error
        s = ''
        s += 'error:' + self.message
        s += 'at line' + str(self.line)
        s += 'column' + str(self.column)
        return s

