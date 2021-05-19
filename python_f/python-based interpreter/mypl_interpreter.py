#Daniel Gallab
#CPSC 326-02
#interprets program functions 


import mypl_ast as ast
import mypl_symbol_table as symbol_table
import error
import sys

class Interpreter(ast.Visitor):
    
    def __init__(self):
        self.sym_table = symbol_table.SymbolTable()
        self.current_value = None
       
    def __write(self,msg): #used instead of print because print in python is equivalent to println
        sys.stdout.write(str(msg))
       
    def visit_stmt_list(self, stmt_list):
        self.current_value = None 
        self.sym_table.push_environment()
        for stmt in stmt_list.stmts:
            stmt.accept(self)
        self.sym_table.pop_environment()
        
           
    def visit_simple_bool_expr(self, simple_bool_expr): 
         simple_bool_expr.expr.accept(self)
         if type(simple_bool_expr.expr) == ast.SimpleExpr: # must look into other nodes to determine type of the expression
            term = simple_bool_expr.expr.term #because of type checking we can assume it is a bool type
            if term.lexeme == 'true':
                self.current_value = True
            elif term.lexeme == 'false':
                self.current_value = False
         if term.tokentype == 'ID': 
            self.current_value = self.sym_table.get_variable_value(term.lexeme)
         if simple_bool_expr.negated:
             self.current_value = not(self.current_value) #if negated, then value becomes the opposite 
           
            
    def visit_complex_bool_expr(self, complex_bool_expr):
        complex_bool_expr.first_expr.accept(self)
        x=self.current_value #for each token, use the counterparts in python
        complex_bool_expr.second_expr.accept(self)
        if complex_bool_expr.bool_rel.tokentype == 'NOT_EQUAL':
            if x != self.current_value:
                self.current_value = True
            else:
                self.current_value = False
        if complex_bool_expr.bool_rel.tokentype == 'EQUAL':
            if x == self.current_value:
                self.current_value = True
            else:
                self.current_value = False
        elif complex_bool_expr.bool_rel.tokentype == 'GREATER_THAN_EQUAL':
            if x >= self.current_value:
                self.current_value = True
            else:
                self.current_value = False
        elif complex_bool_expr.bool_rel.tokentype == 'LESS_THAN_EQUAL':
            if x <= self.current_value:
                self.current_value = True
            else:
                self.current_value = False
        elif complex_bool_expr.bool_rel.tokentype == 'GREATER_THAN':
            if x > self.current_value:
                self.current_value = True
            else:
                self.current_value = False
        elif complex_bool_expr.bool_rel.tokentype == 'LESS_THAN':
            if x < self.current_value:
                self.current_value = True
            else:
                self.current_value = False
        if complex_bool_expr.negated:
            self.current_value = not(self.current_value)
        if complex_bool_expr.has_bool_connector:
            y = self.current_value #store the boolean value in a variable
            complex_bool_expr.rest.accept(self)
            if complex_bool_expr.bool_connector.tokentype == 'AND':
                self.current_value = self.current_value and y 
            else:
                self.current_value = self.current_value or y
            
              
    def visit_if_stmt(self, if_stmt):
        x = True
        if_stmt.if_part.bool_expr.accept(self)
        if self.current_value:
            if_stmt.if_part.stmt_list.accept(self)
        else: #used if initial if statements are not run
            for elseif in if_stmt.elseifs:
                elseif.bool_expr.accept(self)
                if self.current_value and x:
                    elseif.stmt_list.accept(self)
                    x = False                 
            if if_stmt.has_else and x: #if none of the else if statements were run, then x will be True
                #only if none of the ifs are true, the elses are run
                if_stmt.else_stmts.accept(self)
            
        
    def visit_while_stmt(self, while_stmt): 
         while_stmt.bool_expr.accept(self)
         while self.current_value:
             while_stmt.stmt_list.accept(self)
             while_stmt.bool_expr.accept(self)#must constantly reevaluate bool expr
             
    def visit_print_stmt(self, print_stmt):
        print_stmt.expr.accept(self)
        self.__write(self.current_value)
        if print_stmt.is_println:
            self.__write('\n')
       
       
    def visit_assign_stmt(self, assign_stmt):
        assign_stmt.rhs.accept(self)
        if not self.sym_table.variable_exists(assign_stmt.lhs.lexeme):
            self.sym_table.add_variable(assign_stmt.lhs.lexeme)
        if assign_stmt.index_expr == None: #if it is an index expression, then the identifier is not enough to get the correct value
            self.sym_table.set_variable_value(assign_stmt.lhs.lexeme,self.current_value)
        else: #store current value in a variable- this is the rhs value
             y = self.current_value
             x = self.sym_table.get_variable_value(assign_stmt.lhs.lexeme)#x is a list
             assign_stmt.index_expr.accept(self) #current value is now the value inside the brackets
             if self.current_value <0 or self.current_value>=len(x): #checks to see if it is in range, if not raise error
                term = assign_stmt.lhs
                raise error.Error('list index for '+term.lexeme+ ' out of range ',term.line,term.column+1)   
             x[self.current_value] = y;
             self.sym_table.set_variable_value(assign_stmt.lhs.lexeme,x) #goes back into listid's value to change the list
        self.current_value = None
                   
                                       
    def visit_simple_expr(self, simple_expr):
        if  simple_expr.term.tokentype == 'ID':
            var_name = simple_expr.term.lexeme
            var_val = self.sym_table.get_variable_value(var_name)
            self.current_value = var_val
        elif simple_expr.term.tokentype == 'INT':
           self.current_value = int(simple_expr.term.lexeme)   
        elif simple_expr.term.tokentype == 'BOOL': 
            if simple_expr.term.lexeme == 'true': #true should be equivalent to True, not the string value
                self.current_value = True
            else:#same for false
                self.current_value = False
        elif simple_expr.term.tokentype == 'STRING':
            self.current_value = simple_expr.term.lexeme[1:len(simple_expr.term.lexeme)-1]
          
    def visit_index_expr(self, index_expr):  
        index_expr.expr.accept(self) #finds the correct value in the list specified by the identifier
        x = self.sym_table.get_variable_value(index_expr.identifier.lexeme)
        if self.current_value <0 or self.current_value>=len(x): #raises an error if no such value exists (out of range)
            term = index_expr.identifier
            raise error.Error('list index for '+term.lexeme+ ' out of range ',term.line,term.column+1)
        self.current_value = x[self.current_value]
        
    def visit_list_expr(self, list_expr):
         x=[]; #start with an empty list 
         for expr in list_expr.expressions:
             expr.accept(self)
             x=x+[self.current_value] #add items to list
         self.current_value = x #current value becomes entire list
            
    def visit_read_expr(self, read_expr):
        val=input(read_expr.msg.lexeme) #readstr can take any input/readint must take an int
        if read_expr.is_read_int : #if not, then 0 is used as a default value
            try:
                self.current_value = int(val);
            except ValueError:
                self.current_type = 0
        else:
            self.current_value = val
                   
    def visit_complex_expr(self, complex_expr):
        complex_expr.first_operand.accept(self)
        x=self.current_value
        complex_expr.rest.accept(self)
        if complex_expr.math_rel.tokentype == 'PLUS':
            self.current_value = x + self.current_value #python allows direct string and list addition- no need to distinguish between them
        elif complex_expr.math_rel.tokentype == 'MINUS':
            self.current_value = x - self.current_value
        elif complex_expr.math_rel.tokentype == 'MULTIPLY':
            self.current_value = x * self.current_value
        elif complex_expr.math_rel.tokentype == 'DIVIDE':
            self.current_value = x / self.current_value
        elif complex_expr.math_rel.tokentype == 'MODULUS':
             self.current_value = x % self.current_value
       
        
        
