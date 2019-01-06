from LexicalException import LexicalException
from Parser import Parser
from ParserException import ParserException


try:
    p = Parser("test4.jl")
    p1 = p.parse()
    p1.execute()
except ParserException:
    print('parser error')

except LexicalException:
    print('lexical error')

except FileNotFoundError:
    print('source file not found')
except ValueError:
    print('unknown error occurred - terminating')

