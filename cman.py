from os import system
from subprocess import check_output
import requests
from time import sleep


class Сlient_manager():
    """ Represents installing, uninstalling, configurating & editing files of Your client application """

    def __init__(self) -> None:
        self.system_encoding = str(check_output('chcp', shell=True)).split(':')[-1][1:].split('\\')[0]
        print('Client manager application: install, upgrade & add LNetGames\'s games\nVersion 0.1 (beta) | release [M d y (h:m)]\n')
        command = input('> ').lower()
        while not (command in ['get client', 'get games', 'help', '-help', '--help', '?', 'q', 'quit', 'upgrade']):
            print('No such command for client manager :(')
            command = input('\n> ').lower()
        
        while not (command.lower() in ['q', 'quit']):
            if command in ['help', '-help', '--help', '?']:
                self.support()
            elif command == 'get client':
                self.install('client')
            elif command == 'get games':
                self.install('games_module')
            elif command == 'upgrade':
                self.upgrade()
            elif command == 'cls':
                system('cls')
                print('Client manager application: install, upgrade & add LNetGames\'s games\nVersion 0.1 (beta) | release [M d y (h:m)]\n')
            command = input('\n> ')

    def support(self) -> None:
        print('\n\nYou may enter this commands with different cases\n------------------------------------------------')
        print('get client                   uninstall client application')
        print('get games                    install games')
        print('upgrade                      upgrade all modules')
        print('help / -help / --help / ?    get support message like this')
        print('q / quit                     stop client manager')
        print('cls                          clear console\n')

    def handle_connection_status(self) -> str:
        def connection_status() -> bool:
            cur_state = check_output('ipconfig', shell=True).decode(encoding=str(check_output('chcp', shell=True)).split(':')[-1][1:].split('\\')[0]).split('\n')
            return True if any(['IPv4' in line for line in cur_state]) else False
        
        if not connection_status():
            move = input('No interner connection.\n\t* "continue": wait internet connection\n\t* "break": turn to client-manager\n\t> ')
            while not move.lower() in ['continue', 'break']:
                move = input('\n\t* "continue": wait internet connection\n\t* "break": turn to client-manager\n\t> ')
            if move == 'break': return 'break'
        timer = 0
        while True:
            if connection_status(): return 'OK'
            if timer == 0: print('\twaiting internet connection')
            sleep(.5)
            timer += 0.5
            if timer % 10 == 0: print('\twaiting internet connection')
    
    def install(self, file_name) -> bool or None:
        if self.handle_connection_status() == 'break':
            return 'client break'
        url = 'https://raw.githubusercontent.com/Novice2022/LNetGames/main/Games.py' if file_name == 'games_module' else 'https://raw.githubusercontent.com/Novice2022/LNetGames/main/Client.py'
        response = requests.get(url).text
        compare_versions_flag = self.compare_versions(f'{file_name}.py', response.split('\n')[0].replace('\n', '')[3:-1])
        path = str(check_output('cd', shell=True).decode(encoding=self.system_encoding).replace('\b', '')[:-2])
        if compare_versions_flag in ('update', 'not found'):
            with open(f'{file_name}.py', 'w', encoding='utf-8') as f:
                f.write(response.replace('\n', ''))
                if compare_versions_flag == 'not found':
                    print(f'Success!\nInstalled file path: {path}\\games_module.py')
                    return True
                else:
                    print(f'Successfully updated: {path}\\games_module.py')
                    return True
        print(f'You have already installed {file_name}!\nSee: {path}\\games_module.py')
        return True
    
    def upgrade(self) -> bool or None:
        if self.handle_connection_status() == 'break':
            return 'client break'
        print('Upgrading client manager coming soon...')

    @staticmethod
    def compare_versions(exists_file_path: str, request_version: str) -> str:
        try:
            current_version = open(exists_file_path, 'r', encoding='utf-8').readline().replace('\n', '')[3:]
            if current_version != request_version:
                print(f'Changing version:\n{current_version} => {request_version}')
                return 'update'
            return 'OK'
        except FileNotFoundError:
            return 'not found'


def main():
    system('cls')
    cl = Сlient_manager()


if __name__ == "__main__":
    main()
