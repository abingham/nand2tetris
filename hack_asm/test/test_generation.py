import pathlib

from hypothesis import given
import hypothesis.strategies as ST
import pytest

from hack_asm.generation import generate_microcode
from hack_asm.parsing import parse_instruction


EXAMPLES_DIR = pathlib.Path(__file__).parent / 'examples'
MAX_15_BIT = 2 ** 15 - 1


@pytest.fixture(params=EXAMPLES_DIR.glob('*.asm'))
def canned_example(request):
    hack_file = request.param.with_suffix('.hack')
    return (request.param, hack_file)


@given(ST.integers(min_value=0, max_value=MAX_15_BIT))
def test_a_literal(val):
    instruction = parse_instruction('@{}'.format(val))
    assert instruction.generate() == ['0{:015b}'.format(val)]


def test_canned_example(canned_example):
    asm_file, hack_file = canned_example

    with open(asm_file, mode='rt') as stream:
        microcode = generate_microcode(stream)
        microcode = '\n'.join(microcode)

    with open(hack_file, mode='rt') as stream:
        assert microcode == stream.read().strip()
