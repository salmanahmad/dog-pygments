from pygments.lexer import RegexLexer
from pygments.token import *

class DogLexer(RegexLexer):
    name = 'Dog'
    aliases = ['dog']
    filenames = ['*.dog']

    tokens = {
        'root': [
            (r' .*\n', Text),
            (r'\+.*\n', Generic.Inserted),
            (r'-.*\n', Generic.Deleted),
            (r'@.*\n', Generic.Subheading),
            (r'Index.*\n', Generic.Heading),
            (r'=.*\n', Generic.Heading),
            (r'.*\n', Text),
        ]
    }
