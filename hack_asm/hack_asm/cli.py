"""hack-asm

Usage:
  hack-asm [-o <hack-file>] <asm-file>

Options:
  -h --help      Show this screen.
  -o <hack-file> The output hack file [default: out.hack].

"""

import sys

import docopt

from hack_asm.lex import load_instructions_from_file
from hack_asm.symbol_table import create_default_symbol_table, process_labels, resolve_symbols


def main(args):
    args = docopt.docopt(__doc__, argv=args, version='hack-asm 0.1')
    asm_file = args['<asm-file>']
    hack_file = args['-o']
    if hack_file is None:
        hack_file = 'out.hack'

    syms = process_labels(
        load_instructions_from_file(asm_file),
        create_default_symbol_table())

    resolved = resolve_symbols(load_instructions_from_file(asm_file), syms)

    microcode = filter(
        None,
        (instruction.generate()
         for instruction
         in resolved))

    with open(hack_file, mode='wt') as outfile:
        outfile.write('\n'.join(microcode))
        outfile.write('\n')


if __name__ == '__main__':
    main(sys.argv[1:])
