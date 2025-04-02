import requests

def main():
    name = "https://sudoku-api.vercel.app/api/dosuku" # read from sodoku api

    request = requests.get(name)    # request the api

    if request.status_code != 200:  # if api doesnt load print error
        print(f"Error: {request.status_code}")
        return

    data = request.json() # get the data of the sodoku

    original_board = data['newboard']['grids'][0]['value'] # the original board
    solution = data['newboard']['grids'][0]['solution'] # the solution to the board

    print("Original Board:")
    print_board(original_board) # print this original board

    board = [row[:] for row in original_board]

    if backtracking(board):
        print("\nSolved Board using Backtracking:")
        print_board(board)
    else:
        print("No solution found.")

    print("\nActual Solution from API:")
    print_board(solution)

def print_board(board):
    for r in range(9):
        line = ""
        for c in range(9):
            if board[r][c] != 0:
                line += str(board[r][c])
            else:
                line += " "
            if (c+1) % 3 == 0 and (c+1) != 9:
                line += ' |'
            line += " "
        print(line)
        if (r+1) % 3 == 0 and (r+1) != 9:
            print("------|-------|------")



def backtracking(board):
    empty = find_empty(board)
    if not empty:
        return True
    
    row, col = empty

    for num in range(1, 10):  
        if checkAll(board, num, row, col):
            board[row][col] = num

            if backtracking(board):
                return True

            board[row][col] = 0

    return False

def find_empty(board):
    """Finds the first empty cell (0) and returns its (row, col) position."""
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                return r, c
    return None

def checkAll(board, num, r, c):
    return checkSquare(board, r, c) and checkRow(board, num, r, c) and checkCol(board, num, r, c)

def checkSquare(board, r, c):
    hashSet = set()
    for row in range((r//3) * 3, ((r//3) * 3)+ 3):
        for column in range((c//3) * 3,((c//3) * 3) + 3):
            if board[row][column] in hashSet:
                # print("SQUARE FALSE", (r//3), c//3)
                return False
            if board[row][column] != 0:
                # print("ADDING: ", board[row][column])
                hashSet.add(board[row][column])
    return True
      
def checkRow(board, num, r, c):
    index = 0
    for i in board[r]:
        if index != c and num == i and num != 0:
            # print("ROW FALSE: ", num, board[r])
            return False
        index += 1
    return True
    #     if num != 0 and i != c:


    # if num in board[r] and num != 0:
    #     print("ROW FALSE", board[r][c], board[r])
    #     return False
    # return True


def checkCol(board, num, r, c):
    index = 0
    for i in [board[r][c] for r in range(9)]:
        if index != r and num == i and num != 0:
            # print("COL FALSE: ", num, board[r])
            return False
        index += 1
    return True

    # if num in [board[r][c] for r in range(9)] and num != 0:
    #     print("COLUMN FALSE", num, [board[r][c] for r in range(9)] )
    #     return False
    # return True


if __name__ == "__main__":
    main()