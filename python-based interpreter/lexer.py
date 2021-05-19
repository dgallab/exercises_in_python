#Daniel Gallab
#CPSC 326-02
#Assignment 2 
#searches for tokens and determines their tokentype,
#line, and column



import mytoken
import error

class Lexer(object):
    def __init__(self, input_stream): #initial state/input stream is the inputted file
        self.line = 1
        self.column = 0
        self.input_stream = input_stream
        
    def __peek(self): #looks at next character without advancing
        pos = self.input_stream.tell()
        symbol = self.input_stream.read(1)
        self.input_stream.seek(pos)
        return symbol
    
    def __read(self): #advance lexer
        return self.input_stream.read(1)
    
    def next_token(self):
        a=""
        if self.__peek()== '': #end of file
            return mytoken.Token(mytoken.EOS, '', self.line, self.column)
        if self.__peek()== '\n': #end of line
            self.line+=1
            self.__read()
            self.column=0
            return self.next_token()
        if self.__peek()== ' ' or self.__peek()== '\t':#skip over whitespace and indentation
            self.__read()
            self.column+=1
            return self.next_token()
        if self.__peek()== '#':
            self.__read()
            while self.__peek()!= '\n':
                self.__read()
                if self.__peek()== '\n':
                    return self.next_token()
            #needs to skip the line still, but since that while loop was passed, we
        a+=self.__read()#add another read line here
        self.column+=1
        if a == '+':
            return mytoken.Token(mytoken.PLUS, a, self.line, self.column)
        if a == '-':
            return mytoken.Token(mytoken.MINUS, a, self.line, self.column)
        if a == '*':
            return mytoken.Token(mytoken.MULTIPLY, a, self.line, self.column)
        if a == '/':
            return mytoken.Token(mytoken.DIVIDE, a, self.line, self.column)
        if a == '%':
            return mytoken.Token(mytoken.MODULUS, a, self.line, self.column)
        if a == '=': #before making it a token, it needs to check if it is an equal statement
            if self.__peek()== '=':
                a+=self.__read()
                self.column+=1
                return mytoken.Token(mytoken.EQUAL, a, self.line, self.column)
            else:
                return mytoken.Token(mytoken.ASSIGN, a, self.line, self.column)
        if a == '>': #same idea. 
            if self.__peek()== '=':
                a+=self.__read()
                self.column+=1
                return mytoken.Token(mytoken.GREATER_THAN_EQUAL, a, self.line, self.column)
            else:
                return mytoken.Token(mytoken.GREATER_THAN, a, self.line, self.column)
        if a == '<':
            if self.__peek()== '=':
                a+=self.__read()
                self.column+=1
                return mytoken.Token(mytoken.LESS_THAN_EQUAL, a, self.line, self.column)
            else:
                self.column=self.column+1
                return mytoken.Token(mytoken.LESS_THAN, a, self.line, self.column)
        if a == '!':
            if self.__peek()== '=':
                a+=self.__read()
                self.column+=1
                return mytoken.Token(mytoken.NOT_EQUAL, a, self.line, self.column)
        if a == '(':
            return mytoken.Token(mytoken.LPAREN, a, self.line, self.column)
        if a == ')':
            return mytoken.Token(mytoken.RPAREN, a, self.line, self.column)
        if a == '[':
            return mytoken.Token(mytoken.LBRACKET, a, self.line, self.column)
        if a == ']':
            return mytoken.Token(mytoken.RBRACKET, a, self.line, self.column)
        if a == ';':
            return mytoken.Token(mytoken.SEMICOLON, a, self.line, self.column)
        if a == ',':
            return mytoken.Token(mytoken.COMMA, a, self.line, self.column)  
        if a.isdigit(): #len(a) must be checked to be greater than 0 or an error occurs
            while self.__peek().isdigit():
                a+=self.__read()
            return mytoken.Token(mytoken.INT, a, self.line, self.column)
        if a== '"': 
            a+=self.__read()
            self.column+=1
            while a[len(a)-1] != '"':
                a+=self.__read()
                self.column+=1
                if a[len(a)-1] == '\n':
                    raise error.Error('incomplete string'+a,self.line,self.column) #this works but stops everything
                    return self.next_token()
            return mytoken.Token(mytoken.STRING, a, self.line, self.column)
        if a== "'": #if first one is an ', then there must be another before the line ends
            a+=self.__read()
            self.column+=1
            while a[len(a)-1] != "'":
                a+=self.__read()
                self.column+=1
                if a[len(a)-1] == '\n': #or else an error is raised
                    raise error.Error('incomplete string'+ a,self.line,self.column)
            return mytoken.Token(mytoken.STRING, a, self.line, self.column) 
        while self.__peek().isalnum() or self.__peek()== '_' : #when any of these conditions aren't found
            a+=self.__read()#the token must be in the final state
            self.column+=1
        if a == 'or':
            return mytoken.Token(mytoken.OR, a, self.line, self.column)
        if a == 'not':
            return mytoken.Token(mytoken.NOT, a, self.line, self.column)
        if a == 'and':
            return mytoken.Token(mytoken.AND, a, self.line, self.column)
        if a == 'if':
            return mytoken.Token(mytoken.IF, a, self.line, self.column)
        if a == 'then':
            return mytoken.Token(mytoken.THEN, a, self.line, self.column)
        if a == 'do':
            return mytoken.Token(mytoken.DO, a, self.line, self.column)
        if a == 'elseif':
            return mytoken.Token(mytoken.ELSEIF, a, self.line, self.column)
        if a == 'else':
            return mytoken.Token(mytoken.ELSE, a, self.line, self.column)
        if a == 'while':
            return mytoken.Token(mytoken.WHILE, a, self.line, self.column)
        if a == 'readint':
            return mytoken.Token(mytoken.READINT, a, self.line, self.column)
        if a == 'readstr':
            return mytoken.Token(mytoken.READSTR, a, self.line, self.column)
        if a == 'println':
            return mytoken.Token(mytoken.PRINTLN, a, self.line, self.column)
        if a == 'print':
            return mytoken.Token(mytoken.PRINT, a, self.line, self.column)
        if a == 'true' or a == 'false':
            return mytoken.Token(mytoken.BOOL, a, self.line, self.column)
        if a == 'end':
            return mytoken.Token(mytoken.END, a, self.line, self.column)
        elif len(a)>0 and a[0].isalpha():#if it is not a recognized word it will be an id. 
            return mytoken.Token(mytoken.ID, a, self.line, self.column)
        else:
            raise error.Error('unrecognized symbol "'+a+'"',self.line,self.column)

           
