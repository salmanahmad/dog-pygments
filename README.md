
# Pygments for The Dog Programming Language

## Install

To install the Dog lexer and style on your system run the following command:

<pre>
cd lexer
python setup.py install

cd style
python setup.py install
</pre>

(you may need to run the above as sudo)

## Usage

To use the lexer from the commandline run:

<pre>
pygmentize -O full -f html -o <output file> <input file>
</pre>

You may also be interested in using the lexer from inside of a LaTeX document using the minted package:

<pre>
\begin{minted}[linenos=true, numbersep=5pt]{dog}
  include dog
  define with: file append: text do
    print: foo
  end
\end{minted}
</pre>

