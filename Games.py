from os import system  # tabs: 0
from random import randint  # tabs: 0


class XO:  # done for offline gaming  # tabs: 0
    # done  # tabs: 1
    def __init__(self, players: list[str]) -> None:  # tabs: 1
        self.__field = []  # tabs: 2
        for _ in range(3):  # tabs: 2
            self.__field.append([' ', ' ', ' '])  # tabs: 3
        self.__players = [players[0] + ' X', players[1] + ' O']  # tabs: 2
      # tabs: 1
    # done  # tabs: 1
    def run(self) -> None:  # tabs: 1
        """run() method starts game session"""  # tabs: 2
        endOfGame = False  # tabs: 2
        for _ in range(9):  # tabs: 2
            self.__render()  # tabs: 3
            self.__getMove()  # tabs: 3
            if self.__isEndOfGame():  # tabs: 3
                endOfGame = True  # tabs: 4
                break  # tabs: 4
        self.__render(note=False)  # tabs: 2
        self.__final(endOfGame)  # tabs: 2
      # tabs: 1
    # done  # tabs: 1
    def __getMove(self) -> None:  # tabs: 1
        while True:  # tabs: 2
            try:  # tabs: 3
                coords = list(map(int, input(f'{self.__players[0][:-2]}\'s move ({self.__players[0][-1]}): ').split()))  # tabs: 4
                if all([coord in [1, 2, 3] for coord in coords]) and len(coords) == 2 and self.__field[coords[0] - 1][coords[1] - 1] == ' ':  # tabs: 4
                    break  # tabs: 5
                else:  # tabs: 4
                    if self.__field[coords[0] - 1][coords[1] - 1] != ' ':  # tabs: 5
                        print('This field has already been used.\n')  # tabs: 6
                    else:  # tabs: 5
                        print('Two coords must be in range from 1 to 3!\n')  # tabs: 6
            except ValueError:  # tabs: 3
                print('You should enter just 2 integer numbers.')  # tabs: 4
        self.__field[coords[0] - 1][coords[1] - 1] = self.__players[0][-1]  # tabs: 2
        self.__players = self.__players[::-1]  # tabs: 2

    # done  # tabs: 1
    def __render(self, note: bool=True) -> None:  # tabs: 1
        system('cls')  # tabs: 2
        if note:  # tabs: 2
            print('Note row and column numbers to fill square (2 numbers from 1 to 3 divided with space).\n')  # tabs: 3
        for i in range(2):  # tabs: 2
            print(*[f' {e} ' for e in self.__field[i]], sep='|')  # tabs: 3
            print('---+---+---')  # tabs: 3
        print(*[f' {e} 'for e in self.__field[2]], sep='|', end='\n\n')  # tabs: 2
      # tabs: 1
    # done  # tabs: 1
    def __isEndOfGame(self) -> bool:  # tabs: 1
        if any(len(set(row)) == 1 and set(row) != {' '} for row in self.__field) or any(len(set([row[i] for row in self.__field])) == 1 and set([row[i] for row in self.__field]) != {' '} for i in range(3)) or len(set([self.__field[i][j] for i in range(3) for j in range(3) if i + j == 2])) == 1 and set([self.__field[i][j] for i in range(3) for j in range(3) if i + j == 2]) != {' '} or len(set([self.__field[i][j] for i in range(3) for j in range(3) if i == j])) == 1 and set([self.__field[i][j] for i in range(3) for j in range(3) if i == j]) != {' '}:  # tabs: 2
            return True  # tabs: 3
        return False  # tabs: 2
      # tabs: 1
    # done  # tabs: 1
    def __final(self, anybodyWin: bool=True) -> None:  # tabs: 1
        print(f'{self.__players[1][:-2]} won!') if anybodyWin else print('Draw!')  # tabs: 2
        del self  # tabs: 2


class SeaBattle:  # tabs: 0
    # done  # tabs: 1
    def __init__(self, players: list[str]) -> None:  # tabs: 1
        self.__players = [players[0], players[1]]  # tabs: 2
        self.__queue = 'rl'  # shoot left or right field (0 element of current string)  # tabs: 2
        self.__isEndOfGame = False  # tabs: 2

    # done  # tabs: 1
    def run(self):  # tabs: 1
        """run() method starts game session"""  # tabs: 2
        self.__generateFields()  # tabs: 2
        while not self.__isEndOfGame:  # tabs: 2
            self.__render()  # tabs: 3
            self.__getMove()  # tabs: 3
        self.__render()  # tabs: 2
        print(self.__winner + ' won!')  # tabs: 2

    # done  # tabs: 1
    def __generateFields(self) -> None:  # tabs: 1
          # tabs: 2
        def __fill() -> list[list[str]]:  # done  # tabs: 2
            field = []  # tabs: 3
            for _ in range(10):  # tabs: 3
                field.append([' '] * 10)  # tabs: 4
            for ship_length in range(4, 0, -1):  # tabs: 3
                for ship_quantity in range(5 - ship_length):  # tabs: 4
                    while True:  # tabs: 5
                        rotation = ['vertical', ''][randint(0, 1)]  # tabs: 6
                        left_coord, top_coord = 0, 0  # tabs: 6
                        if ship_length == 1:  # tabs: 6
                            while True:  # tabs: 7
                                left_coord, top_coord = randint(1, 10), randint(1, 10)  # tabs: 8
                                if top_coord == 1:  # tabs: 8
                                    if (left_coord == 1 and not '#' in [  # tabs: 9
                                        field[0][0],  # tabs: 10
                                        field[0][1],  # tabs: 10
                                        field[1][0],  # tabs: 10
                                        field[1][1]  # tabs: 10
                                    ]) or (left_coord == 10 and not '#' in [  # tabs: 9
                                        field[0][8],  # tabs: 10
                                        field[0][9],  # tabs: 10
                                        field[1][8],  # tabs: 10
                                        field[1][9]  # tabs: 10
                                    ]) or (left_coord in [_ for _ in range(2, 10)] and not '#' in [  # tabs: 9
                                        field[0][left_coord    ],  # tabs: 11
                                        field[0][left_coord - 1],  # tabs: 10
                                        field[0][left_coord - 2],  # tabs: 10
                                        field[1][left_coord    ],  # tabs: 11
                                        field[1][left_coord - 1],  # tabs: 10
                                        field[1][left_coord - 2]  # tabs: 10
                                    ]): break  # tabs: 9
                                elif top_coord == 10:  # tabs: 8
                                    if (left_coord == 1 and not '#' in [  # tabs: 9
                                        field[8][0],  # tabs: 10
                                        field[8][1],  # tabs: 10
                                        field[9][0],  # tabs: 10
                                        field[9][1]  # tabs: 10
                                    ]) or (left_coord == 10 and not '#' in [  # tabs: 9
                                        field[8][8],  # tabs: 10
                                        field[8][9],  # tabs: 10
                                        field[9][8],  # tabs: 10
                                        field[9][9]  # tabs: 10
                                    ]) or (left_coord in [_ for _ in range(2, 10)] and not '#' in [  # tabs: 9
                                        field[8][left_coord    ],  # tabs: 11
                                        field[8][left_coord - 1],  # tabs: 10
                                        field[8][left_coord - 2],  # tabs: 10
                                        field[9][left_coord    ],  # tabs: 11
                                        field[9][left_coord - 1],  # tabs: 10
                                        field[9][left_coord - 2]  # tabs: 10
                                    ]): break  # tabs: 9
                                else:  # tabs: 8
                                    if (left_coord == 1 and not '#' in [  # tabs: 9
                                            field[top_coord - 2][0],  # tabs: 11
                                            field[top_coord - 2][1],  # tabs: 11
                                            field[top_coord - 1][0],  # tabs: 11
                                            field[top_coord - 1][1],  # tabs: 11
                                            field[top_coord    ][0],  # tabs: 12
                                            field[top_coord    ][1]  # tabs: 12
                                        ]) or (left_coord == 10 and not '#' in [  # tabs: 10
                                            field[top_coord - 2][8],  # tabs: 11
                                            field[top_coord - 2][9],  # tabs: 11
                                            field[top_coord - 1][8],  # tabs: 11
                                            field[top_coord - 1][9],  # tabs: 11
                                            field[top_coord    ][8],  # tabs: 12
                                            field[top_coord    ][9]  # tabs: 12
                                        ]) or (left_coord in [_ for _ in range(2, 10)] and not '#' in [  # tabs: 10
                                            field[top_coord - 2][left_coord    ],  # tabs: 12
                                            field[top_coord - 2][left_coord - 1],  # tabs: 11
                                            field[top_coord - 2][left_coord - 2],  # tabs: 11
                                            field[top_coord - 1][left_coord    ],  # tabs: 12
                                            field[top_coord - 1][left_coord - 1],  # tabs: 11
                                            field[top_coord - 1][left_coord - 2],  # tabs: 11
                                            field[top_coord    ][left_coord    ],  # tabs: 13
                                            field[top_coord    ][left_coord - 1],  # tabs: 12
                                            field[top_coord    ][left_coord - 2]  # tabs: 12
                                        ]):break  # tabs: 10
                            field[top_coord - 1][left_coord - 1] = '#'  # tabs: 7
                            break  # tabs: 7
                        else:  # tabs: 6
                            if rotation == 'vertical':  # tabs: 7
                                while True:  # tabs: 8
                                    try:  # tabs: 9
                                        left_coord, top_coord = randint(1, 10), randint(1, 10)  # tabs: 10
                                        while top_coord + ship_length > 10:  # tabs: 10
                                            top_coord = randint(1, 10)  # tabs: 11
                                        good_position = not ('#' in [  # tabs: 10
                                            field[top_coord - 2][left_coord - 2],  # tabs: 11
                                            field[top_coord - 2][left_coord - 1],  # tabs: 11
                                            field[top_coord - 2][left_coord    ],  # tabs: 12
                                            field[top_coord - 1][left_coord - 2],  # tabs: 11
                                            field[top_coord - 1][left_coord - 1],  # tabs: 11
                                            field[top_coord - 1][left_coord    ],  # tabs: 12
                                            field[top_coord    ][left_coord - 2],  # tabs: 12
                                            field[top_coord    ][left_coord - 1],  # tabs: 12
                                            field[top_coord    ][left_coord    ]  # tabs: 13
                                        ])  # tabs: 10
                                        if good_position:  # tabs: 10
                                            if left_coord == 1:  # tabs: 11
                                                for row in range(top_coord - 1,  top_coord + ship_length):  # tabs: 12
                                                    if (row == 0 and field[row][1] == '#') or (row == 9 and field[row][1] == '#') or (row in [val for val in range(1, 9)] and (field[row][1] == '#' or field[row + 1][0] == '#')) or field[row + 1][left_coord - 1] == '#' or field[row - 1][left_coord - 1] == '#':  # tabs: 13
                                                        good_position = False  # tabs: 14
                                                        break  # tabs: 14
                                            elif left_coord == 10:  # tabs: 11
                                                for row in range(top_coord - 1,  top_coord + ship_length):  # tabs: 12
                                                    if (row == 0 and field[row][8] == '#') or (row == 9 and field[row][8] == '#') or (row in [val for val in range(1, 9)] and (field[row][8] == '#' or field[row + 1][9] == '#')) or field[row + 1][left_coord - 1] == '#' or field[row - 1][left_coord - 1] == '#':  # tabs: 13
                                                        good_position = False  # tabs: 14
                                                        break  # tabs: 14
                                            else:  # tabs: 11
                                                for row in range(top_coord - 1,  top_coord + ship_length):  # tabs: 12
                                                    if (row == 0 and ('#' in [field[row][left_coord - 2], field[row][left_coord]])) or (row == 9 and ('#' in [field[row][left_coord - 2], field[row][left_coord]])) or (row in [val for val in range(1, 9)] and ('#' in [  # tabs: 13
                                                        field[row][left_coord - 2],  # tabs: 14
                                                        field[row][left_coord],  # tabs: 14
                                                        field[row + 1][left_coord - 2],  # tabs: 14
                                                        field[row + 1][left_coord - 1],  # tabs: 14
                                                        field[row + 1][left_coord]  # tabs: 14
                                                    ])) or (row == top_coord - 1 and row > 0 and '#' in [  # tabs: 13
                                                        field[row - 1][left_coord - 2],  # tabs: 14
                                                        field[row - 1][left_coord - 1],  # tabs: 14
                                                        field[row - 1][left_coord]  # tabs: 14
                                                    ]):  # tabs: 13
                                                        good_position = False  # tabs: 14
                                                        break  # tabs: 14
                                            if good_position:  # tabs: 11
                                                for row in range(top_coord - 1, top_coord + ship_length - 1):  # tabs: 12
                                                    field[row][left_coord - 1] = '#'  # tabs: 13
                                                break  # tabs: 12
                                    except IndexError: ...  # tabs: 9
                                break  # tabs: 8
                            else:  # tabs: 7
                                while True:  # tabs: 8
                                    try:  # tabs: 9
                                        left_coord, top_coord = randint(1, 10), randint(1, 10)  # tabs: 10
                                        while left_coord + ship_length > 10:  # tabs: 10
                                            left_coord = randint(1, 10)  # tabs: 11
                                        good_position = not('#' in [  # tabs: 10
                                            field[top_coord - 2][left_coord - 2],  # tabs: 11
                                            field[top_coord - 2][left_coord - 1],  # tabs: 11
                                            field[top_coord - 2][left_coord    ],  # tabs: 12
                                            field[top_coord - 1][left_coord - 2],  # tabs: 11
                                            field[top_coord - 1][left_coord - 1],  # tabs: 11
                                            field[top_coord - 1][left_coord    ],  # tabs: 12
                                            field[top_coord    ][left_coord - 2],  # tabs: 12
                                            field[top_coord    ][left_coord - 1],  # tabs: 12
                                            field[top_coord    ][left_coord    ]])  # tabs: 13
                                        if good_position:  # tabs: 10
                                            if top_coord == 1:  # tabs: 11
                                                for col in range(left_coord - 1,  left_coord + ship_length):  # tabs: 12
                                                    if (col == 0 and field[1][0] == '#') or (col == 9 and field[1][9] == '#') or (col in [val for val in range(1, 9)] and (field[1][col] == '#' or field[0][col + 1] == '#')):  # tabs: 13
                                                        good_position = False  # tabs: 14
                                                        break  # tabs: 14
                                                if field[top_coord - 1][left_coord - 2] == '#':  # tabs: 12
                                                    good_position = False  # tabs: 13
                                            elif top_coord == 10:  # tabs: 11
                                                if field[top_coord - 1][left_coord - 2] == '#':  # tabs: 12
                                                    good_position = False  # tabs: 13
                                                else:  # tabs: 12
                                                    for col in range(left_coord - 1,  left_coord + ship_length):  # tabs: 13
                                                        if (col == 0 and field[8][0] == '#') or (col == 9 and field[8][9] == '#') or (col in [val for val in range(1, 9)] and (field[8][col] == '#' or field[9][col + 1]== '#')):  # tabs: 14
                                                            good_position = False  # tabs: 15
                                                            break  # tabs: 15
                                            else:  # tabs: 11
                                                for col in range(left_coord - 1,  left_coord + ship_length):  # tabs: 12
                                                    if col == 0 and ('#' in [field[top_coord - 1][top_coord - 2], field[top_coord - 1][top_coord]]) or (col == 9 and ('#' in [field[top_coord - 1][top_coord - 2], field[top_coord - 1][top_coord]])) or (col in [val for val in range(1, 9)] and ('#' in [  # tabs: 13
                                                        field[top_coord - 1][top_coord - 2],  # tabs: 14
                                                        field[top_coord - 1][top_coord],  # tabs: 14
                                                        field[top_coord - 2][col + 1],  # tabs: 14
                                                        field[top_coord - 1][col + 1],  # tabs: 14
                                                        field[top_coord    ][col + 1],  # tabs: 15
                                                    ])) or (col == left_coord - 1 and col > 0 and '#' in [  # tabs: 13
                                                        field[top_coord - 2][col - 1],  # tabs: 14
                                                        field[top_coord - 1][col - 1],  # tabs: 14
                                                        field[top_coord    ][col - 1],  # tabs: 15
                                                    ]):  # tabs: 13
                                                        good_position = False  # tabs: 14
                                                        break  # tabs: 14
                                            if good_position:  # tabs: 11
                                                for col in range(left_coord - 1, left_coord + ship_length - 1):  # tabs: 12
                                                    field[top_coord - 1][col] = '#'  # tabs: 13
                                                break  # tabs: 12
                                    except IndexError: ...  # tabs: 9
                                break  # tabs: 8
            return field  # tabs: 3

        self.__player1 = __fill()  # tabs: 2
        self.__player2 = __fill()  # tabs: 2
        self.field1 = []  # tabs: 2
        self.field2 = []  # tabs: 2
        for _ in range(10):  # tabs: 2
            self.field1.append([' ' for __ in range(10)])  # tabs: 3
            self.field2.append([' ' for __ in range(10)])  # tabs: 3

    # done  # tabs: 1
    def __render(self) -> None:  # tabs: 1
        system('cls')          # tabs: 4
        p1_name = self.__players[0][:10] + '... field:' if len(self.__players[0]) > 9 else self.__players[0][:10] + '\'s field:'  # tabs: 2
        p2_name = self.__players[1][:10] + '... field:' if len(self.__players[1]) > 9 else self.__players[1][:10] + '\'s field:'  # tabs: 2
        print('\'#\' - your ship      \' \' - sea      \'X\' - damaged ship      \'~\' - missed\n\n')  # tabs: 5
        print('   ' + p1_name + ' ' * (30 - len(p1_name)) + p2_name)  # tabs: 2
        print('__|_A_B_C_D_E_F_G_H_I_J_      __|_A_B_C_D_E_F_G_H_I_J_')  # tabs: 3
        for i in range(9):  # tabs: 2
            player1 = str([point for point in self.field1[i]])[2:-2].replace('\', \'', ' ')  # tabs: 3
            player2 = str([point for point in self.field2[i]])[2:-2].replace('\', \'', ' ')  # tabs: 3
            line = ''  # tabs: 3
            if   i == 3: line = f'4 | {player1}    /  4 | {player2}' if self.__queue[0] == 'r' else f'4 | {player1}   \   4 | {player2}'  # tabs: 4
            elif i == 4: line = f'5 | {player1}   /|  5 | {player2}' if self.__queue[0] == 'r' else f'5 | {player1}   |\  5 | {player2}'  # tabs: 3
            elif i == 5: line = f'6 | {player1}   \|  6 | {player2}' if self.__queue[0] == 'r' else f'6 | {player1}   |/  6 | {player2}'  # tabs: 3
            elif i == 6: line = f'7 | {player1}    \  7 | {player2}' if self.__queue[0] == 'r' else f'7 | {player1}   /   7 | {player2}'  # tabs: 4
            else:        line = f'{i + 1} | {player1}       {i + 1} | {player2}' if self.__queue[0] == 'r' else f'{i + 1} | {player1}       {i + 1} | {player2}'  # tabs: 7
            print(line)  # tabs: 3
        print('10| ' + str([point for point in self.field1[9]])[2:-2].replace('\', \'', ' ') +        '       10| ' + str([point for point in self.field2[9]])[2:-2].replace('\', \'', ' '))  # tabs: 5
        print('------------------------      ------------------------\n')  # tabs: 3
        print('\n> to get move note row number and columd letter <\n'.upper())  # tabs: 2
          # tabs: 2
        # temp     print('p1:')  # tabs: 3
        for line in self.__player1:  # tabs: 2
            print(*line)  # tabs: 3
        print('\np2:')  # tabs: 2
        for line in self.__player2:  # tabs: 2
            print(*line)  # tabs: 3
        # temp /  # tabs: 2
          # tabs: 2
    # done  # tabs: 1
    def __getMove(self) -> None:  # tabs: 1

        # done  # tabs: 2
        def __request_coords(msg='') -> list[int, int]:  # tabs: 2
            print(msg)  # tabs: 3
            move = input('Shot coordinates: ')  # tabs: 3
            while True:  # tabs: 3
                if len(move.split()) == 2:  # tabs: 4
                    if move.split()[0] in [str(_) for _ in range(1, 11)] and move.split()[1].upper() in [_ for _ in 'ABCDEFGHIJ']:  # tabs: 5
                        move = [int(move.split()[0]) - 1, [_ for _ in 'ABCDEFGHIJ'].index(move.split()[1].upper())]  # tabs: 6
                        break  # tabs: 6
                    print('\n> to get move note row number and columd letter (row: 1 - 10; column: A - J) <')  # tabs: 5
                    move = input('Shot coordinates: ')  # tabs: 5
                else:  # tabs: 4
                    print('\n> to get move note row number and columd letter (row: 1 - 10; column: A - J) <')  # tabs: 5
                    move = input('Shot coordinates: ')  # tabs: 5
            return move  # tabs: 3

        move = __request_coords()  # tabs: 2
        if self.__queue[0] == 'r':  # shooting to left (player's field)  # tabs: 2
            point = self.__player1[move[0]][move[1]]  # tabs: 3
            if point in 'X~':  # tabs: 3
                __request_coords(msg='Oops! You have used this coordinates before.')  # tabs: 4
            elif point == '#':  # tabs: 3
                self.__player1[move[0]][move[1]] = 'X'  # tabs: 4
                self.field1[move[0]][move[1]] = 'X'  # tabs: 4
                self.__refresh_isEndOfGame()  # tabs: 4
                self.__handle_exploding(move)  # tabs: 4
            elif point == ' ':  # tabs: 3
                self.__queue = self.__queue[::-1]  # tabs: 4
                self.__player1[move[0]][move[1]] = '~'  # tabs: 4
                self.field1[move[0]][move[1]] = '~'  # tabs: 4
        else:  # shooting to right (opponent's field)  # tabs: 2
            point = self.__player2[move[0]][move[1]]  # tabs: 3
            if point in 'X~':  # tabs: 3
                __request_coords(msg='Oops! You have used this coordinates before.')  # tabs: 4
            elif point == '#':  # tabs: 3
                self.__player2[move[0]][move[1]] = 'X'  # tabs: 4
                self.field2[move[0]][move[1]] = 'X'  # tabs: 4
                self.__refresh_isEndOfGame()  # tabs: 4
                self.__handle_exploding(move)  # tabs: 4
            elif point == ' ':  # tabs: 3
                self.__queue = self.__queue[::-1]  # tabs: 4
                self.__player2[move[0]][move[1]] = '~'  # tabs: 4
                self.field2[move[0]][move[1]] = '~'  # tabs: 4

      # tabs: 1
    # done  # tabs: 1
    def __refresh_isEndOfGame(self) -> None:  # tabs: 1
        alive_parts = 0  # tabs: 2
        for line in self.__player1:  # tabs: 2
            alive_parts += line.count('#')  # tabs: 3
        if alive_parts == 0:  # tabs: 2
            self.__winner = self.__players[1]  # tabs: 3
            self.__isEndOfGame = True  # tabs: 3
        alive_parts = 0  # tabs: 2
        for line in self.__player2:  # tabs: 2
            alive_parts += line.count('#')  # tabs: 3
        if alive_parts == 0:  # tabs: 2
            self.__winner = self.__players[0]  # tabs: 3
            self.__isEndOfGame = True  # tabs: 3
      # tabs: 1
      # tabs: 1
    def __handle_exploding(self, move: list[int]) -> None:  # tabs: 1
          # tabs: 2
        def  __exploded(field: list[list[str]], move: list[int]) -> list[list[int], str, int]:  # [[topRowCoord, topColumnCoord], shipOrientation]  # tabs: 2

            # define variables \  # tabs: 3

            line   = move[0]  # tabs: 3
            column = move[1]  # tabs: 3

            # define variables /  # tabs: 3

            while line >= 0 and column >= 0:  # tabs: 3
                try:  # tabs: 4
                    _break = 0  # tabs: 5
                    if field[line - 1][column] in 'X#':  # tabs: 5
                        line -= 1  # tabs: 6
                    elif field[line - 1][column] in '~ ':  # tabs: 5
                        _break += 1  # tabs: 6
                    if field[line][column - 1] in 'X#':  # tabs: 5
                        column -= 1  # tabs: 6
                    elif field[line][column - 1] in '~ ':  # tabs: 5
                        _break += 1  # tabs: 6
                    if _break == 2:  # tabs: 5
                        break  # tabs: 6
                except IndexError: pass  # tabs: 4
            ship_orientation = 0  # tabs: 3
            try:  # tabs: 3
                if field[line + 1][column] in 'X#':  # tabs: 4
                    ship_orientation = 'ver'  # tabs: 5
            except IndexError: ...  # tabs: 3
            try:  # tabs: 3
                if field[line][column + 1] in 'X#':  # tabs: 4
                    ship_orientation = 'hor'  # tabs: 5
            except IndexError: ...  # tabs: 3
            return [[line, column], ship_orientation]  # tabs: 3
          # tabs: 2
        def __separate(field: list[list[str]], exploded_res: list[list[int], str, int], for_render=False) -> list[list[str]]:  # tabs: 2
              # tabs: 3
            # define variables \  # tabs: 3

            line   = exploded_res[0][0]  # tabs: 3
            column = exploded_res[0][1]  # tabs: 3

            # define variables /  # tabs: 3

            if exploded_res[1] == 0:  # tabs: 3
                for row in range(line - 1, line + 2):  # tabs: 4
                    for col in range(column - 1, column + 2):  # tabs: 5
                        if row in [_ for _ in range(10)] and col in [_ for _ in range(10)] and not (row == line and col == column):  # tabs: 6
                            field[row][col] = '~'  # tabs: 7
            elif exploded_res[1] == 'ver':  # tabs: 3
                shall_separate = True  # tabs: 4
                length = 1  # tabs: 4
                for i in range(1, 5):  # tabs: 4
                    if field[line][column] == '#': shall_separate = False; break  # tabs: 5
                    if line + i > 9: break  # tabs: 5
                    if field[line + i][column] in '~ ': break  # tabs: 5
                    elif field[line + i][column] == '#': shall_separate = False  # tabs: 5
                    else: length += 1  # tabs: 5
                if shall_separate:  # tabs: 4
                    if line == 0:  # tabs: 5
                        if column == 0:  # tabs: 6
                            for row in range(length):  # tabs: 7
                                field[row][1] = '~'  # tabs: 8
                            field[line + length][0], field[line + length][1] = '~', '~'  # tabs: 7
                        elif column == 9:  # tabs: 6
                            for row in range(length):  # tabs: 7
                                field[row][8] = '~'  # tabs: 8
                            field[length][8], field[length][9] = '~', '~'  # tabs: 7
                        else:  # tabs: 6
                            for row in range(length):  # tabs: 7
                                field[row][column - 1], field[row][column + 1] = '~', '~'  # tabs: 8
                            field[length][column - 1], field[length][column], field[length][column + 1] = '~', '~', '~'  # tabs: 7
                    elif line == 9:  # ok  # tabs: 5
                        if column == 0:  # tabs: 6
                            field[8][0], field[8][1], field[9][1] = '~', '~', '~'  # tabs: 7
                        elif column == 9:  # tabs: 6
                            field[8][8], field[8][9], field[9][8] = '~', '~', '~'  # tabs: 7
                        else:  # tabs: 6
                            field[8][column - 1], field[8][column], field[8][column + 1], field[9][column - 1], field[9][column + 1] = '~', '~', '~', '~', '~'  # tabs: 7
                    else:  # tabs: 5
                        if column == 0:  # tabs: 6
                            field[line - 1][0], field[line - 1][1] = '~', '~'  # tabs: 7
                            for i in range(length):  # tabs: 7
                                if line + i > 9:  # tabs: 8
                                    break  # tabs: 9
                                field[line + i][1] = '~'  # tabs: 8
                            if line + length < 10:  # tabs: 7
                                field[line + length][0], field[line + length][1] = '~', '~'  # tabs: 8
                        elif column == 9:  # tabs: 6
                            field[line - 1][8], field[line - 1][9] = '~', '~'  # tabs: 7
                            for i in range(length):  # tabs: 7
                                if line + i > 9:  # tabs: 8
                                    break  # tabs: 9
                                field[line + i][8] = '~'  # tabs: 8
                            if line + length < 10:  # tabs: 7
                                field[line + length][8], field[line + length][9] = '~', '~'  # tabs: 8
                        else:  # tabs: 6
                            field[line - 1][column - 1], field[line - 1][column], field[line - 1][column + 1] = '~', '~', '~'  # tabs: 7
                            for i in range(length):  # tabs: 7
                                if line + i > 9:  # tabs: 8
                                    break  # tabs: 9
                                field[line + i][column - 1], field[line + i][column + 1] = '~', '~'  # tabs: 8
                            if line + length < 10:  # tabs: 7
                                field[line + length][column - 1], field[line + length][column], field[line + length][column + 1] = '~', '~', '~'  # tabs: 8
            elif exploded_res[1] == 'hor':  # tabs: 3
                shall_separate = True  # tabs: 4
                length = 1  # tabs: 4
                for i in range(1, 5):  # tabs: 4
                    if field[line][column] == '#': shall_separate = False; break  # tabs: 5
                    if line + i > 9: break  # tabs: 5
                    if field[line][column + i] in '~ ': break  # tabs: 5
                    elif field[line][column + i] == '#': shall_separate = False  # tabs: 5
                    else: length += 1  # tabs: 5
                if shall_separate:  # tabs: 4
                    if line == 0:  # tabs: 5
                        if column == 0:  # tabs: 6
                            for col in range(length):  # tabs: 7
                                field[1][col] = '~'  # tabs: 8
                            field[0][column + length], field[1][column + length] = '~', '~'  # tabs: 7
                        elif column == 9:  # tabs: 6
                            for col in range(length):  # tabs: 7
                                field[8][col] = '~'  # tabs: 8
                            field[length][8], field[length][9] = '~', '~'  # tabs: 7
                        else:  # tabs: 6
                            field[0][column - 1], field[1][column - 1] = '~', '~'  # tabs: 7
                            for col in range(column, column + length):  # tabs: 7
                                field[1][col] = '~'  # tabs: 8
                            field[1][col + length - 2], field[0][col + length - 2] = '~', '~'  # tabs: 7
                    elif line == 9:  # tabs: 5
                        if column == 0:  # tabs: 6
                            field[8][0], field[8][1], field[9][1] = '~', '~', '~'  # tabs: 7
                        elif column == 9:  # tabs: 6
                            field[8][8], field[8][9], field[9][8] = '~', '~', '~'  # tabs: 7
                        else:  # tabs: 6
                            field[line - 1][8], field[line][8], field[line + 1][8], field[line - 1][9], field[line + 1][9] = '~', '~', '~', '~', '~'  # tabs: 7
                    else:  # tabs: 5
                        if column == 0:  # tabs: 6
                            for col in range(column, column + length):  # tabs: 7
                                if col > 8:  # tabs: 8
                                    break  # tabs: 9
                                field[line - 1][col], field[line + 1][col] = '~', '~'  # tabs: 8
                            if column + length < 10:  # tabs: 7
                                field[line - 1][column + length], field[line][column + length], field[line + 1][column + length] = '~', '~', '~'  # tabs: 8
                        elif column == 9:  # tabs: 6
                            field[8][column - 1], field[9][column - 1] = '~', '~'  # tabs: 7
                            for i in range(length):  # tabs: 7
                                if column + i > 9:  # tabs: 8
                                    break  # tabs: 9
                                field[8][column + i] = '~'  # tabs: 8
                            if column + length < 10:  # tabs: 7
                                field[8][column + length], field[9][column + length] = '~', '~'  # tabs: 8
                        else:  # tabs: 6
                            field[line - 1][column - 1], field[line][column - 1], field[line + 1][column - 1] = '~', '~', '~'  # tabs: 7
                            for i in range(length):  # tabs: 7
                                if column + i > 9:  # tabs: 8
                                    break  # tabs: 9
                                field[line - 1][column + i], field[line + 1][column + i] = '~', '~'  # tabs: 8
                            if column + length < 10:  # tabs: 7
                                field[line - 1][column + length], field[line][column + length], field[line + 1][column + length] = '~', '~', '~'  # tabs: 8
            else:  # tabs: 3
                print('smth went wrong when it was in move definition (Sea Battle -> __handle_exploding() -> __separate())')  # tabs: 4
                system('pause')  # tabs: 4

            return field  # tabs: 3

        exploed_result = __exploded(self.__player1, move) if self.__queue == 'rl' else __exploded(self.__player2, move)  # tabs: 2
        if self.__queue == 'rl':  # tabs: 2
            self.__player1 = __separate(self.__player1, exploed_result)  # tabs: 3
            self.field1 = [[e for e in ''.join(line).replace('#', ' ')] for line in self.__player1]  # tabs: 3
        else:  # tabs: 2
            self.__player2 = __separate(self.__player2, exploed_result)  # tabs: 3
            self.field2 = [[e for e in ''.join(line).replace('#', ' ')] for line in self.__player2]  # tabs: 3


def main() -> None:  # tabs: 0
    system('cls')  # tabs: 1
    choose = input('Choose the game:\n1: XO\n2: Sea battle\n\nYour choose: ').strip(' ')  # tabs: 1
    while not (choose in [1, 2] or choose in ['1', '2']):  # tabs: 1
        system('cls')  # tabs: 2
        try: choose = int(input('\'1\' to play XO\n\'2\' to play Sea battle\n\nYour choose: '))  # tabs: 2
        except ValueError: system('cls')  # tabs: 2
    choose = int(choose)  # tabs: 1
    system('cls')  # tabs: 1
    if choose == 1:  # tabs: 1
        session = XO(input('Enter User\'s names (2 words): ').split())  # tabs: 2
        session.run()  # tabs: 2
    else:  # tabs: 1
        session = SeaBattle(input('Enter User\'s names (2 words): ').split())  # tabs: 2
        session.run()  # tabs: 2


if __name__ == '__main__':  # tabs: 0
    main()  # tabs: 1

"""  # tabs: 0

    .==================================================.  # tabs: 1
    ||   .=====.      .=.  .====.   .====.  .=====.   ||  # tabs: 2
    ||   *   //      //||  ||   \\    ||   ||    ||   ||  # tabs: 4
    ||      //      //_||  ||___//    ||   ||         ||  # tabs: 6
    ||     //      //``||  ||```\\    ||   || .===.   ||  # tabs: 4
    ||    //   .  //   ||  ||    ||   ||   ||    ||   ||  # tabs: 4
    ||   *=====* *=*  *=*  *=====*  *====*  *====*    ||  # tabs: 2
    '=================================================='  # tabs: 1

"""  # tabs: 0

# horizontal: deleting left part when exploding  # tabs: 0
# vertical:   exploding where damaged bottom or under top of a ship  # tabs: 0