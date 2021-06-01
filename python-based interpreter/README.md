Intro: in my organization of programming languages class, a major project that I really enjoyed was building an interpreter for a custom, rudimentary, text-file based language. 
Our professor defined the rules of the language and provided a few templates. For our purposes, we did not implement classes, inheritance, libraries, or scripts in this new text language. 
Instead the focus on was on variable scope, variable environment, if/while statements, data structures, and boolean and arithmetic operations. The entirety of the project consists of
a symbol_table file, tokenizer, lexer, parser, AST generator, an error catcher, and, finally, the interpreter. In this listing, each file builds on and uses the previous file.

The symbol table keeps track of symbol values based on scope. It includes functions to add or pop environments, as the same variable symbol can have different values at different scopes.

The tokenizer looks for special words (like "if", "+", or "true"). Before the tokenizer, these special words are just strings.

The lexer works closely with the tokenizer to convert the tokens made from the tokenizer into grammatically valid operations. For example, if we come across an "if", we know that we can expect to create an if statement operation. The lexer is also equipped in finding potential errors.

The abstract syntax tree generator works with the output of the lexer to finally define in what order and in what way the code is compiled. 

The interpreter takes a textfile as if it were source code, and runs the program on it, ultimately defining the output and effects of the code. 

testfiles 1 and 2 offer testing opportunities for various concepts.
