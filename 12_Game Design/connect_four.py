grid = [
    ["-",  "-",  "-",  "-",  "-",  "-",  "-" ],     # [R0C0, R0C1, R0C2]
    ["-",  "-",  "-",  "-",  "-",  "-",  "-" ],     # [R0C0, R0C1, R0C2]
    ["-",  "-",  "-",  "-",  "-",  "-",  "-" ],     # [R0C0, R0C1, R0C2]
    ["-",  "-",  "-",  "-",  "-",  "-",  "-" ],     # [R0C0, R0C1, R0C2]
    ["-",  "-",  "-",  "-",  "-",  "-",  "-" ],     # [R0C0, R0C1, R0C2]
    ["-",  "-",  "-",  "-",  "-",  "-",  "-" ],     # [R0C0, R0C1, R0C2]
    ["-",  "-",  "-",  "-",  "-",  "-",  "-" ],     # [R0C0, R0C1, R0C2]
]

current_piece = "R"

last_row = -1
last_col = -1
remaining_spots = 42

def print_grid():
    for i in range(7):
        print(i, end="  ")
     
    print()

    for row in range(6):
        for col in range(7):
            if col != 6:
                print(grid[row][col], end="  ")            
            else:
                print(grid[row][col])
                print()

def is_bad_num_string(choice : str):
    if (choice.isnumeric() and int(choice) >= 0 and int(choice) <= 6):
        return False
    return True
                
def is_bad_choice(choice : str):
    if(choice.__eq__("STOP")):
        return False
    return is_bad_num_string(choice)

def place_piece(col : int):
    global last_row
    global last_col
    global remaining_spots
    while(True):
        row = 5
        while(row >= 0):
            if grid[row][col].__eq__("-"):
                grid[row][col] = current_piece
                last_row = row
                last_col = col
                remaining_spots -=1
                break
            else:
                 row -= 1
        if row != -1:
            break
        else:
            user_choice = ""
            while (is_bad_num_string(user_choice)):
                user_choice = input("Enter a different number (0-6) where to drop the piece: ")
                col = int(user_choice)

def check_row():
    for row in range(3):
        if grid[row][0].__eq__(grid[row][1]) and grid[row][1].__eq__(grid[row][2]):
            return True
    return False
 
def check_col():
    for col in range(3):
        if grid[0][col].__eq__(grid[1][col]) and grid[1][col].__eq__(grid[2][col]):
            return True
    return False

def check_left_diag():
    return grid[0][0].__eq__(grid[1][1]) and grid[1][1].__eq__(grid[2][2])

def check_right_diag():
    return grid[0][2].__eq__(grid[1][1]) and grid[1][1].__eq__(grid[2][0])

def check_draw():
    return remaining_spots == 0

def check_game_over():
    if check_row():
        print(current_piece + " wins!")
        return True
    elif check_col():
        print(current_piece + " wins!")
        return True
    elif check_left_diag():
        print(current_piece + " wins!")
        return True
    elif check_right_diag():
        print(current_piece + " wins!")
        return True
    elif check_draw():
        print("The Game Ends in a Draw!")
        return True
    else:
        return False

def game_loop():
    global current_piece
    print("Welcome to CONNECT FOUR")
    user_choice = ""
    while(True):
        print_grid()
        while(is_bad_choice(user_choice)):
            user_choice = input("Enter STOP to end.  Or a number (0-6) where to drop the piece: ")
        if user_choice.__eq__("STOP"):
            break
        column = int(user_choice)
        place_piece(column)
       #if(check_game_over()):
       #    print_grid()
       #    break
        current_piece = "Y" if current_piece.__eq__("R") else "R"
        user_choice = ""
    print("GAME OVER")
        
game_loop()