from hack_asm import mnemonics


def command_to_microcode(command):
    if command.startswith('@'):
        return _generate_a_instruction(command)
    else:
        return _generate_c_instruction(command)
