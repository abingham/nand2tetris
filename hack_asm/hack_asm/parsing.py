from hack_asm.instructions import AInstruction, CInstruction, LInstruction


def parse_instruction(text):
    if text.startswith('@'):
        return AInstruction(text)
    elif text.startswith('('):
        return LInstruction(text)
    else:
        return CInstruction(text)
