from hack_asm.instructions import AInstruction, CInstruction, LInstruction


def parse_instruction(text):
    """Parse a single assembly instruction."""
    if text.startswith('@'):
        return AInstruction(text)
    elif text.startswith('('):
        return LInstruction(text)
    else:
        return CInstruction(text)


def _tokenize(stream):
    """Convert a stream of assembly into individual instructions."""
    for line in stream:
        line = line.split('//')[0]
        line = line.strip()
        if line:
            yield line


def from_stream(stream):
    "Generate a sequence of instructions from file-like `stream`."
    return map(parse_instruction, _tokenize(stream))
