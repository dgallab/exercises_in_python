#Daniel Gallab
#CPSC 326-02
#Assignment 2
#when a token is found, by the lexer
#its tokentype is determined among these
#predefined variables

PRINT = 'PRINT'
PRINTLN = 'PRINTLN'
READINT = 'READINT'
READSTR = 'READSTR'
LPAREN = 'LPAREN' 
RPAREN = 'RPAREN' 
SEMICOLON = 'SEMICOLON' 
ID = 'ID'
LBRACKET = 'LBRACKET' 
RBRACKET = 'RBRACKET' 
STRING = 'STRING' 
INT = 'INT' 
BOOL = 'BOOL'
COMMA = 'COMMA' 
ASSIGN = 'ASSIGN'
PLUS = 'PLUS'  
MINUS = 'MINUS'
DIVIDE = 'DIVIDE'
MULTIPLY = 'MULTIPLY'
MODULUS='MODULUS'
IF = 'IF' 
THEN = 'THEN'
ELSEIF = 'ELSEIF' 
ELSE = 'ELSE'
END = 'END' 
NOT = 'NOT'
AND = 'AND'
OR = 'OR'
EQUAL = 'EQUAL'
LESS_THAN = 'LESS_THAN' 
GREATER_THAN = 'GREATER_THAN' 
LESS_THAN_EQUAL = 'LESS_THAN_EQUAL'
GREATER_THAN_EQUAL = 'GREATER_THAN_EQUAL' 
NOT_EQUAL = 'NOT_EQUAL' 
WHILE = 'WHILE ' 
DO = 'DO' 
EOS ='EOS' 


class Token(object):
    def __init__(self, tokentype, lexeme, line, column):
        self.tokentype = tokentype #one of the predefined strings 
        self.lexeme = lexeme #the actual token
        self.line = line #line which token is found
        self.column = column #column which token is found

    def __str__(self): #prints the token
        return(self.tokentype+" "+self.lexeme+" "+str(self.line)+":"+str(self.column)+'\n')
        
        

