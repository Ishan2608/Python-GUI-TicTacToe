import tkinter as tk
import random
# --------------------------------------------------------------------------
# GAME LOGIC
# --------------------------------------------------------------------------

# CREATING CONSTANTS AND VARIABLES
MARK1 = 'O'
MARK2 = 'X'

# global variables
current_mark = ''
player1 = ''
player2 = ''
current_player_identifier = 0
# winning conditions
wins = [
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],
    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],
    [(0, 0), (1, 1), (2, 2)],
    [(0, 2), (1, 1), (2, 0)]
]
# places to mark. If it is false, user can place his mark else not
check_table = [[False, False, False],
                [False, False, False],
                [False, False, False]]
# variable to stop users form placing their marks
game_over = False

# DEFINING FUNCTIONS


def set_initials(name1, name2):
    global current_mark, player1, player2, current_player_identifier
    player1 = name1
    player2 = name2
    current_player_identifier = 0
    current_mark = change_turn()


def change_turn():
    global current_player_identifier, player1, player2
    if current_player_identifier % 2 == 0:
        current_player = player1
        mark = MARK1
    else:
        current_player = player2
        mark = MARK2

    turn.config(text=f"{current_player}'s Turn: {mark}")
    current_player_identifier += 1

    return mark


def place_mark(event):
    global current_mark, game_over
    if not game_over:
        row = event.widget.grid_info()['row']
        col = event.widget.grid_info()['column']
        r = rows[row]
        c = cols[col]
        if not check_table[r][c]:
            check_table[r][c] = current_mark
            event.widget.config(text=f"{current_mark}", fg="black")
            status.config(text="Status: OK")
            current_mark = change_turn()
            win = check_win()
            if win == 2:
                display_winner(player2)
                game_over = True
            elif win == 1:
                display_winner(player1)
                game_over = True
            elif win == 0 and ((False not in check_table[0]) and (False not in check_table[1]) and (False not in check_table[2])):
                status.config(text="Draw")
                game_over = True
            else:
                return
        else:
            status.config(text="Status: Wrong Move")
            return
    else:
        status.config(text="Game Over!!", fg='crimson')


def check_win():
    global wins, player1, player2, winner
    for row in wins:
        elem1 = row[0]
        elem2 = row[1]
        elem3 = row[2]
        if (check_table[elem1[0]][elem1[1]] == "X") and (check_table[elem2[0]][elem2[1]] == "X") and (check_table[elem3[0]][elem3[1]] == "X"):
            return 2
        elif (check_table[elem1[0]][elem1[1]] == "O") and (check_table[elem2[0]][elem2[1]] == "O") and (check_table[elem3[0]][elem3[1]] == "O"):
            return 1
    return 0


def display_winner(winner):
    status.config(text=f"{winner} Won!!", fg='green')


def create_input_placeholder():
    name1.insert(0, 'Enter Name of Player 1')
    name2.insert(0, 'Enter Name of Player 2')


def remove_input_placeholder(event):
    event.widget.delete(0, tk.END)


def destroy_welcome():
    # extract entry values
    val1 = name1.get()
    val2 = name2.get()

    # remove the form widgets
    name1.destroy()
    name2.destroy()
    begin_btn.destroy()

    # Start the game
    display_game_board(val1, val2)
    set_initials(val1, val2)


def display_game_board(val1, val2):
    player1_name_display.config(text=f"Player1({MARK1}): {val1}")
    player2_name_display.config(text=f"Player2({MARK2}): {val2}")

    # Placing the Widgets
    heading.grid(row=0, column=0, sticky="w")
    player1_name_display.grid(row=1, column=0, sticky="w")
    player2_name_display.grid(row=2, column=0, sticky="w")
    turn.grid(row=3, column=0, sticky="w")
    status.grid(row=4, column=0, sticky="w")

    top_left.grid(row=0, column=1, rowspan=2, columnspan=2, sticky='nesw')
    middle_left.grid(row=2, column=1, rowspan=2, columnspan=2, sticky='nesw')
    bottom_left.grid(row=4, column=1, rowspan=2, columnspan=2, sticky='nesw')

    top_middle.grid(row=0, column=3, rowspan=2, columnspan=2, sticky='nesw')
    middle_middle.grid(row=2, column=3, rowspan=2, columnspan=2, sticky='nesw')
    bottom_middle.grid(row=4, column=3, rowspan=2, columnspan=2, sticky='nesw')

    top_right.grid(row=0, column=5, rowspan=2, columnspan=2, sticky='nesw')
    middle_right.grid(row=2, column=5, rowspan=2, columnspan=2, sticky='nesw')
    bottom_right.grid(row=4, column=5, rowspan=2, columnspan=2, sticky='nesw')


# --------------------------------------------------------------------------
# GAME User Interface
# --------------------------------------------------------------------------

# UI VARIABLES AND CONSTANTS
# fonts
BODY = ("Arial", 16, "normal")
HEAD = ("Courier", 20, "bold")
GIANT = ("Arial", 50, "bold")

# placeholders in Game Grid
PLACEHOLDER = "↓"
PLACEHOLDER2 = "?"
FG = "#bfc1c1"

# The rows and columns of the grid and their corresponding rows and columns in a matrix
rows = {0: 0, 2: 1, 4: 2}
cols = {1: 0, 3: 1, 5: 2}

# CREATE WIDGETS
# create the window
window = tk.Tk()
window.title("Welcome to Tic Tac Toe")
window.geometry("640x427")

# Set a background randomly
bg_image_1 = tk.PhotoImage(file="bg.png")
bg_image_2 = tk.PhotoImage(file="bg-2.png")
bg = [0, 1]
choice = random.choice(bg)
canvas = tk.Canvas(width=640, height=427)
if choice == 0:
    canvas.create_image(0, 0, image=bg_image_1, anchor="nw")
else:
    canvas.create_image(0, 0, image=bg_image_2, anchor="nw")

# Create A Form
name1 = tk.Entry(width=30, font=BODY)
name2 = tk.Entry(width=30, font=BODY)
begin_btn = tk.Button(text="Begin", font=BODY, command=destroy_welcome)
create_input_placeholder()

# remove placeholder when user clicks inside the entry
name1.bind('<FocusIn>', remove_input_placeholder)
name2.bind('<FocusIn>', remove_input_placeholder)

# Place the form
canvas.grid(row=0, column=0, rowspan=6, columnspan=7)
name1.grid(row=2, column=2, columnspan=3, sticky='ew')
name2.grid(row=3, column=2, columnspan=3, sticky='ew')
begin_btn.grid(row=4, column=2, columnspan=3, sticky='ew')

# Create the Game Board Widgets

# Left Menu
# heading
heading = tk.Label(text="Tic Tac Toe", font=HEAD)
# player names
player1_name_display = tk.Label(text=f"Player1: ", font=BODY)
player2_name_display = tk.Label(text=f"Player2: ", font=BODY)
# winner name
winner = tk.Label(text=f"Player Wins", font=BODY)
# show whose turn it is right now
turn = tk.Label(text="Player1's Turn", font=BODY)
# show status of the move or the game
status = tk.Label(text="Status: ", font=BODY)

# main game grid

# top row
top_left = tk.Button(text=PLACEHOLDER2, font=GIANT, fg=FG)
top_left.bind("<Button-1>", place_mark)
top_middle = tk.Button(text=PLACEHOLDER2, font=GIANT, fg=FG)
top_middle.bind("<Button-1>", place_mark)
top_right = tk.Button(text=PLACEHOLDER2, font=GIANT, fg=FG)
top_right.bind("<Button-1>", place_mark)

# middle row
middle_left = tk.Button(text=PLACEHOLDER2, font=GIANT, fg=FG)
middle_left.bind("<Button-1>", place_mark)
middle_middle = tk.Button(text=PLACEHOLDER2, font=GIANT, fg=FG)
middle_middle.bind("<Button-1>", place_mark)
middle_right = tk.Button(text=PLACEHOLDER2, font=GIANT, fg=FG)
middle_right.bind("<Button-1>", place_mark)

# bottom row
bottom_left = tk.Button(text=PLACEHOLDER2, font=GIANT, fg=FG)
bottom_left.bind("<Button-1>", place_mark)
bottom_middle = tk.Button(text=PLACEHOLDER2, font=GIANT, fg=FG)
bottom_middle.bind("<Button-1>", place_mark)
bottom_right = tk.Button(text=PLACEHOLDER2, font=GIANT, fg=FG)
bottom_right.bind("<Button-1>", place_mark)

# keep the window open until the user closes it himself
window.mainloop()
