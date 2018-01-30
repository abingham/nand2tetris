def load_commands(handle):
    "Generate a sequence of assembly commands from file-like `handle`."
    for line in handle:
        line = line.split('//')[0]
        line = line.strip()
        if line:
            yield line


def load_commands_from_file(filename):
    with open(filename, mode='rt') as handle:
        yield from load_commands(handle)
