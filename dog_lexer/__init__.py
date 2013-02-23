from pygments.lexer import RegexLexer, bygroups
from pygments.token import *

class DogLexer(RegexLexer):
    name = 'Dog'
    aliases = ['dog']
    filenames = ['*.dog']


    tokens = {
        # copied from PerlLexer:
        'balanced-regex': [
            (r'/(\\\\|\\/|[^/])*/[egimosx]*', String.Regex, '#pop'),
            (r'!(\\\\|\\!|[^!])*![egimosx]*', String.Regex, '#pop'),
            (r'\\(\\\\|[^\\])*\\[egimosx]*', String.Regex, '#pop'),
            (r'{(\\\\|\\}|[^}])*}[egimosx]*', String.Regex, '#pop'),
            (r'<(\\\\|\\>|[^>])*>[egimosx]*', String.Regex, '#pop'),
            (r'\[(\\\\|\\\]|[^\]])*\][egimosx]*', String.Regex, '#pop'),
            (r'\((\\\\|\\\)|[^\)])*\)[egimosx]*', String.Regex, '#pop'),
            (r'@(\\\\|\\\@|[^\@])*@[egimosx]*', String.Regex, '#pop'),
            (r'%(\\\\|\\\%|[^\%])*%[egimosx]*', String.Regex, '#pop'),
            (r'\$(\\\\|\\\$|[^\$])*\$[egimosx]*', String.Regex, '#pop'),
        ],
        'root': [
            (r'\s+', Text),

            # balanced delimiters (copied from PerlLexer):
            (r's{(\\\\|\\}|[^}])*}\s*', String.Regex, 'balanced-regex'),
            (r's<(\\\\|\\>|[^>])*>\s*', String.Regex, 'balanced-regex'),
            (r's\[(\\\\|\\\]|[^\]])*\]\s*', String.Regex, 'balanced-regex'),
            (r's\((\\\\|\\\)|[^\)])*\)\s*', String.Regex, 'balanced-regex'),
            (r'm?/(\\\\|\\/|[^/\n])*/[gcimosx]*', String.Regex),
            (r'm(?=[/!\\{<\[\(@%\$])', String.Regex, 'balanced-regex'),

            # Comments
            (r'#(.*?)\n', Comment.Single),
            # Symbols
            (r'\'([^\'\s\[\]\(\)\{\}]+|\[\])', String.Symbol),
            # Multi-line DoubleQuotedString
            (r'"""(\\\\|\\"|[^"])*"""', String),
            # DoubleQuotedString
            (r'"(\\\\|\\"|[^"])*"', String),
            # keywords
            (r'(def|class|try|catch|finally|retry|return|return_local|match|'
             r'include|define|do|end|if|then|else|while|forever|'
             r'repeat|times|for|each|on'
             r'case|->|=>)\b', Keyword),
            # constants
            (r'(null|false|true)\b', Name.Constant),
            (r'[(){};,/?\|:\\]', Punctuation),
            # names
            (r'(print:)\b', Name.Builtin),
            # functions
            (r'[a-zA-Z]([a-zA-Z0-9_]|[-+?!=*/^><%])*:', Name.Function),
            # operators, must be below functions
            (r'[-+*/~,<>=&!?%^\[\]\.$]+', Operator),
            ('[A-Z][a-zA-Z0-9_]*', Name.Constant),
            ('@[a-zA-Z_][a-zA-Z0-9_]*', Name.Variable.Instance),
            ('@@[a-zA-Z_][a-zA-Z0-9_]*', Name.Variable.Class),
            ('@@?', Operator),
            ('[a-zA-Z_][a-zA-Z0-9_]*\.', Name.Function),
            ('[a-zA-Z_][a-zA-Z0-9_]*', Name),
            # numbers - / checks are necessary to avoid mismarking regexes,
            # see comment in RubyLexer
            (r'(0[oO]?[0-7]+(?:_[0-7]+)*)(\s*)([/?])?',
             bygroups(Number.Oct, Text, Operator)),
            (r'(0[xX][0-9A-Fa-f]+(?:_[0-9A-Fa-f]+)*)(\s*)([/?])?',
             bygroups(Number.Hex, Text, Operator)),
            (r'(0[bB][01]+(?:_[01]+)*)(\s*)([/?])?',
             bygroups(Number.Bin, Text, Operator)),
            (r'([\d]+(?:_\d+)*)(\s*)([/?])?',
             bygroups(Number.Integer, Text, Operator)),
            (r'\d+([eE][+-]?[0-9]+)|\d+\.\d+([eE][+-]?[0-9]+)?', Number.Float),
            (r'\d+', Number.Integer)
        ]
    }
