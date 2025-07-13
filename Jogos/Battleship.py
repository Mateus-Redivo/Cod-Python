import random
import os
import time

# Game constants
BOARD_SIZE = 10
EMPTY = " "
SHIP = "S"
HIT = "X"
MISS = "O"
HIDDEN = "~"

# Ship types with their sizes
SHIPS = {
    "Carrier": 5,
    "Battleship": 4,
    "Cruiser": 3,
    "Submarine": 3,
    "Destroyer": 2
}


def clear_screen():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def initialize_board(size):
    """Create an empty board of given size."""
    return [[EMPTY for _ in range(size)] for _ in range(size)]


def print_board(board, hide_ships=False):
    """Display the game board."""
    print("  " + " ".join(str(i) for i in range(BOARD_SIZE)))
    for i in range(BOARD_SIZE):
        row = [str(i)]
        for j in range(BOARD_SIZE):
            cell = board[i][j]
            if hide_ships and cell == SHIP:
                row.append(HIDDEN)
            else:
                row.append(cell)
        print(" ".join(row))


def place_ship(board, ship_size, ship_name):
    """Place a ship of given size on the board randomly."""
    while True:
        # Choose random orientation (0: horizontal, 1: vertical)
        orientation = random.randint(0, 1)

        # Choose random starting position
        if orientation == 0:  # Horizontal
            row = random.randint(0, BOARD_SIZE - 1)
            col = random.randint(0, BOARD_SIZE - ship_size)
        else:  # Vertical
            row = random.randint(0, BOARD_SIZE - ship_size)
            col = random.randint(0, BOARD_SIZE - 1)

        # Check if placement is valid
        valid = True
        for i in range(ship_size):
            r = row + (i if orientation == 1 else 0)
            c = col + (i if orientation == 0 else 0)
            if board[r][c] != EMPTY:
                valid = False
                break

        # If valid, place ship and return
        if valid:
            for i in range(ship_size):
                r = row + (i if orientation == 1 else 0)
                c = col + (i if orientation == 0 else 0)
                board[r][c] = SHIP
            return True


def place_player_ship(board, ship_size, ship_name):
    """Allow player to place a ship on the board."""
    print(f"\nPlacing {ship_name} (size: {ship_size})")
    print_board(board)

    while True:
        try:
            orientation = input(
                "Choose orientation (h for horizontal, v for vertical): ").lower()
            if orientation not in ['h', 'v']:
                print("Invalid orientation. Please enter 'h' or 'v'.")
                continue

            row = int(input(f"Enter row (0-{BOARD_SIZE-1}): "))
            col = int(input(f"Enter column (0-{BOARD_SIZE-1}): "))

            if row < 0 or row >= BOARD_SIZE or col < 0 or col >= BOARD_SIZE:
                print(
                    f"Coordinates out of bounds. Please enter values between 0 and {BOARD_SIZE-1}.")
                continue

            # Check if ship fits on board
            if orientation == 'h' and col + ship_size > BOARD_SIZE:
                print("Ship doesn't fit on the board horizontally. Try again.")
                continue
            if orientation == 'v' and row + ship_size > BOARD_SIZE:
                print("Ship doesn't fit on the board vertically. Try again.")
                continue

            # Check if placement overlaps with existing ships
            valid = True
            for i in range(ship_size):
                r = row + (i if orientation == 'v' else 0)
                c = col + (i if orientation == 'h' else 0)
                if board[r][c] != EMPTY:
                    valid = False
                    break

            if not valid:
                print("Ship overlaps with another ship. Try again.")
                continue

            # Place the ship
            for i in range(ship_size):
                r = row + (i if orientation == 'v' else 0)
                c = col + (i if orientation == 'h' else 0)
                board[r][c] = SHIP

            return True

        except ValueError:
            print("Please enter valid numbers.")


def setup_game():
    """Initialize the game boards and place ships."""
    player_board = initialize_board(BOARD_SIZE)
    computer_board = initialize_board(BOARD_SIZE)

    # Place computer ships
    for ship_name, ship_size in SHIPS.items():
        place_ship(computer_board, ship_size, ship_name)

    # Place player ships
    print("Set up your board:")
    for ship_name, ship_size in SHIPS.items():
        place_player_ship(player_board, ship_size, ship_name)
        clear_screen()

    return player_board, computer_board


def get_player_move():
    """Get a valid move from the player."""
    while True:
        try:
            row = int(input(f"Enter target row (0-{BOARD_SIZE-1}): "))
            col = int(input(f"Enter target column (0-{BOARD_SIZE-1}): "))

            if row < 0 or row >= BOARD_SIZE or col < 0 or col >= BOARD_SIZE:
                print(
                    f"Coordinates out of bounds. Please enter values between 0 and {BOARD_SIZE-1}.")
                continue

            return row, col

        except ValueError:
            print("Please enter valid numbers.")


def computer_move(player_board, previous_moves):
    """Generate a computer move."""
    while True:
        row = random.randint(0, BOARD_SIZE - 1)
        col = random.randint(0, BOARD_SIZE - 1)

        if (row, col) not in previous_moves:
            previous_moves.add((row, col))
            return row, col


def check_game_over(board):
    """Check if all ships are sunk."""
    for row in board:
        if SHIP in row:
            return False
    return True


def play_game():
    """Main game loop."""
    player_board, computer_board = setup_game()
    computer_moves = set()
    player_moves = set()

    player_turn = True
    game_over = False

    while not game_over:
        clear_screen()

        print("Your board:")
        print_board(player_board)

        print("\nComputer's board:")
        print_board(computer_board, hide_ships=True)

        if player_turn:
            print("\nYour turn!")
            row, col = get_player_move()

            while (row, col) in player_moves:
                print("You already fired at this position. Try again.")
                row, col = get_player_move()

            player_moves.add((row, col))

            if computer_board[row][col] == SHIP:
                print("HIT!")
                computer_board[row][col] = HIT
                if check_game_over(computer_board):
                    print("Congratulations! You sank all enemy ships!")
                    game_over = True
            else:
                print("MISS!")
                computer_board[row][col] = MISS

        else:  # Computer's turn
            print("\nComputer's turn...")
            time.sleep(1)

            row, col = computer_move(player_board, computer_moves)

            if player_board[row][col] == SHIP:
                print(f"Computer hit your ship at ({row}, {col})!")
                player_board[row][col] = HIT
                if check_game_over(player_board):
                    print("Game over! The computer sank all your ships!")
                    game_over = True
            else:
                print(f"Computer missed at ({row}, {col})!")
                player_board[row][col] = MISS

        player_turn = not player_turn

        input("\nPress Enter to continue...")

    # Show final boards
    clear_screen()
    print("GAME OVER")
    print("\nYour final board:")
    print_board(player_board)

    print("\nComputer's final board:")
    print_board(computer_board)


def main():
    """Start the game."""
    clear_screen()
    print("Welcome to BATTLESHIP!")
    print("\nGame rules:")
    print("1. You and the computer will take turns firing at each other's ships.")
    print("2. First to sink all enemy ships wins.")

    while True:
        play_game()

        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again != 'y':
            break

    print("\nThanks for playing Battleship!")


if __name__ == "__main__":
    main()
