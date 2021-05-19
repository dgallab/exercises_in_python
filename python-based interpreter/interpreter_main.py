#Daniel Gallab
#CPSC 326-02
#main
#first calls the lexer class to gather
#tokens, then calls the parser class to examine
#sequence of tokens for correctness, then
#calls the ast class to construct an abstract
#syntax tree based on the sequence
#then calls the type checker to ensure the code
#is type safe
#then interprets the code (runs it as program)

import sys
import lexer
import myparser
import error
import mypl_ast_printer as ast_printer
import mypl_interpreter as interpreter

def main(testfile2):
    try:
        file_stream = open(testfile2, 'r')
        the_lexer = lexer.Lexer(file_stream)
        the_parser = myparser.Parser(the_lexer)
        stmt_list = the_parser.parse()
        print_visitor = ast_printer.ASTPrintVisitor(sys.stdout)
        stmt_list.accept(print_visitor)
        #checker = type_checker.TypeChecker()
        #stmt_list.accept(checker)
        itpr = interpreter.Interpreter()
        stmt_list.accept(itpr)

        #print out AST tree
    except IOError as e: #if file cannot be found
        print ("error: unable to open file '" + filename + "'")
        sys.exit(1)
    except error.Error as e:
        print (e)
        sys.exit(1)
        
if __name__ == '__main__':
   main("testfile2.txt")
   if len(sys.argv) != 2:
       print ('usage:', sys.argv[0], 'source-code-file')
       sys.exit(1)
   else:
       main(sys.argv[1])
