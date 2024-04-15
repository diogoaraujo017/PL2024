import ply.lex as lex

# List of token names. 
tokens = (
    'SELECT',
    'FROM',
    'WHERE',
    'INFO',
    'NUMBER',
    'FLOAT', 
    'EQUAL',
    'GREATER',
    'LESS',
    'COMMA',
)

# Regular expression rules for simple tokens
t_SELECT = r'[Ss][Ee][Ll][Ee][Cc][Tt]'
t_FROM = r'[Ff][Rr][Oo][Mm]'
t_WHERE = r'[Ww][Hh][Ee][Rr][Ee]'

t_INFO = r'\w+'

t_NUMBER = r'\d+'
t_FLOAT = r'\d+\.\d+'
t_EQUAL = r'\='
t_GREATER = r'\>'
t_LESS = r'\<'
t_COMMA = r'\,'

t_ignore = " \t"

# New line check
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    
# Build the lexer
lexer = lex.lex()

testQuery = "Select id, nome, salario From empregados Where salario >= 820"

lexer.input(testQuery)

while tok := lexer.token():
    print(tok)
