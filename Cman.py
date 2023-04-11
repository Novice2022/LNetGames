#  version: 2.3. Release: 12.04.2023

import platform, re
from os import system
from time import sleep
from subprocess import check_output, CalledProcessError

_OS = platform.system()

del platform

def clear_console() -> int: ...
def get_current_IP() -> str: ...
def get_installed_files() -> list[str]: ...
def console_output() -> str: ...

if _OS == 'Windows':
    def clear_console() -> int: system('cls')
    def console_output(command: str) -> str: return check_output(command, shell=True, encoding=str(check_output('chcp', shell=True)).split(':')[-1][1:].split('\\')[0])
    def get_ethernet_info() -> str:
        return console_output('ipconfig')
    def get_installed_files() -> list[str]:
        files = set(re.findall(r'\w*\.py', console_output('dir')))
        if not 'cman.py' in files:
            print()
            print('\t/    please rename this file to \"cman.py\" make it avaliable to update this file automatically    \ ')
            print('\t\   (some systems don\'t give permition for programs to rename files. Thanks for understanding)   /\n\n')
            input('Enter to continue...')
            print()
        files = list(files.intersection(set(['client.py', 'cman.py', 'games.py', 'converter.py'])))
        return files
elif _OS == 'Linux':
    def clear_console() -> int: system('clear')
    def console_output(command: str) -> str: return check_output(command, shell=True, encoding='utf-8')
    def get_ethernet_info() -> str:
        return console_output('ifconfig')
    def get_installed_files() -> list[str]:
        files = set(re.findall(r'\w*\.py', console_output('dir')))
        if not 'cman.py' in files:
            print()
            print('\t/    please rename this file to \"cman.py\" make it avaliable to update this file automatically    \ ')
            print('\t\   (some systems don\'t give permition for programs to rename files. Thanks for understanding)   /\n\n')
            input('Enter to continue...')
            print()
        files = list(files.intersection(set(['client.py', 'cman.py', 'games.py', 'converter.py'])))
        return files

__author__ = 'Igor Zabrodin (@YandexFindMe / https://t.me/YandexFindMe)'
__version__ = '2.3'
__program_status__ = 1


#  ---------------------------------------------------------------------  start main logic  ---------------------------------------------------------------------

clear_console()
try:
    import requests
except ModuleNotFoundError:
    print('\tMust be installed \"requests\" module.')
    while True:
        command = input('\tInstall [Y/n]: ')
        if command == 'Y':
            try:
                console_output('pip install requests')
            except CalledProcessError:
                print('\tYou can install this package by yourself using \'pip\'.')
                print('\tThis manager can\'t do this because you didn\'t put \'pip\' to os environment path or you use other python version which \'pip\' doesn\'t in path or overloaded.')
                print('\tYou can install python again with \'add to path\' configuration in setuper window.')
                print('\tSee info about \'pip\' into your browser or write (@YandexFindMe / https://t.me/YandexFindMe) if you didn\'t understand.')
                print('\tPlease do second one if you really have no idea.')
            try:
                import requests
            except ModuleNotFoundError:
                print('\tProblem in your \'pip\' configurations.\n\tSolving automatically will be later.')
                __program_status__ = -2
                break
        elif command == 'n':
            __program_status__ = 0
            break
if __program_status__ == 1:
    clear_console()

#  ---------------------------------------------------------------------  start main logic  ---------------------------------------------------------------------


class Сlient_manager():
    """ Represents installing and upgrading actual files """

    def __init__(self) -> None:
        __description = f'Client manager application: install, upgrade, work & enjoy with LNetGames\'s applications\nVersion: {__version__}\n\nDON\'T REMOVE or RENAME files which this manager handle (rename only this file to \"cman.py\" after installing)!'
        print(__description)
        self.__support()
        command = input('\n> ').lower()
        while not (command in ['get client', 'get games', 'get converter', 'help', '-help', '--help', '?', 'exit', 'upgrade', 'clear']):
            print('No such command for client manager :(')
            command = input('\n> ')
        
        while command.lower() != 'exit':
            if command in ['help', '-help', '--help', '?']:
                self.__support()
            print()
            if command in ['get client', 'get games', 'get converter']:
                self.__install(command.split()[1])
            elif command == 'upgrade':
                self.__upgrade()
            elif command == 'clear':
                clear_console()
                print(__description)
            command = input('\n> ')

    def __support(self) -> None:
        print('\n\n\t   You can enter this commands with different cases  \n\t-----------------------------------------------------')
        print('\tget client                   install client')
        print('\tget games                    install games')
        print('\tget converter                install converter')
        print('\tupgrade                      upgrade all scripts')
        print('\thelp / -help / --help / ?    get this window')
        print('\texit                         exit from client manager')
        print('\tclear                        clear current window\n')

    def __handle_connection_status(self) -> str:
        def __connection_status() -> bool:
            ethernet_info = get_ethernet_info()
            return True if any(['IPv4' in ethernet_info if _OS == 'Windows' else 'inet 192.168']) else False

        if not __connection_status() or __connection_status() == None:
            move = input('No internet connection.\n\t* "continue": wait internet connection\n\t* "break": turn to client-manager\n\t> ')
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

    def __install(self, file_name: str) -> None:
        if self.__handle_connection_status() == 'break':
            return 'client break'
        url = f'https://raw.githubusercontent.com/Novice2022/LNetGames/main/{file_name[0].upper() + file_name[1:]}.py'
        response = requests.get(url).text
        if self.__compare_versions(f'{file_name}.py', response.split('\n')[0][3:-1]) == 'not found':
            with open(f'{file_name}.py', 'w', encoding='utf-8') as f:
                f.write(response.replace('\n', ''))
                print(f'\tInst: {file_name}.py ')
                return None
        print(f'\t{file_name}.py actually inastalled. Try \"upgrade\"')

    def __upgrade(self) -> str or None:
        if self.__handle_connection_status() == 'break':
            return 'client break'
        for file_name in get_installed_files():
            response = requests.get(f'https://raw.githubusercontent.com/Novice2022/LNetGames/main/{file_name[0].upper() + file_name[1:]}').text
            versions = self.__compare_versions(file_name, response)
            if 'update' in versions:
                versions = versions.replace('update ', '')
                with open(f'{file_name}', 'w', encoding='utf-8') as f:
                    f.write(response.replace('\n', ''))
                    print(f'\tUpg: {file_name} {versions}')
            else:
                print(f'\t{file_name} has latest version')

    @staticmethod
    def __compare_versions(exists_file_path: str, request_version: str) -> str:
        try:
            current_version = open(exists_file_path, 'r', encoding='utf-8').readline()[3:-1]
            request_version = request_version.split('\n')[0][3:-1]
            if current_version != request_version: return f'update \t\t[{current_version}  =>  {request_version}]'
            return 'OK'
        except FileNotFoundError:
            return 'not found'


#  ----------------------------------------------------------------------  finish main logic  ----------------------------------------------------------------------

if __name__ == "__main__":
    if __program_status__ == 1:
        clear_console()
        try:
            Сlient_manager()
        except Exception:
            print('\n\tYou probably aren\'t connected to the internet.\n\tRefresh internet connection and retry.')
            __program_status__ = -1
    print(f'\nProgram status: {__program_status__}')

#  ----------------------------------------------------------------------  finish main logic  ----------------------------------------------------------------------
