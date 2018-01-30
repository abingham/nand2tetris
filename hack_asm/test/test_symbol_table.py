from hypothesis import given
import hypothesis.strategies as ST
import pytest

from hack_asm.symbol_table import SymbolTable


@given(ST.text(), ST.integers())
def test_reassigning_symbol_raises_KeyError(key, value):
    st = SymbolTable()
    st[key] = value
    with pytest.raises(KeyError):
        st[key] = value
