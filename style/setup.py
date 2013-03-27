from setuptools import setup
 
__author__ = 'Salman Ahmad'
 
setup(
    name='Dog Pygments Style',
    version='0.0.1',
    description=__doc__,
    author=__author__,
    packages=['dog_style'],
    entry_points='''
[pygments.styles]
dog = dog_style:DogStyle
'''
)