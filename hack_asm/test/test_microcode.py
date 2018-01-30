from hypothesis import given
import hypothesis.strategies as ST

from hack_asm.microcode import command_to_microcode


MAX_15_BIT = 2 ** 15 - 1


@given(ST.integers(min_value=0, max_value=MAX_15_BIT))
def test_a_literal(val):
    mc = command_to_microcode('@{}'.format(val))
    assert mc == '0{:015b}'.format(val)
