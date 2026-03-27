import ply.lex as lex       # Para auxiliar na análise léxica
import sys                  # Para abrir arquivo pelo cmd


# -------- Palavras reservadas -------- # 
palavras_reservadas = {
    'begin':     'BEGIN',
    'program':   'PROGRAM',
    'end':       'END',
    'read':      'READ',
    'write':     'WRITE',
    'var':       'VAR',
    'procedure': 'PROCEDURE',
    'function':  'FUNCTION',
    'do':        'DO',
    
    # Tipos
    'integer': 'INTEGER',
    'boolean': 'BOOLEAN',

    # Literais Booleanos
    'true':  'TRUE',  # Token para a palavra-chave 'true' (K de Keyword)
    'false': 'FALSE', # Token para a palavra-chave 'false'

    # Condicionais
    'if':    'IF',
    'then':  'THEN',
    'else':  'ELSE',
    'while': 'WHILE',

    # Operadores Lógicos
    'and': 'AND',
    'or': 'OR',
    'not': 'NOT',

    # Divisão
    'div': 'DIVIDE'
}
# --------------------------- #


# -------- Lista dos tokens -------- #
tokens = [
    # Identificadores e números
    'ID',         
    'NUM', # Este é o token para números (ex: 100, 5)

    # Operadores aritméticos
    'PLUS',       # +
    'MINUS',      # -
    'TIMES',      # *

    # Operadores Relacionais e Lógicos
    'ATRIB',      # :=
    'EQUAL',      # =
    'NOT_EQ',     # <>
    'LESS',       # <
    'GREATER',    # >
    'LESS_EQ',    # <=
    'GREATER_EQ', # >=

    # Delimitadores
    'LPAREN',     # (
    'RPAREN',     # )
    'SEMICOL',    # ;
    'COLON',      # :
    'PERIOD',     # .
    'COMMA'       # ,
   
] + list(palavras_reservadas.values())


t_PLUS      = r'\+'      
t_MINUS     = r'-'
t_TIMES     = r'\*'      
t_DIVIDE    = r'div'
t_ATRIB     = r':='
t_LPAREN    = r'\('        
t_RPAREN    = r'\)'        
t_SEMICOL   = r';'
t_COLON     = r':'
t_PERIOD    = r'\.'
t_EQUAL     = r'='
t_NOT_EQ    = r'<>'
t_COMMA     = r','

#Regras mais longas (<=) devem vir antes de regras mais curtas (<)
t_LESS_EQ   = r'<='
t_GREATER_EQ = r'>='
t_LESS      = r'<'
t_GREATER   = r'>'
# ------------------


# -------- Regras de expressão regular para formação de tokens mais "complexos" -------- #
def t_NUM(t):
    r'\d+'

    t.value = int(t.value)
    return t

def t_ILLEGAL(t):
    r'[$]'
    print(f"Caractere ilegal '{t.value}' encontrado na linha {t.lineno}")
    t.lexer.skip(1)

def t_BAD_ID(t):
    r'_[A-Za-z0-9_]*'
    print(f"Identificador inválido (não pode iniciar com '_') na linha {t.lineno}: {t.value}")
    t.lexer.skip(len(t.value))


def t_ID(t):
    r'[A-Za-z][A-Za-z0-9_]*'

    # Verifica se o identificador encontrado é uma palavra reservada
    t.type = palavras_reservadas.get(t.value, 'ID')
    return t
# ------------------

# -------- Regras pra ignorar espaços em \n, \t e espaço em branco -------- #
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
    print(f"Caractere ilegal '{t.value[0]}' encontrado na linha {t.lineno}")
    t.lexer.skip(1) # Pula o caractere ilegal e continua a análise.
# ------------------


# -------- chamada do lexer -------- #
lexer = lex.lex()
# ------------------


# -------- Bloco __main__ -------- #
if __name__ == '__main__':

    # Lê o arquivo passado como argumento de linha de comando
    programa_fonte = ""
    with open(sys.argv[1],'r', encoding="utf-8") as f:
        programa_fonte = f.read()
   
    # Alimenta o lexer com o conteúdo do arquivo
    lexer.input(programa_fonte)

    # Itera chamando lexer.token() até None, imprimindo cada token reconhecido
    while True:
        tok = lexer.token()
        if not tok:
            break      # Fim dos tokens
        print(tok)