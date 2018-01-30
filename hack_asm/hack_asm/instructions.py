import re

from hack_asm import mnemonics


class AInstruction:
    SYMBOL_REGEX = re.compile('^[A-Za-z_.$:][A-Za-z0-9_.$:]+$')

    def __init__(self, asm):
        if not asm.startswith('@'):
            raise ValueError('a-instructions must start with @')

        self._value = asm[1:]

        # If the value is not a valid symbol name, then it must be a positive
        # integer.
        if not self.is_symbol:
            try:
                int(asm[1:])
            except ValueError:
                raise ValueError(
                    'a-instruction values must be positive integers or valid symbols ({}).'.format(
                        AInstruction.SYMBOL_REGEX))

    @property
    def value(self):
        return self._value

    @property
    def is_symbol(self):
        return re.match(AInstruction.SYMBOL_REGEX, self.value)

    def generate(self):
        if self.is_symbol:
            raise ValueError(
                'Can not generate code from unresolevd a-instruction.')

        return ['0{:015b}'.format(int(self.value))]

    def __eq__(self, rhs):
        return self.value == rhs.value

    def __repr__(self):
        return 'AInstruction("@{}")'.format(self.value)


class CInstruction:
    def __init__(self, asm):
        asm = CInstruction._normalize(asm)
        self._dest, asm = asm.split('=')
        self._computation, self._jump = asm.split(';')

        self._codes = dict(
            comp=mnemonics.computation(self.computation),
            dest=mnemonics.destination(self.destination),
            jump=mnemonics.jump(self.jump))

    @property
    def destination(self):
        return self._dest

    @property
    def computation(self):
        return self._computation

    @property
    def jump(self):
        return self._jump

    def generate(self):
        return ['111{comp}{dest}{jump}'.format(**self._codes)]

    def __eq__(self, rhs):
        return (self.destination == rhs.destination
                and self.computation == rhs.computation
                and self.jump == rhs.jump)

    def __repr__(self):
        dest = '' if self.destination == 'null' else '{}='.format(self.destination)
        jump = '' if self.jump == 'null' else ';{}'.format(self.jump)
        return 'CInstruction("{}{}{}")'.format(dest, self.computation, jump)

    @staticmethod
    def _normalize(command):
        if '=' not in command:
            command = 'null={}'.format(command)

        if ';' not in command:
            command = '{};null'.format(command)

        return command


class LInstruction:
    def __init__(self, asm):
        if asm[0] != '(' or asm[-1] != ')':
            raise ValueError('Labels must start with "(" and end with ")"')

        self._label = asm[1:-1]

    @property
    def label(self):
        return self._label

    def generate(self):
        return []

    def __eq__(self, rhs):
        return self.label == rhs.label

    def __repr__(self):
        return 'LInstruction("({})")'.format(self.label)
