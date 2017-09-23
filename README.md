# A let statement for python

A simple class that allows a let-like construct as known from the lisp languages.

Home: https://github.com/kwmiebach/python-let

Inspired by: https://nvbn.github.io/2014/09/25/let-statement-in-python/

See discussion: https://www.reddit.com/r/Python/comments/41yr58/let_statement_in_python_2014/

This is not a real let-statement, because the variables are only
added to a dictionary that is available inside the with-block.

The name of the dictionary will still overwrite anything with the same name
outside the with-block. Only the values of the dictionary are
unvavailable outside the block, they are explicitly deleted.

A real let-statement which accesses pythons local variables seems difficult, since
the tools that python provides, namely "inspect" and "locals()",
do not or do not always allow write access. Only from the global scope 
"locals()" delivers a dictionary that you can write back to.
