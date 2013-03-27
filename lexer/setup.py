from setuptools import setup
 
__author__ = 'Salman Ahmad'
 
setup(
    name='Dog Pygments Lexer',
    version='0.0.1',
    description=__doc__,
    author=__author__,
    packages=['dog_lexer'],
    entry_points='''
[pygments.lexers]
doglexer = dog_lexer:DogLexer
'''
)