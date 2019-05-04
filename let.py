class let:

    """
    Home: https://github.com/kwmiebach/python-let

    Usage example:

    from lib.let import let
    with let(a=1,b=2) as l:
      assert l.a == 1

    l.a # raises Exception
    """
      
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

    def __str__(self):
      return str(self._bindings)

    def __repr__(self):
      # todo also include self.__class__.__name__
      return repr(self._bindings)
