import sys

from hack_asm.lex import load_commands_from_file
from hack_asm.microcode import command_to_microcode


def main(args):
    # TODO: docopt
    filename = args[0]

    for cmd in load_commands_from_file(filename):
        print(command_to_microcode(cmd))


if __name__ == '__main__':
    main(sys.argv[1:])
