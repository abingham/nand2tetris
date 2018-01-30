class SymbolTable(dict):
    """A symbol table for the hack assembler.

    This is essentially a dict except that you can only set a value once.
    """
    def __setitem__(self, key, value):
        if key in self:
            raise KeyError('Name {} already in symbol table'.format(key))
        super().__setitem__(key, value)


def create_default_symbol_table():
    """Create a SymbolTable initialized with the standard hack registers."""

    st = SymbolTable({
        'SP': 0,
        'LCL': 1,
        'ARG': 2,
        'THIS': 3,
        'THAT': 4,
        'SCREEN': 16384,
        'KBD': 24576,
    })

    st.update({'R{}'.format(r): r
               for r in range(16)})

    return st
