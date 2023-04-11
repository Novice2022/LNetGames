#  version: 1.0 (beta). Release: 11.04.2023

from os import system
import platform

def clear_console() -> None: ...

if platform.system() == 'Windows':
    def clear_console() -> None: system('cls')
elif platform.system() == 'Linux':
    def clear_console() -> None: system('clear')

del platform

class Converter:
    """ Converting ASCII chars to beautiful font """

    def __init__(self, row: str) -> None:
        self.__alphabet = {
            ' ': [
                '     ',
                '     ',
                '     ',
                '     ',
                '     ',
                '     '
            ],
            '0': [
                '    ____ ',
                '   / __ \\',
                '  / / / /',
                ' / / / / ',
                '/ /_/ /  ',
                '\____/   '
            ],
            '1': [
                '     __  ',
                '    /  \ ',
                '   /_/ / ',
                '    / /  ',
                ' __/ /_  ',
                '/_____/  '
            ],
            '2': [
                '    ___  ',
                '   /   \ ',
                '   \// / ',
                '  __/ /  ',
                ' / __/_  ',
                '/_____/  '
            ],
            '3': [
                '    ___  ',
                '   /__ \ ',
                '    _/ / ',
                '   |  /  ',
                ' ___\ \  ',
                '/_____/  '
            ],
            '4': [
                '   __  __',
                '  / / / /',
                ' / /_/ / ',
                ' \__  /  ',
                '   / /   ',
                '  /_/    '
            ],
            '5': [
                '    _____',
                '   / ___/',
                '  / /_   ',
                '  \__ \  ',
                ' ___/ /  ',
                ' \___/   '
            ],
            '6': [
                '    _____',
                '   / ___/',
                '  / /_   ',
                ' / __ \  ',
                '/ /_/ /  ',
                '\____/   '
            ],
            '7': [
                '  _______',
                ' /____  /',
                '     / / ',
                '    / /  ',
                '   / /   ',
                '  /_/    '
            ],
            '8': [
                '    ____ ',
                '   / __ \\',
                '  / /_/ /',
                ' / __  / ',
                '/ /_/ /  ',
                '\____/   '
            ],
            '9': [
                '    ____ ',
                '   / __ \\',
                '  / /_/ /',
                '  \__  / ',
                '  __/ /  ',
                ' /___/   '
            ],
            'a': [
                '',
                '',
                '',
                '',
                '',
                ''
            ],
            'b': [
                '',
                '',
                '',
                '',
                '',
                ''
            ],
            'c': [
                '',
                '',
                '',
                '',
                '',
                ''
            ],
            'd': [
                '',
                '',
                '',
                '',
                '',
                ''
            ],
            'e': [
                '',
                '',
                '',
                '',
                '',
                ''
            ],
            'f': [
                '',
                '',
                '',
                '',
                '',
                ''
            ],
            'g': [
                '',
                '',
                '',
                '',
                '',
                ''
            ],
            'h': [
                '',
                '',
                '',
                '',
                '',
                ''
            ],
            'i': [
                '',
                '',
                '',
                '',
                '',
                ''
            ],
            'j': [
                '',
                '',
                '',
                '',
                '',
                ''
            ],
            'k': [
                '',
                '',
                '',
                '',
                '',
                ''
            ],
            'l': [
                '',
                '',
                '',
                '',
                '',
                ''
            ],
            'm': [
                '',
                '',
                '',
                '',
                '',
                ''
            ],
            'n': [
                '',
                '',
                '',
                '',
                '',
                ''
            ],
            'o': [
                '',
                '',
                '',
                '',
                '',
                ''
            ],
            'p': [
                '',
                '',
                '',
                '',
                '',
                ''
            ],
            'q': [
                '',
                '',
                '',
                '',
                '',
                ''
            ],
            'r': [
                '',
                '',
                '',
                '',
                '',
                ''
            ],
            's': [
                '',
                '',
                '',
                '',
                '',
                ''
            ],
            't': [
                '',
                '',
                '',
                '',
                '',
                ''
            ],
            'u': [
                '',
                '',
                '',
                '',
                '',
                ''
            ],
            'v': [
                '',
                '',
                '',
                '',
                '',
                ''
            ],
            'w': [
                '',
                '',
                '',
                '',
                '',
                ''
            ],
            'x': [
                '',
                '',
                '',
                '',
                '',
                ''
            ],
            'y': [
                '',
                '',
                '',
                '',
                '',
                ''
            ],
            'z': [
                '',
                '',
                '',
                '',
                '',
                ''
            ],
        }
        
        self.standart = row
        self.standart = self.__generate_monospace()
        self.normalized = self.standart
        self.__normalise_text()

    def __generate_monospace(self):
        temp_invalid_container = []
        for chars_line in zip([self.__alphabet.get(char) for char in self.standart]):
            temp_invalid_container.append(chars_line[0])
        font = ''
        for char_line in range(6):
            for row in temp_invalid_container:
                font += row[char_line]
            font += '\n'
                
        return font
    
    def __normalise_text(self) -> str:
        """ solve it with replaceing """
        return ''
    
    @staticmethod
    def draw(text: str) -> None: 
        """ \'Converter.draw\' is a copy of usual \'print\' function """
        return print(text)


def draw_only():
    converter = Converter(input('Enter row You want to draw: '))
    move = input('\n1) get standart text\n2) get normalized text\n\t> ').replace(' ', '')
    while not move in ['1', '2']:
        move = input('Enter 1 or 2:\n\t> ').replace(' ', '')
    clear_console()
    if move == '1':
        converter.draw(converter.standart)
    else:
        converter.draw(converter.normalized)


def dialog_version() -> None:
    while True:
        text = input('Enter row You want to draw or (\'exit\' / \'выйти\') to return to main menu:\n\t> ')
        if text in ['exit', 'выйти']:
            break
        converter = Converter(text)
        move = input('\n1) get standart text\n2) get normalized text\n\t> ').replace(' ', '')
        while not move in ['1', '2']:
            move = input('Enter 1 or 2:\n\t> ').replace(' ', '')
        clear_console()
        if move == '1':
            converter.draw(converter.standart)
        else:
            converter.draw(converter.normalized)
        input('\n\nEnter to continue...')
        clear_console()
    clear_console()


def main():
    while True:
        clear_console()
        move = input('1) simple version\n2) dialog version\n3) stop program\n\t> ').replace(' ', '')
        while not move in ['1', '2', '3']:
            move = input('Enter 1 or 2:\n\t> ').replace(' ', '')
        clear_console()
        if move == '1':
            draw_only()
            input('\n\nEnter to continue...')
        elif move == '2':
            dialog_version()
        else:
            break
    clear_console()

if __name__ == '__main__':
    main()


"""
     _____    __    _____  __   _____
    |__   |  /  \  |  _  \(__) / ____\
      /  /  / <> \ |     / __ | /  __
     /  /_ /  __  \|  _  \|  || \__\ \
    |_____'__/  \__'_____/|__| \_____/

"""
