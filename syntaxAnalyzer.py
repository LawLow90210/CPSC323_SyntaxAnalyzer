#imports
import lexer
import sys

# Tells the parser to keep going, false just prints tokens
SWITCH = True
# list of (type, lexeme, line) imported from the tokenize function in lexer
tokens = []
# index of the current token
pos = 0
# the output file
out = None

# list of qualifiers
QUALIFIERS = ('integer', 'boolean', 'real')
# lis of operations
OPERATORS = ('==', '!=', '>', '<', '<=', '>=')

# special error class for when parsing fails
class ParseError(Exception):
	pass

# test file input & output storage variables

test_input = 'easyInput.txt'
# test_input = 'hardInput.txt'
# test_input = 'hardInput.txt'
test_output = 'output.txt'

#helper functions

# returns current positions type
def cur_type(): 
	return tokens[pos][0]
# returns current positions lexeme
def cur_lex():  
	return tokens[pos][1]
# returns current line 
def cur_line(): 
	return tokens[pos][2]

# true if the current token is this keyword or seperator or operator
def is_(lexeme):
	# making it easier to read
    type, lexeme_name, _ = tokens[pos]
	# if type is a keyword, check regardless of case that the lexeme matches one of the lexemes 
    if type == 'keyword':
        return lexeme_name.lower() == lexeme
    return type in ('separator', 'operator') and lexeme_name == lexeme

# writes the token to the output file
def show_token():
    if cur_type() != 'eof':
        out.write(f'Token: {cur_type().capitalize():<12} Lexeme: {cur_lex()}\n')

# moves to the next token instead of using lexer since that wasn't working
def advance():
    global pos
    if cur_type() != 'eof':
        pos += 1
        show_token()

# prints the rule of the function to the output file if switch is true 
def rule(text):
    if SWITCH:
        out.write(text + '\n')

# formattig for error messages 
def error(kind, msg):
    lex = cur_lex() if cur_type() != 'eof' else 'end of file'
    if cur_type() == 'unknown':
        kind = 'Invalid token'
    raise ParseError(f'Syntax Error ({kind}) | line {cur_line()} | '
                     f'token: {cur_type()} | lexeme: {lex} | {msg}')

# current token must be this lexeme, advance or print an error
def expect(lexeme):
    if is_(lexeme):
        advance()
    else:
        error('Missing/unexpected symbol', f"expected '{lexeme}'")

# helper for building a statement
def starts_statement():
    return (cur_type() == 'identifier' or
            any(is_(x) for x in ('{', 'if', 'return', 'put', 'get', 'while')))


#Naming Conventions:
# * when printing a statement, capitalize functions and if they are a function prime write as "Function Prime"
# * when naming functions the names are lowercase and use snake case (ex: snake_case)
# * if a function has a name that is a keyword, write "function" then the keyword (ex: function_keyword)
# * if a function has a name that is shortened capital letters, the function will be named the full word and lowercase (ex: IDs is named identifier)
# * all functions are single words (ex: expression rather than expressions)

# starting functions

def rat26f():
    rule('<Rat26F> -> <Opt Function Definitions> @ <Opt Declaration List> @ <Statement List>')
    opt_function_definitions()
    expect('@')
    opt_declaration_list()
    expect('@')
    statement_list()
    if cur_type() != 'eof':
        error('Unexpected token', 'extra tokens after the end of the program')

def empty():
    rule('<Empty> -> epsilon')

def opt_function_definitions():
    if is_('function'):
        rule('<Opt Function Definitions> -> <Function Definitions>')
        function_definitions()
    else:
        rule('<Opt Function Definitions> -> <Empty>')
        empty()

def opt_declaration_list():
    if cur_type() == 'keyword' and cur_lex().lower() in QUALIFIERS:
        rule('<Opt Declaration List> -> <Declaration List>')
        declaration_list()
    else:
        rule('<Opt Declaration List> -> <Empty>')
        empty()

def opt_parameter_list():
    if cur_type() == 'identifier':
        rule('<Opt Parameter List> -> <Parameter List>')
        parameter_list()
    else:
        rule('<Opt Parameter List> -> <Empty>')
        empty()

# functions and parameters

def function_definitions():
    rule('<Function Definitions> -> <Function> <Function Definitions Prime>')
    function()
    function_definitions_prime()

def function_definitions_prime():
    if is_('function'):
        rule('<Function Definitions Prime> -> <Function Definitions>')
        function_definitions()
    else:
        rule('<Function Definitions Prime> -> epsilon')

def function():
    rule('<Function> -> function <Identifier> ( <Opt Parameter List> ) <Opt Declaration List> <Body>')
    expect('function')
    identifier()
    expect('(')
    opt_parameter_list()
    expect(')')
    opt_declaration_list()
    body()

def parameter_list():
    rule('<Parameter List> -> <Parameter> <Parameter List Prime>')
    parameter()
    parameter_list_prime()

def parameter_list_prime():
    if is_(','):
        rule('<Parameter List Prime> -> , <Parameter List>')
        advance()
        parameter_list()
    else:
        rule('<Parameter List Prime> -> epsilon')

def parameter():
    rule('<Parameter> -> <IDs> <Qualifier>')
    identifiers()
    qualifier()

def qualifier():                    # your old one was misspelled "quantifier"
    rule('<Qualifier> -> integer | boolean | real')
    if cur_type() == 'keyword' and cur_lex().lower() in QUALIFIERS:
        advance()
    else:
        error('Missing type', "expected 'integer', 'boolean' or 'real'")

def body():
    rule('<Body> -> { <Statement List> }')
    expect('{')
    statement_list()
    expect('}')

#Declarations and ID's

def declaration_list():
    rule('<Declaration List> -> <Declaration> ; <Declaration List Prime>')
    declaration()
    expect(';')
    declaration_list_prime()

def declaration_list_prime():
    if cur_type() == 'keyword' and cur_lex().lower() in QUALIFIERS:
        rule('<Declaration List Prime> -> <Declaration List>')
        declaration_list()
    else:
        rule('<Declaration List Prime> -> epsilon')

def declaration():
    rule('<Declaration> -> <Qualifier> <IDs>')
    qualifier()
    identifiers()

def identifiers():
    rule('<IDs> -> <Identifier> <IDs Prime>')
    identifier()
    identifiers_prime()

def identifiers_prime():
    if is_(','):
        rule('<IDs Prime> -> , <IDs>')
        advance()
        identifiers()
    else:
        rule('<IDs Prime> -> epsilon')

def identifier():                   # replaces your "return" stub
    if cur_type() == 'identifier':
        advance()
    else:
        error('Missing identifier', 'expected an identifier')

# Statements

def statement_list():
    rule('<Statement List> -> <Statement> <Statement List Prime>')
    statement()
    statement_list_prime()

def statement_list_prime():
    if starts_statement():          # NOT "token != None", which would try to parse a } as a statement
        rule('<Statement List Prime> -> <Statement List>')
        statement_list()
    else:
        rule('<Statement List Prime> -> epsilon')

def statement():
    if is_('{'):
        rule('<Statement> -> <Compound>');  compound()
    elif cur_type() == 'identifier':
        rule('<Statement> -> <Assign>');    assign()
    elif is_('if'):
        rule('<Statement> -> <If>');        function_if()
    elif is_('return'):
        rule('<Statement> -> <Return>');    function_return()
    elif is_('put'):
        rule('<Statement> -> <Print>');     function_print()
    elif is_('get'):
        rule('<Statement> -> <Scan>');      scan()
    elif is_('while'):
        rule('<Statement> -> <While>');     function_while()
    else:
        error('Invalid statement', 'expected the start of a statement')

def compound():
    rule('<Compound> -> { <Statement List> }')
    expect('{')
    statement_list()
    expect('}')

def assign():
    rule('<Assign> -> <Identifier> = <Expression> ;')
    identifier()
    expect('=')
    expression()
    expect(';')

def function_if():
    rule('<If> -> if ( <Condition> ) <Statement> <If Prime>')
    expect('if')
    expect('(')
    condition()
    expect(')')
    statement()
    if_prime()

def if_prime():
    if is_('fi'):
        rule('<If Prime> -> fi')
        advance()
    elif is_('else'):
        rule('<If Prime> -> else <Statement> fi')
        advance()
        statement()
        expect('fi')
    else:
        error('Missing symbol', "expected 'fi' or 'else'")

def function_return():
    rule('<Return> -> return <Return Prime>')
    expect('return')
    return_prime()

def return_prime():
    if is_(';'):
        rule('<Return Prime> -> ;')
        advance()
    else:
        rule('<Return Prime> -> <Expression> ;')
        expression()
        expect(';')

def function_print():
    rule('<Print> -> put ( <Expression> ) ;')
    expect('put')
    expect('(')
    expression()
    expect(')')
    expect(';')

def scan():
    rule('<Scan> -> get ( <IDs> ) ;')
    expect('get')
    expect('(')
    identifiers()
    expect(')')
    expect(';')

def function_while():
    rule('<While> -> while ( <Condition> ) <Statement>')
    expect('while')
    expect('(')
    condition()
    expect(')')
    statement()

# Conditions and expressions

def condition():
    rule('<Condition> -> <Expression> <Relop> <Expression>')
    expression()
    relop()
    expression()

def relop():
    rule('<Relop> -> == | != | > | < | <= | >=')
    if cur_type() == 'operator' and cur_lex() in OPERATORS:
        advance()
    else:
        error('Missing operator', 'expected a relational operator')

def expression():
    rule('<Expression> -> <Term> <Expression Prime>')
    term()
    expression_prime()

def expression_prime():
    if is_('+') or is_('-'):
        rule(f'<Expression Prime> -> {cur_lex()} <Term> <Expression Prime>')
        advance()
        term()
        expression_prime()
    else:
        rule('<Expression Prime> -> epsilon')

def term():
    rule('<Term> -> <Factor> <Term Prime>')
    factor()
    term_prime()

def term_prime():
    if is_('*') or is_('/'):
        rule(f'<Term Prime> -> {cur_lex()} <Factor> <Term Prime>')
        advance()
        factor()
        term_prime()
    else:
        rule('<Term Prime> -> epsilon')

def factor():
    if is_('-'):
        rule('<Factor> -> - <Primary>')
        advance()
        primary()
    else:
        rule('<Factor> -> <Primary>')
        primary()

def primary():
    if cur_type() == 'identifier':
        rule('<Primary> -> <Identifier> <Primary Prime>')
        advance()
        primary_prime()
    elif cur_type() == 'integer':
        rule('<Primary> -> <Integer>')
        advance()
    elif cur_type() == 'real':
        rule('<Primary> -> <Real>')
        advance()
    elif is_('('):
        rule('<Primary> -> ( <Expression> )')
        advance()
        expression()
        expect(')')
    elif is_('true'):
        rule('<Primary> -> true')
        advance()
    elif is_('false'):
        rule('<Primary> -> false')
        advance()
    else:
        error('Invalid expression', 'expected an identifier, number, ( , true or false')

def primary_prime():
    if is_('('):
        rule('<Primary Prime> -> ( <IDs> )')
        advance()
        identifiers()
        expect(')')
    else:
        rule('<Primary Prime> -> epsilon')

# Driver 

def run(in_name, out_name):
    global tokens, pos, out
    with open(in_name, 'r') as f:
        tokens = lexer.tokenize(f.read())
    pos = 0
    with open(out_name, 'w') as out:
        try:
            show_token()                 # print the first token
            rat26f()
            out.write('\nParsing finished: no syntax errors found.\n')
        except ParseError as e:
            out.write('\n' + str(e) + '\n')   # error type, line, token, lexeme

if __name__ == '__main__':
    infile = sys.argv[1] if len(sys.argv) > 1 else test_input
    outfile = sys.argv[2] if len(sys.argv) > 2 else test_output
    run(infile, outfile)


	
