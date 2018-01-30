from hack_asm.instructions import AInstruction, CInstruction, LInstruction


def load_instructions(handle):
    "Generate a sequence of assembly commands from file-like `handle`."
    for line in handle:
        line = line.split('//')[0]
        line = line.strip()

        if not line:
            continue
        elif line.startswith('@'):
            yield AInstruction(line)
        elif line.startswith('('):
            yield LInstruction(line)
        else:
            yield CInstruction(line)


def load_instructions_from_file(filename):
    with open(filename, mode='rt') as handle:
        yield from load_instructions(handle)
