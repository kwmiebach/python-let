"""
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
But a let-statement, that does not work inside a function seems of little use. 

Usage example:
    
with let(a=1,b=2) as l:
  assert l.a == 1

l.a # raises Exception
"""

class let:
    
    def __init__(self, **bindings):
        self._bindings = bindings
        self.data = dict()
        self.alive = None

    def __enter__(self):
        for k in self._bindings.keys():
            self.__dict__[k] = self._bindings[k]
        self.alive = True
        return self

    def __exit__(self, type, value, traceback):
        self.alive = False
        for k in self._bindings.keys():
            del self.__dict__[k]

    def __getattr__(self, name):
        if self.alive is None:
            raise Exception("Use let with 'with'")
        if not self.alive:
            raise Exception("No access outside 'with'")
