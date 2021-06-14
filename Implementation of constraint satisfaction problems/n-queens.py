import itertools

def rempos(board, size):   
    takenr = frozenset(x for x, y in board)
    freer = (x for x in range(size) if x not in takenr)
    takenc = frozenset(y for x, y in board)
    freec = (y for y in range(size) if y not in takenc)
    
    freerc = itertools.product(freer, freec)
    taken_first_diagonals = frozenset(x + y for x, y in board)
    taken_second_diagonals = frozenset(x - y for x, y in board)
    return (
        (x, y) for x, y in freerc
        if x + y not in taken_first_diagonals
        and x - y not in taken_second_diagonals
    )
def ordrem(board, size):
    if board:
        max_x = max(x for x, y in board)
    else:
        max_x = -1
    return (
        (x, y) for x, y in rempos(board, size)
        if x > max_x
    )

def nqueens(size, board=None):
    board = board or frozenset()
    if len(board) == size:
        yield board
    for position in ordrem(board, size):
        new_board = board.union((position,))
        yield from nqueens(size, new_board)

def printb(board):
    size = len(board)
    for row in range(size):
        cells = (
            "Q " if (row, col) in board else "_ "
            for col in range(size)
        )
        print("".join(cells))
    print("               ")

if __name__ == "__main__":
    size = int(input("Please enter the no. of queens: "))
    print("The size of board will be: ",size)
    print("**************************************")
    print("Constraints placed: On the board of size",size,",",size,"queens must be placed in such a way that no 2 queens co-incide horizantally, vertically, or diagonally")
    print("\n\n")
    print("The solutions are as follows: ")
    solution_count = 0
    for solution in nqueens(size):
        solution_count += 1
        printb(solution)
        print("**" * size)
    print("{count} solutions".format(count=solution_count))
