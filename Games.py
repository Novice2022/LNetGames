#  version: 1.0. Release: 1.03.2023

from os import system
from random import randint


class XO:  # done for offline gaming
    
    def __init__(self, players: list[str]) -> None:
        self.__field = []
        for _ in range(3):
            self.__field.append([' ', ' ', ' '])
        self.__players = [players[0] + ' X', players[1] + ' O']
    
    def run(self) -> None:
        """run() method starts game session"""
        endOfGame = False
        for _ in range(9):
            self.__render()
            self.__getMove()
            if self.__isEndOfGame():
                endOfGame = True
                break
        self.__render(note=False)
        self.__final(endOfGame)
    
    def __getMove(self) -> None:
        while True:
            try:
                coords = list(map(int, input(f'{self.__players[0][:-2]}\'s move ({self.__players[0][-1]}): ').split()))
                if all([coord in [1, 2, 3] for coord in coords]) and len(coords) == 2 and self.__field[coords[0] - 1][coords[1] - 1] == ' ':
                    break
                else:
                    if self.__field[coords[0] - 1][coords[1] - 1] != ' ':
                        print('This field has already been used.\n')
                    else:
                        print('Two coords must be in range from 1 to 3!\n')
            except ValueError:
                print('You should enter just 2 integer numbers.')
        self.__field[coords[0] - 1][coords[1] - 1] = self.__players[0][-1]
        self.__players = self.__players[::-1]

    def __render(self, note: bool=True) -> None:
        system('cls')
        if note:
            print('Note row and column numbers to fill square (2 numbers from 1 to 3 divided with space).\n')
        for i in range(2):
            print(*[f' {e} ' for e in self.__field[i]], sep='|')
            print('---+---+---')
        print(*[f' {e} 'for e in self.__field[2]], sep='|', end='\n\n')
    
    def __isEndOfGame(self) -> bool:
        if any(len(set(row)) == 1 and set(row) != {' '} for row in self.__field) or any(len(set([row[i] for row in self.__field])) == 1 and set([row[i] for row in self.__field]) != {' '} for i in range(3)) or len(set([self.__field[i][j] for i in range(3) for j in range(3) if i + j == 2])) == 1 and set([self.__field[i][j] for i in range(3) for j in range(3) if i + j == 2]) != {' '} or len(set([self.__field[i][j] for i in range(3) for j in range(3) if i == j])) == 1 and set([self.__field[i][j] for i in range(3) for j in range(3) if i == j]) != {' '}:
            return True
        return False
    
    def __final(self, anybodyWin: bool=True) -> None:
        print(f'{self.__players[1][:-2]} won!') if anybodyWin else print('Draw!')
        del self


class SeaBattle:  # done for offline gaming (beta)
    def __init__(self, players: list[str]) -> None:
        self.__players = [players[0], players[1]]
        self.__queue = 'rl'  # shoot left or right field (0 element of current string)
        self.__isEndOfGame = False

    def run(self):
        """run() method starts game session"""
        self.__generateFields()
        while not self.__isEndOfGame:
            self.__render()
            self.__getMove()
        self.__render()
        print(self.__winner + ' won!')

    def __generateFields(self) -> None:
        
        def __fill() -> list[list[str]]:  # done
            field = []
            for _ in range(10):
                field.append([' '] * 10)
            for ship_length in range(4, 0, -1):
                for ship_quantity in range(5 - ship_length):
                    while True:
                        rotation = ['vertical', ''][randint(0, 1)]
                        left_coord, top_coord = 0, 0
                        if ship_length == 1:
                            while True:
                                left_coord, top_coord = randint(1, 10), randint(1, 10)
                                if top_coord == 1:
                                    if (left_coord == 1 and not '#' in [
                                        field[0][0],
                                        field[0][1],
                                        field[1][0],
                                        field[1][1]
                                    ]) or (left_coord == 10 and not '#' in [
                                        field[0][8],
                                        field[0][9],
                                        field[1][8],
                                        field[1][9]
                                    ]) or (left_coord in [_ for _ in range(2, 10)] and not '#' in [
                                        field[0][left_coord    ],
                                        field[0][left_coord - 1],
                                        field[0][left_coord - 2],
                                        field[1][left_coord    ],
                                        field[1][left_coord - 1],
                                        field[1][left_coord - 2]
                                    ]): break
                                elif top_coord == 10:
                                    if (left_coord == 1 and not '#' in [
                                        field[8][0],
                                        field[8][1],
                                        field[9][0],
                                        field[9][1]
                                    ]) or (left_coord == 10 and not '#' in [
                                        field[8][8],
                                        field[8][9],
                                        field[9][8],
                                        field[9][9]
                                    ]) or (left_coord in [_ for _ in range(2, 10)] and not '#' in [
                                        field[8][left_coord    ],
                                        field[8][left_coord - 1],
                                        field[8][left_coord - 2],
                                        field[9][left_coord    ],
                                        field[9][left_coord - 1],
                                        field[9][left_coord - 2]
                                    ]): break
                                else:
                                    if (left_coord == 1 and not '#' in [
                                        field[top_coord - 2][0],
                                        field[top_coord - 2][1],
                                        field[top_coord - 1][0],
                                        field[top_coord - 1][1],
                                        field[top_coord    ][0],
                                        field[top_coord    ][1]
                                    ]) or (left_coord == 10 and not '#' in [
                                        field[top_coord - 2][8],
                                        field[top_coord - 2][9],
                                        field[top_coord - 1][8],
                                        field[top_coord - 1][9],
                                        field[top_coord    ][8],
                                        field[top_coord    ][9]
                                    ]) or (left_coord in [_ for _ in range(2, 10)] and not '#' in [
                                        field[top_coord - 2][left_coord    ],
                                        field[top_coord - 2][left_coord - 1],
                                        field[top_coord - 2][left_coord - 2],
                                        field[top_coord - 1][left_coord    ],
                                        field[top_coord - 1][left_coord - 1],
                                        field[top_coord - 1][left_coord - 2],
                                        field[top_coord    ][left_coord    ],
                                        field[top_coord    ][left_coord - 1],
                                        field[top_coord    ][left_coord - 2]
                                    ]):break
                            field[top_coord - 1][left_coord - 1] = '#'
                            break
                        else:
                            if rotation == 'vertical':
                                while True:
                                    try:
                                        left_coord, top_coord = randint(1, 10), randint(1, 10)
                                        while top_coord + ship_length > 10:
                                            top_coord = randint(1, 10)
                                        good_position = not ('#' in [
                                            field[top_coord - 2][left_coord - 2],
                                            field[top_coord - 2][left_coord - 1],
                                            field[top_coord - 2][left_coord    ],
                                            field[top_coord - 1][left_coord - 2],
                                            field[top_coord - 1][left_coord - 1],
                                            field[top_coord - 1][left_coord    ],
                                            field[top_coord    ][left_coord - 2],
                                            field[top_coord    ][left_coord - 1],
                                            field[top_coord    ][left_coord    ]
                                        ])
                                        if good_position:
                                            if left_coord == 1:
                                                for row in range(top_coord - 1,  top_coord + ship_length):
                                                    if (row == 0 and field[row][1] == '#') or (row == 9 and field[row][1] == '#') or (row in [val for val in range(1, 9)] and (field[row][1] == '#' or field[row + 1][0] == '#')) or field[row + 1][left_coord - 1] == '#' or field[row - 1][left_coord - 1] == '#':
                                                        good_position = False
                                                        break
                                            elif left_coord == 10:
                                                for row in range(top_coord - 1,  top_coord + ship_length):
                                                    if (row == 0 and field[row][8] == '#') or (row == 9 and field[row][8] == '#') or (row in [val for val in range(1, 9)] and (field[row][8] == '#' or field[row + 1][9] == '#')) or field[row + 1][left_coord - 1] == '#' or field[row - 1][left_coord - 1] == '#':
                                                        good_position = False
                                                        break
                                            else:
                                                for row in range(top_coord - 1,  top_coord + ship_length):
                                                    if (row == 0 and ('#' in [field[row][left_coord - 2], field[row][left_coord]])) or (row == 9 and ('#' in [field[row][left_coord - 2], field[row][left_coord]])) or (row in [val for val in range(1, 9)] and ('#' in [
                                                        field[row][left_coord - 2],
                                                        field[row][left_coord],
                                                        field[row + 1][left_coord - 2],
                                                        field[row + 1][left_coord - 1],
                                                        field[row + 1][left_coord]
                                                    ])) or (row == top_coord - 1 and row > 0 and '#' in [
                                                        field[row - 1][left_coord - 2],
                                                        field[row - 1][left_coord - 1],
                                                        field[row - 1][left_coord]
                                                    ]):
                                                        good_position = False
                                                        break
                                            if good_position:
                                                for row in range(top_coord - 1, top_coord + ship_length - 1):
                                                    field[row][left_coord - 1] = '#'
                                                break
                                    except IndexError: ...
                                break
                            else:
                                while True:
                                    try:
                                        left_coord, top_coord = randint(1, 10), randint(1, 10)
                                        while left_coord + ship_length > 10:
                                            left_coord = randint(1, 10)
                                        good_position = not('#' in [
                                            field[top_coord - 2][left_coord - 2],
                                            field[top_coord - 2][left_coord - 1],
                                            field[top_coord - 2][left_coord    ],
                                            field[top_coord - 1][left_coord - 2],
                                            field[top_coord - 1][left_coord - 1],
                                            field[top_coord - 1][left_coord    ],
                                            field[top_coord    ][left_coord - 2],
                                            field[top_coord    ][left_coord - 1],
                                            field[top_coord    ][left_coord    ]])
                                        if good_position:
                                            if top_coord == 1:
                                                for col in range(left_coord - 1,  left_coord + ship_length):
                                                    if (col == 0 and field[1][0] == '#') or (col == 9 and field[1][9] == '#') or (col in [val for val in range(1, 9)] and (field[1][col] == '#' or field[0][col + 1] == '#')):
                                                        good_position = False
                                                        break
                                                if field[top_coord - 1][left_coord - 2] == '#':
                                                    good_position = False
                                            elif top_coord == 10:
                                                if field[top_coord - 1][left_coord - 2] == '#':
                                                    good_position = False
                                                else:
                                                    for col in range(left_coord - 1,  left_coord + ship_length):
                                                        if (col == 0 and field[8][0] == '#') or (col == 9 and field[8][9] == '#') or (col in [val for val in range(1, 9)] and (field[8][col] == '#' or field[9][col + 1]== '#')):
                                                            good_position = False
                                                            break
                                            else:
                                                for col in range(left_coord - 1,  left_coord + ship_length):
                                                    if col == 0 and ('#' in [field[top_coord - 1][top_coord - 2], field[top_coord - 1][top_coord]]) or (col == 9 and ('#' in [field[top_coord - 1][top_coord - 2], field[top_coord - 1][top_coord]])) or (col in [val for val in range(1, 9)] and ('#' in [
                                                        field[top_coord - 1][top_coord - 2],
                                                        field[top_coord - 1][top_coord],
                                                        field[top_coord - 2][col + 1],
                                                        field[top_coord - 1][col + 1],
                                                        field[top_coord    ][col + 1],
                                                    ])) or (col == left_coord - 1 and col > 0 and '#' in [
                                                        field[top_coord - 2][col - 1],
                                                        field[top_coord - 1][col - 1],
                                                        field[top_coord    ][col - 1],
                                                    ]):
                                                        good_position = False
                                                        break
                                            if good_position:
                                                for col in range(left_coord - 1, left_coord + ship_length - 1):
                                                    field[top_coord - 1][col] = '#'
                                                break
                                    except IndexError: ...
                                break
            return field

        self.__player1 = __fill()
        self.__player2 = __fill()
        self.field1 = []
        self.field2 = []
        for _ in range(10):
            self.field1.append([' ' for __ in range(10)])
            self.field2.append([' ' for __ in range(10)])

    def __render(self) -> None:
        system('cls')        
        p1_name = self.__players[0][:10] + '... field:' if len(self.__players[0]) > 9 else self.__players[0][:10] + '\'s field:'
        p2_name = self.__players[1][:10] + '... field:' if len(self.__players[1]) > 9 else self.__players[1][:10] + '\'s field:'
        print('\'#\' - your ship      \' \' - sea      \'X\' - damaged ship      \'~\' - missed\n\n')
        print('   ' + p1_name + ' ' * (30 - len(p1_name)) + p2_name)
        print('__|_A_B_C_D_E_F_G_H_I_J_      __|_A_B_C_D_E_F_G_H_I_J_')
        for i in range(9):
            player1 = str([point for point in self.field1[i]])[2:-2].replace('\', \'', ' ')
            player2 = str([point for point in self.field2[i]])[2:-2].replace('\', \'', ' ')
            line = ''
            if   i == 3: line = f'4 | {player1}    /  4 | {player2}' if self.__queue[0] == 'r' else f'4 | {player1}   \   4 | {player2}'
            elif i == 4: line = f'5 | {player1}   /|  5 | {player2}' if self.__queue[0] == 'r' else f'5 | {player1}   |\  5 | {player2}'
            elif i == 5: line = f'6 | {player1}   \|  6 | {player2}' if self.__queue[0] == 'r' else f'6 | {player1}   |/  6 | {player2}'
            elif i == 6: line = f'7 | {player1}    \  7 | {player2}' if self.__queue[0] == 'r' else f'7 | {player1}   /   7 | {player2}'
            else:        line = f'{i + 1} | {player1}       {i + 1} | {player2}' if self.__queue[0] == 'r' else f'{i + 1} | {player1}       {i + 1} | {player2}'
            print(line)
        print('10| ' + str([point for point in self.field1[9]])[2:-2].replace('\', \'', ' ') +        '       10| ' + str([point for point in self.field2[9]])[2:-2].replace('\', \'', ' '))
        print('------------------------      ------------------------\n')
        print('\n> to get move note row number and columd letter <\n'.upper())
        
        # temp     print('p1:')
        for line in self.__player1:
            print(*line)
        print('\np2:')
        for line in self.__player2:
            print(*line)
        # temp /
        
    def __getMove(self) -> None:

        def __request_coords(msg='') -> list[int, int]:
            print(msg)
            move = input('Shot coordinates: ')
            while True:
                if len(move.split()) == 2:
                    if move.split()[0] in [str(_) for _ in range(1, 11)] and move.split()[1].upper() in [_ for _ in 'ABCDEFGHIJ']:
                        move = [int(move.split()[0]) - 1, [_ for _ in 'ABCDEFGHIJ'].index(move.split()[1].upper())]
                        break
                    print('\n> to get move note row number and columd letter (row: 1 - 10; column: A - J) <')
                    move = input('Shot coordinates: ')
                else:
                    print('\n> to get move note row number and columd letter (row: 1 - 10; column: A - J) <')
                    move = input('Shot coordinates: ')
            return move

        move = __request_coords()
        if self.__queue[0] == 'r':  # shooting to left (player's field)
            point = self.__player1[move[0]][move[1]]
            if point in 'X~':
                __request_coords(msg='Oops! You have used this coordinates before.')
            elif point == '#':
                self.__player1[move[0]][move[1]] = 'X'
                self.field1[move[0]][move[1]] = 'X'
                self.__refresh_isEndOfGame()
                self.__handle_exploding(move)
            elif point == ' ':
                self.__queue = self.__queue[::-1]
                self.__player1[move[0]][move[1]] = '~'
                self.field1[move[0]][move[1]] = '~'
        else:  # shooting to right (opponent's field)
            point = self.__player2[move[0]][move[1]]
            if point in 'X~':
                __request_coords(msg='Oops! You have used this coordinates before.')
            elif point == '#':
                self.__player2[move[0]][move[1]] = 'X'
                self.field2[move[0]][move[1]] = 'X'
                self.__refresh_isEndOfGame()
                self.__handle_exploding(move)
            elif point == ' ':
                self.__queue = self.__queue[::-1]
                self.__player2[move[0]][move[1]] = '~'
                self.field2[move[0]][move[1]] = '~'

    def __refresh_isEndOfGame(self) -> None:
        alive_parts = 0
        for line in self.__player1:
            alive_parts += line.count('#')
        if alive_parts == 0:
            self.__winner = self.__players[1]
            self.__isEndOfGame = True
        alive_parts = 0
        for line in self.__player2:
            alive_parts += line.count('#')
        if alive_parts == 0:
            self.__winner = self.__players[0]
            self.__isEndOfGame = True
    
    def __handle_exploding(self, move: list[int]) -> None:
        
        def  __exploded(field: list[list[str]], move: list[int]) -> list[list[int], str, int]:  # [[topRowCoord, topColumnCoord], shipOrientation]
            line   = move[0]
            column = move[1]
            while line >= 0 and column >= 0:
                try:
                    _break = 0
                    if field[line - 1][column] in 'X#':
                        line -= 1
                    elif field[line - 1][column] in '~ ':
                        _break += 1
                    if field[line][column - 1] in 'X#':
                        column -= 1
                    elif field[line][column - 1] in '~ ':
                        _break += 1
                    if _break == 2:
                        break
                except IndexError: pass
            ship_orientation = 0
            try:
                if field[line + 1][column] in 'X#':
                    ship_orientation = 'ver'
            except IndexError: ...
            try:
                if field[line][column + 1] in 'X#':
                    ship_orientation = 'hor'
            except IndexError: ...
            return [[line, column], ship_orientation]
        
        def __separate(field: list[list[str]], exploded_res: list[list[int], str, int], for_render=False) -> list[list[str]]:
            line   = exploded_res[0][0]
            column = exploded_res[0][1]
            if exploded_res[1] == 0:
                for row in range(line - 1, line + 2):
                    for col in range(column - 1, column + 2):
                        if row in [_ for _ in range(10)] and col in [_ for _ in range(10)] and not (row == line and col == column):
                            field[row][col] = '~'
            elif exploded_res[1] == 'ver':
                shall_separate = True
                length = 1
                for i in range(1, 5):
                    if field[line][column] == '#': shall_separate = False; break
                    if line + i > 9: break
                    if field[line + i][column] in '~ ': break
                    elif field[line + i][column] == '#': shall_separate = False
                    else: length += 1
                if shall_separate:
                    if line == 0:
                        if column == 0:
                            for row in range(length):
                                field[row][1] = '~'
                            field[line + length][0], field[line + length][1] = '~', '~'
                        elif column == 9:
                            for row in range(length):
                                field[row][8] = '~'
                            field[length][8], field[length][9] = '~', '~'
                        else:
                            for row in range(length):
                                field[row][column - 1], field[row][column + 1] = '~', '~'
                            field[length][column - 1], field[length][column], field[length][column + 1] = '~', '~', '~'
                    elif line == 9:  # ok
                        if column == 0:
                            field[8][0], field[8][1], field[9][1] = '~', '~', '~'
                        elif column == 9:
                            field[8][8], field[8][9], field[9][8] = '~', '~', '~'
                        else:
                            field[8][column - 1], field[8][column], field[8][column + 1], field[9][column - 1], field[9][column + 1] = '~', '~', '~', '~', '~'
                    else:
                        if column == 0:
                            field[line - 1][0], field[line - 1][1] = '~', '~'
                            for i in range(length):
                                if line + i > 9:
                                    break
                                field[line + i][1] = '~'
                            if line + length < 10:
                                field[line + length][0], field[line + length][1] = '~', '~'
                        elif column == 9:
                            field[line - 1][8], field[line - 1][9] = '~', '~'
                            for i in range(length):
                                if line + i > 9:
                                    break
                                field[line + i][8] = '~'
                            if line + length < 10:
                                field[line + length][8], field[line + length][9] = '~', '~'
                        else:
                            field[line - 1][column - 1], field[line - 1][column], field[line - 1][column + 1] = '~', '~', '~'
                            for i in range(length):
                                if line + i > 9:
                                    break
                                field[line + i][column - 1], field[line + i][column + 1] = '~', '~'
                            if line + length < 10:
                                field[line + length][column - 1], field[line + length][column], field[line + length][column + 1] = '~', '~', '~'
            elif exploded_res[1] == 'hor':
                shall_separate = True
                length = 1
                for i in range(1, 5):
                    if field[line][column] == '#': shall_separate = False; break
                    if line + i > 9: break
                    if field[line][column + i] in '~ ': break
                    elif field[line][column + i] == '#': shall_separate = False
                    else: length += 1
                if shall_separate:
                    if line == 0:
                        if column == 0:
                            for col in range(length):
                                field[1][col] = '~'
                            field[0][column + length], field[1][column + length] = '~', '~'
                        elif column == 9:
                            for col in range(length):
                                field[8][col] = '~'
                            field[length][8], field[length][9] = '~', '~'
                        else:
                            field[0][column - 1], field[1][column - 1] = '~', '~'
                            for col in range(column, column + length):
                                field[1][col] = '~'
                            field[1][column + length - 2], field[0][column + length - 2] = '~', '~'
                    elif line == 9:
                        if column == 0:
                            field[8][0], field[8][1], field[9][1] = '~', '~', '~'
                        elif column == 9:
                            field[8][8], field[8][9], field[9][8] = '~', '~', '~'
                        else:
                            field[line - 1][8], field[line][8], field[line + 1][8], field[line - 1][9], field[line + 1][9] = '~', '~', '~', '~', '~'
                    else:
                        if column == 0:
                            for col in range(column, column + length):
                                if col > 8:
                                    break
                                field[line - 1][col], field[line + 1][col] = '~', '~'
                            if column + length < 10:
                                field[line - 1][column + length], field[line][column + length], field[line + 1][column + length] = '~', '~', '~'
                        elif column == 9:
                            field[8][column - 1], field[9][column - 1] = '~', '~'
                            for i in range(length):
                                if column + i > 9:
                                    break
                                field[8][column + i] = '~'
                            if column + length < 10:
                                field[8][column + length], field[9][column + length] = '~', '~'
                        else:
                            field[line - 1][column - 1], field[line][column - 1], field[line + 1][column - 1] = '~', '~', '~'
                            for i in range(length):
                                if column + i > 9:
                                    break
                                field[line - 1][column + i], field[line + 1][column + i] = '~', '~'
                            if column + length < 10:
                                field[line - 1][column + length], field[line][column + length], field[line + 1][column + length] = '~', '~', '~'
            else:
                print('smth went wrong when it was in move definition (Sea Battle -> __handle_exploding() -> __separate())')
                system('pause')
            return field

        exploed_result = __exploded(self.__player1, move) if self.__queue == 'rl' else __exploded(self.__player2, move)
        if self.__queue == 'rl':
            self.__player1 = __separate(self.__player1, exploed_result)
            self.field1 = [[e for e in ''.join(line).replace('#', ' ')] for line in self.__player1]
        else:
            self.__player2 = __separate(self.__player2, exploed_result)
            self.field2 = [[e for e in ''.join(line).replace('#', ' ')] for line in self.__player2]


def main() -> None:
    system('cls')
    choose = input('Choose the game:\n1: XO\n2: Sea battle\n\nYour choose: ').strip(' ')
    while not (choose in [1, 2] or choose in ['1', '2']):
        system('cls')
        try: choose = int(input('\'1\' to play XO\n\'2\' to play Sea battle\n\nYour choose: '))
        except ValueError: system('cls')
    choose = int(choose)
    system('cls')
    if choose == 1:
        session = XO(input('Enter User\'s names (2 words): ').split())
        session.run()
    else:
        session = SeaBattle(input('Enter User\'s names (2 words): ').split())
        session.run()


if __name__ == '__main__':
    main()


"""
    .==================================================.
    ||   .=====.      .=.  .====.   .====.  .=====.   ||
    ||   *   //      //||  ||   \\    ||   ||    ||   ||
    ||      //      //_||  ||___//    ||   ||         ||
    ||     //      //``||  ||```\\    ||   || .===.   ||
    ||    //   .  //   ||  ||    ||   ||   ||    ||   ||
    ||   *=====* *=*  *=*  *=====*  *====*  *====*    ||
    '=================================================='

"""
