'''
Puzzle quiz game functions
https://github.com/archy-co/lab1_task2
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


def get_item_block(coord: tuple) -> int:
    '''
    Gets item (x, y) coordinates on board and return its block number
    (numeration begins from top to bottom)
    '''
    if (coord[0] >= 4 and coord[1] == 4) or (coord[0] == 4 and coord[1] <= 4):
        return 1
    if (coord[0] >= 3 and coord[1] == 5) or (coord[0] == 3 and coord[1] <= 5):
        return 2
    if (coord[0] >= 2 and coord[1] == 6) or (coord[0] == 2 and coord[1] <= 6):
        return 3
    if (coord[0] >= 1 and coord[1] == 7) or (coord[0] == 1 and coord[1] <= 7):
        return 4
    if (coord[0] >= 0 and coord[1] == 8) or (coord[0] == 0 and coord[1] <= 8):
        return 5

    return 0


def get_blocks_items(board: list) -> list:
    '''
    Finds block for each element in table. Returns tuple where key is block number,
    and value - list of items of the block
    '''
    block_items = dict()

    for i in range(len(board)):
        for j in range(len(board)):
            try:
                item = int(board[i][j])
                item_block = get_item_block(tuple([j, i]))
                block_items[item_block] = block_items.get(item_block, []) + [item]

            except ValueError:
                continue
    return block_items


def check_block(board):
    '''
    Checks by the blocks of the same color
    '''
    blocks_items = get_blocks_items(board)
    print(blocks_items)
    for items in blocks_items.values():
        items_str = ''.join(map(str, items))

        if not check_rowwise(items_str):
            return False
    return True




if __name__ == '__main__':
    import doctest
    doctest.testmod()
    t_board = [\
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

    print(check_block(t_board))
