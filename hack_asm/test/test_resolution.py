from hack_asm.instructions import AInstruction, LInstruction
from hack_asm.resolution import resolve_labels, resolve_symbols
from hack_asm.symbol_table import SymbolTable


def test_basic_resolve_labels():
    instructions = (LInstruction("(zero)"), 0, 0, LInstruction("(two)"), 0)
    syms = SymbolTable()
    resolve_labels(instructions, syms)
    assert syms == {'zero': 0, 'two': 2}


def test_basic_symbol_resolution():
    instructions = (AInstruction("@foo"), 0, AInstruction('@bar'))
    syms = SymbolTable()
    assert list(resolve_symbols(instructions, syms)) == [AInstruction('@16'), 0, AInstruction('@17')]
