from hypothesis import assume, given
import hypothesis.strategies as ST
import pytest

import hack_asm.mnemonics as mnm


def test_all_computation_mnemonics_have_unique_microcodes():
    assert len(set(mnm._COMPUTATION_MNEMONICS.values())) == len(mnm._COMPUTATION_MNEMONICS)


@given(ST.text())
def test_ValueError_on_invalid_computation_mnemonic(mnemonic):
    assume(mnemonic not in mnm._COMPUTATION_MNEMONICS)
    with pytest.raises(ValueError):
        mnm.computation(mnemonic)


def test_all_destination_mnemonics_have_unique_microcodes():
    assert len(set(mnm._DEST_MNEMONICS.values())) == len(mnm._DEST_MNEMONICS)


@given(ST.text())
def test_ValueError_on_invalid_dest_mnemonic(mnemonic):
    assume(mnemonic not in mnm._DEST_MNEMONICS)
    with pytest.raises(ValueError):
        mnm.destination(mnemonic)


def test_all_jump_mnemonics_have_unique_microcodes():
    assert len(set(mnm._JUMP_MNEMONICS.values())) == len(mnm._JUMP_MNEMONICS)


@given(ST.text())
def test_ValueError_on_invalid_jump_mnemonic(mnemonic):
    assume(mnemonic not in mnm._JUMP_MNEMONICS)
    with pytest.raises(ValueError):
        mnm.jump(mnemonic)
