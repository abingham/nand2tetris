from hypothesis import given
import hypothesis.strategies as ST
import pytest

from hack_asm.instructions import AInstruction, LInstruction
from hack_asm.symbol_table import process_labels, resolve_symbols, SymbolTable


@given(ST.text(), ST.integers())
def test_reassigning_symbol_raises_KeyError(key, value):
    st = SymbolTable()
    st[key] = value
    with pytest.raises(KeyError):
        st[key] = value


def test_basic_process_labels():
    instructions = (LInstruction("(zero)"), 0, 0, LInstruction("(two)"), 0)
    syms = SymbolTable()
    process_labels(instructions, syms)
    assert syms == {'zero': 0, 'two': 2}


def test_basic_symbol_resolution():
    instructions = (AInstruction("@foo"), 0, AInstruction('@bar'))
    syms = SymbolTable()
    assert list(resolve_symbols(instructions, syms)) == [AInstruction('@16'), 0, AInstruction('@17')]
