player_one_symbol = "X"
player_two_symbol = "O"

grid = [["|___|","|___|","|___|"],
            ["|___|","|___|","|___|"],
            ["|___|","|___|","|___|"]]

def show_board(): #pretty print board
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in grid]))

def start_game():
    print("Welcome to Tic-Tac-Toe!")
    show_board()
    print()
    player_one = input("Player one enter your name: ")
    print(f"Hello {player_one}! You will be X")
    print()
    player_two = input("Player two enter your name: ")
    while 1:
        if player_two != player_one:
            break
        else: 
            print("Player name must be different from first player")
            player_two = input("Player two enter your name: ")

    print(f"Hello {player_two}! You will be O")
    print()
    return player_one, player_two

def game_board(row, column, value):
    grid[row][column] = f"| {value} |"
    show_board()
    print()

def play_logic():
    count = 0
    while 1:
        row, column, value = player_one_prompt()
        if grid[row][column] == "|___|":
            game_board(row, column, value)
            if check_winner(row, column, value, count):
                print(f"{player_one} you win!")
                break
        else:
            print("Spot has already been selected. Try again")
            continue
        row, column, value = player_two_prompt()
        if grid[row][column] == "|___|":
            game_board(row, column, value)
            if check_winner(row, column, value, count):
                print(f"{player_two} you win!")
                break
        else:
            while 1:
                print("Spot has already been selected. Try again")
                row, column, value = player_two_prompt()
                if grid[row][column] == "|___|":
                    game_board(row, column, value)
                    break
                else:
                    game_board(row, column, value)
            if check_winner(row, column, value, count):
                print(f"{player_two} you win!")
                break
        count += 1

def check_winner(row, column, value, count):
    if grid[0][column] == f"| {value} |" and grid[1][column] == f"| {value} |" and grid[2][column] == f"| {value} |": #check vertical 
        return True
    if grid[row][0] == f"| {value} |" and grid[row][1] == f"| {value} |" and grid[row][2] == f"| {value} |": #check horizontal 
        return True
    if row == column and grid[0][0] == f"| {value} |" and grid[1][1] == f"| {value} |" and grid[2][2] == f"| {value} |": #check diagonal
        return True
    if row + column == 2 and grid[0][2] == f"| {value} |" and grid[1][1] == f"| {value} |" and grid[2][0] == f"| {value} |": #check second diagonal
        return True
    else:
        False


def player_one_prompt():
    row = input(f"{player_one} ({player_one_symbol}) make your move! Type the row (between 0 and 2): ")
    column = input(f"{player_one} ({player_one_symbol}) Type the column (between 0 and 2): ")
    print()
    return int(row), int(column), player_one_symbol

def player_two_prompt():
    row = input(f"{player_two} ({player_two_symbol}) make your move! Type the row (between 0 and 2): ")
    column = input(f"{player_two} ({player_two_symbol}) Type the column (between 0 and 2): ")
    print()
    return int(row), int(column), player_two_symbol

if __name__ == "__main__":
    player_one, player_two = start_game()
    play_logic()

