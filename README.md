
# Pygments lexer for The Dog Programming Language

## Install

To install the Dog lexer on your system run the following command:

``python setup.py install``

(you may need to run the above as sudo)

## Usage

To use the lexer from the commandline run:

<code>
<pre>
pygmentize -O full -f html -o <output file> <input file>
</pre>
</code>


You may also be interested in using the lexer from inside of a LaTeX document using the minted package:


<code>
<pre>
\begin{minted}[linenos=true, numbersep=5pt]{dog}
  include dog
  define with: file append: text do
    print: foo
  end
\end{minted}
</pre>
</code>
