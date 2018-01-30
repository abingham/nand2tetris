"""hack-asm

Usage:
  hack-asm [-o <hack-file>] <asm-file>

Options:
  -h --help      Show this screen.
  -o <hack-file> The output hack file [default: out.hack].

"""

import sys

import docopt

from hack_asm.generation import generate_microcode


def main(args):
    args = docopt.docopt(__doc__, argv=args, version='hack-asm 0.1')
    asm_file = args['<asm-file>']
    hack_file = args['-o']

    if hack_file is None:
        hack_file = 'out.hack'

    with open(asm_file, mode='rt') as infile,\
         open(hack_file, mode='wt') as outfile:
        microcode = generate_microcode(infile)
        outfile.write('\n'.join(microcode))
        outfile.write('\n')


if __name__ == '__main__':
    main(sys.argv[1:])
