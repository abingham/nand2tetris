from hypothesis import given
import hypothesis.strategies as ST

from hack_asm.parsing import parse_instruction


MAX_15_BIT = 2 ** 15 - 1


@given(ST.integers(min_value=0, max_value=MAX_15_BIT))
def test_a_literal(val):
    instruction = parse_instruction('@{}'.format(val))
    assert instruction.generate() == '0{:015b}'.format(val)
