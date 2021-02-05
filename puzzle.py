'''
# https://github.com/archy-co/lab1_task2
'''


def validate_board(board: list) -> bool:
    '''
    Validates the board by all criterias and returns returns result: True is board
    is ready to play and False otherwise (at least one criteria does not apply)
    >>> board = [\
        "**** ****",\
        "***1 ****",\
        "**  3****",\
        "* 4 1****",\
        "     9 5 ",\
        " 6  83  *",\
        "3   1  **",\
        "  8  2***",\
        "  2  ****"\
    ]
    >>> validate_board(board)
    False
    '''
    return check_rowwise(board) and check_rowwise(transpose_rc(board)) and check_block(board)

def check_rowwise(board: list) -> bool:
    '''
    Takes board as input, iterates through each column and checks whethere there are
    repetitive numbers in row. If yes returns False; otherwise returns True
    >>> check_rowwise(['1241'])
    False
    >>> check_rowwise(['9385'])
    True
    '''
    for row in board:
        deja_vu = []
        for cell in row:
            try:
                if int(cell) in deja_vu:
                    return False
                deja_vu.append(int(cell))
            except ValueError:
                continue

    return True


def transpose_rc(board: list) -> list:
    '''
    Switches rows and columns

    (the same implementation of the function as in skyscrapers module)
    >>> transpose_rc(['***21**', '412453*', '423145*', '*543215', '*35214*',\
                             '*41532*', '*2*1***'])
    ['*44****', '*125342', '*23451*', '2413251', '154213*', '*35142*', '***5***']
    '''
    n_board = []
    board_dict = dict()
    for row in board:
        for i in range(len(row)):
            board_dict[i] = board_dict.get(i, '')+row[i]

    for value in board_dict.values():
        n_board.append(value)

    return n_board

def check_block(board):
    '''
    Checks by the blocks of the same color
    '''
    pass

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    board = [\
        "**** ****",\
        "***1 ****",\
        "**  3****",\
        "* 4 1****",\
        "     9 5 ",\
        " 6  83  *",\
        "3   1  **",\
        "  8  2***",\
        "  2  ****"\
    ]

    print(check_rowwise(board))
