from hack_asm.instructions import AInstruction, CInstruction, LInstruction


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


def process_labels(instructions, syms):
    """Update `syms` with addresses for labels found in the instruction stream.
    """
    idx = 0
    for ins in instructions:
        if isinstance(ins, LInstruction):
            syms[ins.label] = idx
        else:
            idx += 1

    return syms


def resolve_symbols(instructions, syms):
    """Resolve the symbols of a-instructions in a sequence of instructions.

    This takes in a sequence of instructions and generates a second sequence in
    which a-instruction symbols are resolved to actual addresses. Other
    instructions are returned unmodified.
    """

    next_address = 16
    for instruction in instructions:
        if isinstance(instruction, AInstruction) and instruction.is_symbol:
            if instruction.value not in syms:
                syms[instruction.value] = next_address
                next_address += 1
            instruction = AInstruction('@{}'.format(syms[instruction.value]))

        yield instruction
