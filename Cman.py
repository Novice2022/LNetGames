#  version: 2.0. Release: 09.03.2023

import platform, re, requests
from os import system
from time import sleep
from subprocess import check_output

_OS = platform.system()

def clear_console() -> int: ...
def get_current_directory() -> str: ...
def get_current_IP() -> str: ...
def get_installed_files() -> list[str]: ...

if _OS == 'Windows':
    def clear_console() -> int: system('cls')
    def get_current_directory() -> str:
        return check_output('cd',  shell=True).decode(encoding=str(check_output('chcp', shell=True)).split(':')[-1][1:].split('\\')[0]).replace('\b', '')[:-2]
    def get_ethernet_info() -> str:
        return check_output('ipconfig', shell=True).decode(encoding=str(check_output('chcp', shell=True)).split(':')[-1][1:].split('\\')[0]).split('\n')
    def get_installed_files() -> list[str]:
        return list(set(re.findall(r'\w*\.py', check_output('dir', shell=True, encoding=str(check_output('chcp', shell=True)).split(':')[-1][1:].split('\\')[0]))).intersection(set(['client.py', 'cman.py', 'games.py'])))
elif _OS == 'Linux':
    def clear_console() -> int: system('clear')
    def get_current_directory() -> str:
        return check_output('pwd', shell=True).decode(encoding='utf-8').replace('\b', '')
    def get_ethernet_info() -> str:
        return check_output('ifconfig', shell=True).decode(encoding='utf-8').split('\n')
    def get_installed_files() -> list[str]:
        return list(set([_file for _file in check_output('dir', shell=True, encoding='utf-8').replace('\n', '  ').replace('\t', '  ').split('  ')]).intersection(set(['client.py', 'cman.py', 'games.py'])))

__author__ = 'Igor Zabrodin (@YandexFindMe / https://t.me/YandexFindMe)'
__version__ = '2.0'

class Сlient_manager():
    """ Represents installing, uninstalling, configurating & editing files of Your client application """

    def __init__(self) -> None:
        __description = f'Client manager application: install, upgrade & add LNetGames\'s games\n{__version__}\n\nPlease, DON\'T REMOVE OR RENAME files which this manager handle!'
        print(__description)
        command = input('\n> ').lower()
        while not (command in ['get client', 'get games', 'help', '-help', '--help', '?', 'exit', 'upgrade', 'clear']):
            print('No such command for client manager :(')
            command = input('\n> ')
        
        while command.lower() != 'exit':
            if command in ['help', '-help', '--help', '?']:
                self._support()
            elif command == 'get client':
                self._install('client')
            elif command == 'get games':
                self._install('games')
            elif command == 'upgrade':
                self._upgrade()
            elif command == 'clear':
                clear_console()
                print(__description)
            command = input('\n> ')

    def _support(self) -> None:
        print('\n\n\tYou may enter this commands with different cases\n------------------------------------------------')
        print('\tget client                   install client')
        print('\tget games                    install games')
        print('\tupgrade                      upgrade all scripts')
        print('\thelp / -help / --help / ?    get this window')
        print('\texit                         exit from client manager')
        print('\tclear                        clear current window\n')

    def _handle_connection_status(self) -> str:
        def __connection_status() -> bool:
            ethernet_info = get_ethernet_info()  # TODO: FIX Raises on Linux
            return True if any(['IPv4' in line if _OS == 'Windows' else 'inet 192.168' in line for line in ethernet_info]) else False if (_OS == 'Linux' and 'eth0:' in ethernet_info) or _OS == 'Windows' in ethernet_info[0] else False
        
        if not __connection_status() or __connection_status() == None:
            move = input('No interner connection.\n\t* "continue": wait internet connection\n\t* "break": turn to client-manager\n\t> ')
            while not move.lower() in ['continue', 'break']:
                move = input('\n\t* "continue": wait internet connection\n\t* "break": turn to client-manager\n\t> ')
            if move == 'break': return 'break'
        timer = 0
        while True:
            if __connection_status(): return 'OK'
            if timer == 0: print('\twaiting internet connection')
            sleep(.5)
            timer += 0.5
            if timer % 10 == 0: print('\twaiting internet connection')

    def _install(self, file_name: str) -> bool:
        if self._handle_connection_status() == 'break':
            return 'client break'
        url = 'https://raw.githubusercontent.com/Novice2022/LNetGames/main/Games.py' if file_name == 'games' else 'https://raw.githubusercontent.com/Novice2022/LNetGames/main/Client.py'
        response = requests.get(url).text
        compare_versions_flag = self.__compare_versions(f'{file_name}.py', response.split('\n')[0][3:-1])
        path = get_current_directory()
        if compare_versions_flag == 'not found':
            with open(f'{file_name}.py', 'w', encoding='utf-8') as f:
                f.write(response.replace('\n', ''))
                if compare_versions_flag == 'not found':
                    print(f'\tInst: {file_name}.py ')
                    return True
        print(f'\t{file_name}.py actually inastalled. Try \"upgrade\"')
        return True

    def _upgrade(self) -> str or bool:
        if self._handle_connection_status() == 'break':
            return 'client break'
        for _file in get_installed_files():
            response = requests.get(f'https://raw.githubusercontent.com/Novice2022/LNetGames/main/{_file[0].upper() + _file[1:]}').text
            versions = self.__compare_versions(_file, response)
            if 'update' in versions:
                versions = versions.replace('update ', '')
                with open(f'{_file}', 'w', encoding='utf-8') as f:
                    f.write(response.replace('\n', ''))
                    print(f'\tUpg: {_file} {versions}')
            else:
                print(f'\t{_file} has latest version')

    @staticmethod
    def __compare_versions(exists_file_path: str, request_version: str) -> str:
        try:
            current_version = open(exists_file_path, 'r', encoding='utf-8').readline()[3:-1]
            request_version = request_version.split('\n')[0][3:-1]
            if current_version != request_version: return f'update {current_version} => {request_version}'
            return 'OK'
        except FileNotFoundError:
            return 'not found'


def main() -> int():
    clear_console()
    try:
        Сlient_manager()
    except Exception as EX:
        print('\tYou probably aren\'t connected to the internet.\n\tRefresh internet connection and retry.')
        return -1
    return 0


if __name__ == "__main__":
    print(f'Program status: {main()}')
