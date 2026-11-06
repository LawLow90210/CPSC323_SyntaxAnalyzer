#list of functions
#if that function 
import lexer

#functions / variable def
switch = False
#define current token using whatever lexeme we're on
token = '' 

# test file input & output storage variables

test_input = 'easyInput02.txt'
# test_input = 'hardInput.txt'
# test_input = 'hardInput.txt'
test_output = 'output.txt'

#Naming Conventions:
# * when printing a statement, capitalize functions and if they are a function prime write as "Function Prime"
# * when naming functions the names are lowercase and use snake case (ex: snake_case)
# * if a function has a name that is a keyword, write "function" then the keyword (ex: function_keyword)
# * if a function has a name that is shortened capital letters, the function will be named the full word and lowercase (ex: IDs is named identifier)
# * all functions are single words (ex: expression rather than expressions)

def rat26f():
	if switch:
		print('<Rat26F> ::= <Opt Function Definitions> @ <Opt Declaration List> @ <Statement List>')
	opt_function_definition()
	if token == '@':
		lexer()
	else: 
		print('Error')
	if token == '@':
		lexer()
		statement_list()
	else:
		print('Error')
	if not any:
		print('Error Rule: 1')

def function_if():
	if switch:
		print('<If> ::= if ( <Condition> ) <Statement> <If Prime>')
	if token == 'if':
		lexer()
	else:
		print('Error')
	if token == '(':
		lexer()
		condition()
	else:
			print('Error')
	if token == ')':
		lexer()
		statement()
		if_prime()
	if not any:
		print('Error Rule 18')

def identifiers():
	if switch:
		print ('<IDs> ::= <Identifier> <IDs_prime>')
	lexer()
	identifiers_prime()
	if not any:
			print('Error Rule 13')

def statement_list():
	if switch:
		print ('<Statement List> ::= <Statement> <Statement List Prime>')
	statement()
	statement_list_prime()
	if not any:
		print('Error Rule 14')

def function_return():
	if switch:
		print ('<Return> ::= return <Return Prime>')
	if token == 'return':
		lexer()
		return_prime()
	if not any: 
		print('Error Rule 19')

def return_prime():
	if switch:
		print ('<Return Prime> ::= ; | <Expression> ;')
	if token == ';':
		lexer()
	else: 
		expression>()
		lexer()
	if not any:
		print('Error Rule 35')

def primary():
	if switch:
		print ('<Primary> ::= <Identifier> <Primary_backtrack> | <Integer> <Primary Prime> | ( <Expression> ) <Primary Prime> | <Real> <Primary Prime> | true <Primary Prime> | false <Primary Prime>’')
	if token == 'identifer':
		lexer()
		primary_backtrack
	if token == 'integer' or 'real':
			lexer()
			primary_prime
	if token is '(':
		lexer()
		expression()
	if token == ')':
		primary_prime
	else:
		print('Error')
	if token is True or False:
		lexer()
		primary_prime()
	else:
		print('Error Rule 28')


def expression():
	if switch:
		print ('<Expression> ::= <Term> <Expression Prime>')
	term()
	expression_prime()
	#end of if
	if not any: 
			print('Error')
			#end of if

def function_definitions():
	if switch:
		print ('<Function Definitions> ::= <Function> <Function Definitions Prime>')
	function()
	function_definitions_prime()
	if not any:
		print('Error Rule 3')

def function_definitions_prime():
	if switch:
		print ('<Function Definitions Prime> ::= <Function Definitions> | epsilon')
	if token != None:
		function_definitions()
	if not any:
		print('Error Rule 40')
	else:
		None

def parameter_list():
	if switch:
		print ('<Parameter List> ::= <Parameter> <Parameter List Prime>')
	parameter()
	parameter_list_prime()
	if not any:
		print('Error Rule 6')

def parameter_list_prime():
	if switch:
		print ('<Parameter List Prime> ::= , <Parameter List> | epsilon')
	if token == ',':
		parameter_list()
	if not any:
		print('Error Rule 39')
	else:
		None

def declaration_list():
	if switch:
		print ('<Declaration List> := <Declaration> <Declaration List Prime>')
	declaration()
	declaration_list_prime()
	if not any:
		print('Error Rule 11')

def declaration_list_prime():
	if switch:
		print ('<Declaration List Prime> := ; | ; <Declaration List>')
	lexer()
	if token != None:
		declaration_list()
	else:
		None
	if not any:
		print('Error Rule 38')


def expression_prime():
	if switch:
		print ('<Expression Prime> := + <Term> <Expression Prime> | - <Term> <Expression Prime> | epsilon')
		if token == '+' or '-' or None:
			lexer()
			term()
			expression_prime()
			#end of if
	#end of if

def identifiers_prime():
	if switch:
		print ('<IDs_prime> ::=, <IDs> | epsilon')
	if token == ',':
		identifiers()
	if not any:
		print('Error Rule 37')
	else:
		None

def statement_list_prime():
	if switch:
		print ('<Statement List Prime> ::= <Statement List> | epsilon')
	if token != None:
		statement_list()
	if not any:
		print('Error Rule 36')
	else:
		None

def statement():
	if switch:
		print ('<Statement> ::= <Compound> | <Assign> | <If> | <Return> | <Print> | <Scan> | <While>')
	if token == '{':
		compound()	
	else: 
			print('Error')
	if token == 'identifier':
		assign()
	else:
		print('Error')
	if token == 'if':
		function_if()
	else:
		print('Error')
	if token == 'return':
		function_return()
	else: 
		print('Error')	
	if token == 'put':
		function_print()
	else:
		print('Error')
	if token == 'get':
		scan()
	else:
		print('Error')
	if token == 'while':
		function_while()
	else:
		print('Error')
	if not any:
		print('Error Rule 15')

def term():
	if switch:
		print ('<Term> ::= <Factor> <Term Prime>')
	factor()
	term_prime()
	#end of if
	if not any: 
			print('Error')
			#end of if

def term_prime():
	if switch:
		print ('<Term Prime> ::= * <Factor> <Term Prime> | / <Factor> <Term Prime> | epsilon')
		if token == '*' or '/' or None:
			lexer()
			factor()
			term_prime()
			#end of if
		if not any:
			print('Error')
	#end of if

def factor():
	if switch:
		print ('<Factor> ::= - <Primary> | <Primary>')
		if token == '-':
			lexer()
			primary()
		if not any:
			print('Error Rule 27')
	
def factor():
	if switch:
		print ('<Factor> ::= - <Primary> | <Primary>')
		#end of if

def empty():
	if switch:
		print ('<Empty> ::=')
	if token == None:
		lexer()
	if not any: 
			print('Error: Empty expected')
			#end of if

def primary_prime():
	if switch:
		print ('<Primary’> ::= <Term’> <Expression’> <Primary’> | epsilon')
		term()
		expression_prime()
		primary_prime()
		#end of if
	if not any:
		print('Error Rule 32')
		#end of if
		
def primary():
	if switch:
		print ('''<Primary> : : = <Indentifier> <Primary Prime> 
		        | <Integer> <Primary Prime> 
		        | <Identifier> ( <IDs> ) <Primary Prime> 
		        | ( <Expression> ) <Primary Prime> 
		        | <Real> <Primary Prime> 
		        | true Primary Prime 
		        | false Primary Prime''')
		#end if
	lexer()
	
	if token == '(':
		lexer()
		identifier()
		#end if
		
	if token == ')':
		lexer()
		#end if
	else:
		print('Error: ( expected ) ')
		#end else
	if token == 'true' or 'false':
		lexer()
		primary_prime()
		if not any:
			print('Error')
                #end of if

def relop():
	if switch:
		print ('<Relop> ::= == | != | > | < | <= | >=')
		#end if
	if token in ('==', '!=', '>', '<', '<=', '>='):
		lexer();
	if not any:
		print('Error Rule 24')
        #end of if

def function_while():
	if switch:
		print ('<While> : : = while ( <Condition> ) <Statement>')
		if token == 'while':
			lexer()
		else:
			print("Error: while expected")
	if token == '(':
			lexer()
			condition()
	else:
		print("Error: ( expected")
	if token == '(':
		lexer()
		statement()
	else:
		print("Error: ( expected")

def condition():
	if switch:
		print ('<Condition> ::= <Expression> <Condition Prime>')

	expression()
	condition_prime()

	if not any: 
		print('Error')
		# end if

def condition_prime():
	if switch:
		print ('<Condition Prime> ::= == <Expression> | != <Expression> | > <Expression> | < <Expression> | <= <Expression> | >=  <Expression> ')
		if token in ('==', '|', '!=', '|', '>', '|', '<', '|,' '<=', '|', '>='):
			lexer()
		expression()
		if not any: 
			print('Error')

def scan():
	if switch:
		print ('<Scan> : : = get ( <IDs> )')
		if token == 'get':
			lexer()
		else:
			print('Error: get expected')
		if token == '(':
			lexer()
		else:
			print('Error: get expected')

		# not sure if IDs and identifier are different :standing_man:
		identifiers() 
		
		if token == ')':
			lexer()
		else:
			print('Error: get expected')


def print():
	if switch:
		print ('<Print> ::= put ( <Expression>)')
		if token == 'put':
			lexer()
			# end if
		else:
			print('Error')
			# end else
			
		if token == '(':
			lexer()
			# end if
		else:
			print('Error')
			# end else
			
		expression()
		
		if token == ')':
			lexer()
			# end if
		else:
			print('Error')
			# end else
def assign():
	if switch:
		print ('<Assign> ::= <Identifier> = <Expression>')
	identifier()
	lexer()
	expression()
	# end if
	
def identifier():
	return

def compound():
	if switch:
		print ('<Compound> ::= { <Statement List> }')
	if token == '{':
		lexer()
	statement_list()
	if token == '}':
		lexer()

	if not any:
		print('Error Rule 16')

def assign():
	if switch:
		print('<Assign> ::= <Identifier> = <Expression>')
		if token == 'identifier':
			lexer()
		else:
			print('Error')
		if token == '=':
			lexer()
			expression()
	if not any:
		print('Error Rule 12')

def factor():
	if switch:
		print ('<Factor> ::= - <Primary> | <Primary>')
		if token == '-':
			lexer()

		primary()
		if not any: 
			print('Error')

def primary_backtrack():
	if switch:
		print ('<Primary_backtrack> ::= <Primary’> |  ( <IDs> ) <Primary’>')
		if token == '(':
			lexer()
			identifiers()
			if token == ')':
				lexer()
				primary_prime()
			else:
				print('Error')
		else:
			primary_prime()
		if not any:
			print('Error Rule 41')

def parameter_list():
	if switch:
		print ('<Parameter List> ::= <Parameter> <Parameter List Prime>')
		parameter()
		parameter_list_prime()
		if not any:
			print('Error Rule 6')


def declaration():
	if switch:
		print ('<Declaration> ::=  <Qualifier > <IDs>')
	qualifier()
	identifier()
	if not any:
		print('Error Rule 12')

def qualifier():
	print('TEST1: Entered qualifier() function')
	lexer()

def body():
	if switch:
		print ('<Body> ::= { < Statement List> }')
	if token == '{':
		lexer()
		# end if
	
	statement_list()
	
	if token == '}':
		lexer()
	else:
		print('Error')

	if not any:
		print('Error Rule 9')

def function_print():
	if switch:
		print('<Print> ::= put ( <Expression>)')
		if token == 'put':
			lexer()
		else:
			print('Error')
		if token == '(':
			lexer()
		else:
			print('Error')

		expression()

		if token == ')':
			lexer()
		else:
			print('Error')
	if not any:
		print('Error Rule 20')

def quantifier():
	if switch:
		print('<Qualifier> ::= integer | boolean | real')
	if token in ('integer', 'boolean', 'real'):
		lexer()
	if not any:
		print('Error Rule 8')

def parameter():
	if switch:
		print('<Parameter> ::= <IDs > <Qualifier>')
	identifier()
	quantifier()
	if not any:
		print('Error Rule 7')

def opt_parameter_list():
	if switch:
		print ('<Opt Parameter List> ::= <Parameter List> | <Empty>')
	if token is empty:
	    lexer()
	else:
	    parameter_list()
	if not any:
		print('Error Rule 5')

def parameter_list():
	print('TEST1: Entered parameter_list() function')
	lexer()

def opt_function_definition():
	if switch:
		print ('<Opt Function Definitions> ::= <Function Definitions> | <Empty>')
	if token is empty:
		lexer()
	else:
		function_definition()
	if not any:
		print('Error Rule 2')

def function_definition():
	print('TEST1: Entered function_definition() function')
	lexer()

def function():
	if switch:
		print ('<Function> ::= function <Identifier> ( <Opt Parameter List> ) <Opt Declaration List> <Body>')
		if token == 'function':
			lexer()
			identifier()
		else:
			print('Error')
		if token == '(':
			lexer()
			opt_parameter_list()
		if token == ')':
			lexer()
			opt_declaration_list()
			body()
		if not any:
			print('Error Rule 4') 

def opt_declaration_list():
	print('TEST1: Entered opt_declaration_list() function')
	lexer()

def if_prime():
	if switch:
		print ('<If Prime> ::=  fi | else <Statement> fi')
	if token == 'else':
		lexer()
		statement()
	else:
		print('Error')
	if token == 'fi':
		lexer()

	if not any:
		print('Error Rule 34')



# main testing location

with open(test_input, 'r') as file:
    input_text = file.read()

#tokens = lex(input_text)
i = 0
with open(test_output, 'w') as output:
    output.write(f'{"token":<15}lexeme\n')
    output.write('-' * 25 + '\n')
    while True:
        token_type, lexeme, i = lex(input_text, i)
        if token_type is None:
            break
        output.write(f'{token_type:<15}\t{lexeme}\n')

#syntaxAnalyzer :party:
class syntaxAnalyzer:
    def __init__(self, transitions, accepting, start='S'):
        self.transitions = transitions  # dict: (state, char_class) -> next_state
        self.accepting = accepting # dict: state -> token
        self.start = start

    def run(self, input_str, i):
        state = self.start #the starting state
        last_accept = None # the tokken typefor the longest accepted token
        last_end = i #the index right after last_accept

        #these are our pointers helping us step through the code
        j = i 

        #while the pointer is smaller than the length of the input
        #go to the next transtion and get that information
        #if the next transition doesnt exist, break
        while j < len(input_str):
            next_transition = self.transitions.get((state, char_class(input_str[j])))
            if next_transition is None:
                break
            state = next_transition
            j += 1
            
            if state in self.accepting: # if state does exist,
                #pointer goes one forward
                #if the state is an accepting state, the whole token can be read
                #stores 2 things: the token type, and the index
                last_accept = self.accepting[state]
                last_end = j
        return last_accept, last_end #return the whole accepted token and the index where it ended

	
