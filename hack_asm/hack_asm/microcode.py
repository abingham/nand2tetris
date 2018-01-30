from hack_asm import mnemonics


def _generate_a_instruction(command):
    assert command.startswith('@')
    val = int(command[1:])
    return '0{:015b}'.format(val)


def _normalize_c_command(command):
    if '=' not in command:
        command = 'null={}'.format(command)

    if ';' not in command:
        command = '{};null'.format(command)

    return command


def _generate_c_instruction(command):
    command = _normalize_c_command(command)

    assert '=' in command
    assert ';' in command

    dest, rest = command.split('=')
    computation, jump = rest.split(';')

    return '111{comp}{dest}{jump}'.format(
        comp=mnemonics.computation(computation),
        dest=mnemonics.destination(dest),
        jump=mnemonics.jump(jump))


def command_to_microcode(command):
    if command.startswith('@'):
        return _generate_a_instruction(command)
    else:
        return _generate_c_instruction(command)
