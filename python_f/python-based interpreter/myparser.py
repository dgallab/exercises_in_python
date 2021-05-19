#Daniel Gallab
#CPSC 326-02
#Assignment 4 
#examines the token sequence to
#determine if the sequence follows
#the set of grammar rules provided
#while building a parse tree

import lexer
import mytoken
import error
import mypl_ast as ast #contains the structs needed for the abstract syntax tree

class Parser(object):
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = None
    
    def parse(self):
        stmt_lst_node=ast.StmtList()
        self.advance()
        self.stmts(stmt_lst_node)
        self.eat(mytoken.EOS, 'expecting end of file')
        return stmt_lst_node
    # helper functions:
    
    def advance(self):
        self.current_token = self.lexer.next_token()
        
    def eat(self, mytokentype, error_msg):
        if self.current_token.tokentype == mytokentype:
            self.advance()
        else:
            self.error(error_msg)
            
    def error(self, error_msg):
        s = error_msg +  "found " + self.current_token.lexeme + '"'
        l = self.current_token.line
        c = self.current_token.column
        raise error.Error(error_msg, l, c)
    
    def stmts(self,stmt_lst_node):
        tokens = [mytoken.IF, mytoken.WHILE, mytoken.PRINT, mytoken.PRINTLN, mytoken.ID]
        if self.current_token.tokentype not in tokens:
            return
        s = self.stmt(stmt_lst_node)
        self.stmts(stmt_lst_node)
        return s
        
    def stmt(self,stmt_lst_node): #the first child from the stmt_lst_node (root)
        #<output> the x variable is crucial in determining whether the statement should be appended to the root node, or
        #not, because it is already appended to another node
        if self.current_token.tokentype == mytoken.PRINT or self.current_token.tokentype == mytoken.PRINTLN:
            print_node = ast.PrintStmt()
            if self.current_token.tokentype == mytoken.PRINTLN:
                print_node.is_println=True
            self.advance()
            self.eat(mytoken.LPAREN, 'expecting "("')
            print_node.expr = self.expr() #
            self.eat(mytoken.RPAREN, 'expecting ")"')
            self.eat(mytoken.SEMICOLON, 'expecting ";"')
            stmt_lst_node.stmts.append(print_node)
            return print_node

        #<assign>
        elif self.current_token.tokentype == mytoken.ID:
            assign_node = ast.AssignStmt()
            assign_node.lhs = self.current_token
            self.advance()
            expr = self.listindex() #listindex may not exist- in that case, only the lhs attribute matters
            assign_node.index_expr = expr
            self.eat(mytoken.ASSIGN, 'expecting "="')
            assign_node.rhs = self.expr()
            self.eat(mytoken.SEMICOLON, 'expecting ";"')
            stmt_lst_node.stmts.append(assign_node)
            return assign_node
        #<cond>
        elif self.current_token.tokentype == mytoken.IF:
            basic_if = ast.BasicIf() #start by making a basic if
            self.advance()
            basic_if.bool_expr = self.bexpr() #add the first bool expression
            
            self.eat(mytoken.THEN, 'expecting "then"')
            s = ast.StmtList() #create a new instance of statement list node
            self.stmts(s)
            basic_if.stmt_list = s 
            if_node = ast.IfStmt()  
            if_node.if_part = basic_if
            if_node = self.condt(if_node, stmt_lst_node) #if statement's attributes are defined in the condt statment
            self.eat(mytoken.END, 'expecting "end"') #may be identical to the basic if node if condt is empty
            stmt_lst_node.stmts.append(if_node)
            return if_node
        #<loop>
        elif self.current_token.tokentype == mytoken.WHILE:
            while_node = ast.WhileStmt()
            self.advance()
            while_node.bool_expr = self.bexpr() 
            self.eat(mytoken.DO, 'expecting "do"')
            s = ast.StmtList()  #create a new instance of statement list node
            self.stmts(s)
            while_node.stmt_list = s 
            self.eat(mytoken.END, 'expecting "end"')# want the statement appended twice to different nodes
            stmt_lst_node.stmts.append(while_node)
            return while_node
            
        else: 
            l = self.current_token.line
            c = self.current_token.column
            raise error.Error('not a valid statement at:',l,c)
        
    def condt(self, if_node, stmt_lst_node):
        #if neither of the if statements are true, then the if node will be similar to the basic if n
         if self.current_token.tokentype == mytoken.ELSEIF:
             basic_if = ast.BasicIf()
             self.eat(mytoken.ELSEIF, 'expecting "elseif"')
             basic_if.bool_expr = self.bexpr() 
             self.eat(mytoken.THEN, 'expecting "then"')
             s = ast.StmtList()
             self.stmts(s)
             basic_if.stmt_list = s
             if_node.elseifs.append(basic_if) #can have any number of else ifs
             self.condt(if_node, stmt_lst_node)
         elif self.current_token.tokentype == mytoken.ELSE:
            if_node.has_else = True #only one else
            self.eat(mytoken.ELSE, 'expecting "else"')
            s = ast.StmtList()
            self.stmts(s)
            if_node.else_stmts = s
         return if_node
        

    def expr(self): # start by defining the simple_expr_node- the exprt will determine if it is
        #a complex_expr_node
        simple_expr_node = ast.SimpleExpr()
        node = self.value(simple_expr_node)
        node = self.exprt(node)
        return node
        
    def value(self, simple_expr_node): #5 different types of values, one imbedded in ID
        if self.current_token.tokentype == mytoken.ID:
            index_expr_node = ast.IndexExpr()
            simple_expr_node.term = self.current_token
            self.advance()
            if self.current_token.tokentype != mytoken.LBRACKET: #we need to know beforehand which node we are returning
                return simple_expr_node
            index_expr_node.identifier = simple_expr_node.term
            index_expr_node.expr = self.listindex()
            return index_expr_node   
        elif (self.current_token.tokentype == mytoken.STRING or self.current_token.tokentype == mytoken.INT
        or self.current_token.tokentype == mytoken.BOOL):
            simple_expr_node.term = self.current_token
            self.advance()
            return simple_expr_node
        #<input> has only one way to call it- so, we do not need a function for it
        elif self.current_token.tokentype == mytoken.READINT or self.current_token.tokentype == mytoken.READSTR:
            read_expr_node = ast.ReadExpr()
            if self.current_token.tokentype == mytoken.READINT:
                read_expr_node.is_read_int = True
            self.advance()
            self.eat(mytoken.LPAREN, 'expecting "("')
            read_expr_node.msg = self.current_token
            self.eat(mytoken.STRING, 'expecting "STRING"')
            self.eat(mytoken.RPAREN, 'expecting ")"')
            return read_expr_node
        elif self.current_token.tokentype == mytoken.LBRACKET:
            list_expr_node = ast.ListExpr()
            self.advance()
            if self.current_token.tokentype != mytoken.RBRACKET:
                self.exprlist(list_expr_node)
            else:
                self.eat(mytoken.RBRACKET, 'expecting "]"')
            return list_expr_node
        else:
            raise error.Error('not a valid value',self.current_token.line,self.current_token.column)

    def listindex(self): #used for lists
        if self.current_token.tokentype == mytoken.LBRACKET:
            self.advance()
            expr = self.expr()
            self.eat(mytoken.RBRACKET, 'expecting "]"')
            return expr
        
        else: #if the nextmytoken is not a left bracket,
            return 

    def exprlist(self,list_expr_node): #we took care of the empty case in the value function
        list_expr_node.expressions.append(self.expr())
        self.exprtail(list_expr_node)
        
    def exprtail(self,list_expr_node):
        if self.current_token.tokentype != mytoken.COMMA:
            self.advance()#empty case
            return
        self.eat(mytoken.COMMA, 'expecting ","')
        list_expr_node.expressions.append(self.expr())
        self.exprtail(list_expr_node)       
    
    def exprt(self, node): #takes in a simple_expr_node as a parameter to determine if it is complex
        complex_expr_node = ast.ComplexExpr()
        complex_expr_node.first_operand = node
        if (self.current_token.tokentype != mytoken.PLUS and self.current_token.tokentype != mytoken.MINUS and
        self.current_token.tokentype != mytoken.MULTIPLY and self.current_token.tokentype != mytoken.DIVIDE and
        self.current_token.tokentype != mytoken.MODULUS):
            return node #return the simple expression node since exprt is empty
        else:
            complex_expr_node.math_rel = self.math_rel()
            complex_expr_node.rest = self.expr()
            return complex_expr_node 
           
                 
    def math_rel(self): #returns the operator (for complex expressions)
        if self.current_token.tokentype == mytoken.PLUS:
            x=self.current_token
            self.eat(mytoken.PLUS, 'expecting "+"')
            return x
        elif self.current_token.tokentype == mytoken.MINUS:
            x=self.current_token
            self.eat(mytoken.MINUS, 'expecting "-"')
            return x
        elif self.current_token.tokentype == mytoken.MULTIPLY:
            x=self.current_token
            self.eat(mytoken.MULTIPLY, 'expecting "*"')
            return x
        elif self.current_token.tokentype == mytoken.DIVIDE:
            x=self.current_token
            self.eat(mytoken.DIVIDE, 'expecting "/"')
            return x
        elif self.current_token.tokentype == mytoken.MODULUS:
            x=self.current_token
            self.eat(mytoken.MODULUS, 'expecting "%"')
            return x
        else:
            raise error.Error('not a valid math operator',self.current_token.line,self.current_token.column)

    def bexpr(self): #similar structure to the expression function
        simple_bool_expr = ast.SimpleBoolExpr()
        if self.current_token.tokentype == mytoken.NOT:
            self.eat(mytoken.NOT, 'expecting "NOT"')
            simple_bool_expr.negated = True
        simple_bool_expr.expr = self.expr()
        node = self.bexprt(simple_bool_expr)  
        return node

    def bexprt(self,node1):
        complex_bool_expr_node = ast.ComplexBoolExpr()
        complex_bool_expr_node.negated = node1.negated
        complex_bool_expr_node.first_expr = node1.expr
        if (self.current_token.tokentype == mytoken.EQUAL or self.current_token.tokentype == mytoken.LESS_THAN or
        self.current_token.tokentype == mytoken.NOT_EQUAL or self.current_token.tokentype == mytoken.GREATER_THAN_EQUAL or
        self.current_token.tokentype == mytoken.GREATER_THAN or self.current_token.tokentype == mytoken.LESS_THAN_EQUAL):
            complex_bool_expr_node.bool_rel = self.bool_rel()
            complex_bool_expr_node.second_expr = self.expr()
            if self.current_token.tokentype == mytoken.AND:
                complex_bool_expr_node.has_bool_connector = True
                complex_bool_expr_node.bool_connector = self.current_token
            if self.current_token.tokentype == mytoken.OR:
                complex_bool_expr_node.has_bool_connector = True
                complex_bool_expr_node.bool_connector = self.current_token
            complex_bool_expr_node.rest = self.bconnct()
            return complex_bool_expr_node
        else: #empty case means it is a simple boolean expression
            return node1

    def bool_rel(self): #returns a boolean operator
        if self.current_token.tokentype == mytoken.EQUAL:
            x = self.current_token
            self.eat(mytoken.EQUAL, 'expecting "=="')
            return x
        elif self.current_token.tokentype == mytoken.NOT_EQUAL:
            x = self.current_token
            self.eat(mytoken.NOT_EQUAL, 'expecting "!="')
            return x
        elif self.current_token.tokentype == mytoken.LESS_THAN:
            x = self.current_token
            self.eat(mytoken.LESS_THAN, 'expecting "<"')
            return x
        elif self.current_token.tokentype == mytoken.LESS_THAN_EQUAL:
            x = self.current_token
            self.eat(mytoken.LESS_THAN_EQUAL, 'expecting "<="')
            return x
        elif self.current_token.tokentype == mytoken.GREATER_THAN:
            x = self.current_token
            self.eat(mytoken.GREATER_THAN, 'expecting ">"')
            return x
        elif self.current_token.tokentype == mytoken.GREATER_THAN_EQUAL:
            x = self.current_token
            self.eat(mytoken.GREATER_THAN_EQUAL, 'expecting ">="')
            return x
        else:
            raise error.Error('not a valid boolean operator',self.current_token.line,self.current_token.column)

    def bconnct(self): #returns a boolean connective if any
        if self.current_token.tokentype == mytoken.AND:
            self.eat(mytoken.AND, 'expecting "and"')
            return self.bexpr()
        elif self.current_token.tokentype == mytoken.OR:
            self.eat(mytoken.OR, 'expecting "or"')
            return self.bexpr()
        else: #empty case
            return     
         
         
            
            
            
            
            
            
            
            
            
            
            
            
            
        
       
