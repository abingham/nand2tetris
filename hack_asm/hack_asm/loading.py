from hack_asm.parsing import parse_instruction


def from_stream(stream):
    "Generate a sequence of instructions from file-like `stream`."
    for line in stream:
        line = line.split('//')[0]
        line = line.strip()

        if line:
            yield parse_instruction(line)


def from_file(filename):
    with open(filename, mode='rt') as handle:
        yield from from_stream(handle)
