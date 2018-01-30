from itertools import chain

from hack_asm import parsing
from hack_asm.resolution import resolve_labels, resolve_symbols
from hack_asm.symbol_table import create_default_symbol_table


def generate_microcode(stream):
    """Generate a sequence of microcode instructions from an input stream of
    assembly.

    `stream` should be a file-like object producting assembly code. It needs to
    be seekable because this will make multiple passes over it.
    """

    # Resolve all code labels into `syms`
    syms = resolve_labels(
        parsing.from_stream(stream),
        create_default_symbol_table())

    stream.seek(0)

    # Resolve all symbols to memory locations
    resolved = resolve_symbols(
        parsing.from_stream(stream),
        syms)

    # Let all instructions generate microcode
    return chain(*(ins.generate() for ins in resolved))
