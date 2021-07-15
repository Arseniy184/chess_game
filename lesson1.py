#! -*- coding: utf-8 -*-


class Color(object):
    EMPTY = 0
    BLACK = 1
    WHITE = 2


class Empty(object):
    color = Color.EMPTY

    def get_moves(self, board, x, y):
        raise Exception('Error !')

    def __str__(self):
        return '  '


class ChessMan(object):
    IMG = None

    def __init__(self, color):
        self.color = color

    def __str__(self):
        return self.IMG[0 if self.color == Color.WHITE else 1]


class Pawn(ChessMan):
    IMG = ('♙', '♟')

    def get_moves(self, board, x, y):
        moves = []
        if self.color == Color.BLACK and y < 7 and board.get_color(x+1, y) == Color.EMPTY:
            moves.append([x+1, y])
        return moves


class King(ChessMan):
    IMG = ('♔', '♚')

    def get_moves(self, x, y):
        moves = []
        return moves


# noinspection PyTypeChecker
class Board(object):
    def __init__(self):
        self.board = [[Empty()] * 8 for y in range(8)]
        self.board[1][2] = Pawn(Color.BLACK)
        self.board[0][3] = King(Color.BLACK)
        self.board[7][3] = King(Color.WHITE)

    def get_color(self, x, y):
        return self.board[y][x].color

    def get_moves(self, x, y):
        return self.board[x][y].get_moves(self, x, y)

    def move(self, xy_from, xy_to):
        self.board[xy_to[0]][xy_to[1]] = self.board[xy_from[0]][xy_from[1]]
        self.board[xy_from[0]][xy_from[1]] = Empty()

    def __str__(self):
        colors = [0, 46]
        res = ''
        i = 0
        for x in range(8):
            for y in range(8):
                res += set_color(colors[i]) + str(self.board[x][y]) + '  '
                i = 1 - i
            i = 1 - i
            res += set_color(0) + '\n'
        return res


def set_color(color):
    return '\033[%sm' % color


b = Board()
print(b)
m = b.get_moves(1, 2)
print(m)
b.move([1, 2], m[0])
print(b)
