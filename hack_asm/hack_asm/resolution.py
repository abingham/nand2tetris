"""Routines to resolve the various kinds of symbols in Hack.
"""

from hack_asm.instructions import AInstruction, LInstruction


def resolve_labels(instructions, syms):
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
