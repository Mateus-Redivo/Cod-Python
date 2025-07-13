import numpy as np
import pygame
import sys

# Colors
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Game dimensions
ROW_COUNT = 6
COLUMN_COUNT = 7
SQUARESIZE = 100

def create_board():
    """Create an empty game board."""
    return np.zeros((ROW_COUNT, COLUMN_COUNT))

def drop_piece(board, row, col, piece):
    """Place a piece on the board."""
    board[row][col] = piece

def is_valid_location(board, col):
    """Check if a column has space for another piece."""
    return board[ROW_COUNT-1][col] == 0

def get_next_open_row(board, col):
    """Find the next available row in the given column (gravity effect)."""
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r
    return -1

def winning_move(board, piece):
    """Check if the last move was a winning move."""
    # Check horizontal
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    # Check vertical
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    # Check positively sloped diagonals
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    # Check negatively sloped diagonals
    for c in range(COLUMN_COUNT-3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True
    
    return False

def draw_board(board, screen):
    """Draw the game board with all pieces."""
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            # Draw blue rectangle for each cell
            pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
            
            # Draw the pieces
            center_x = int(c*SQUARESIZE+SQUARESIZE/2)
            center_y = int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)
            radius = int(SQUARESIZE/2 - 5)
            
            if board[r][c] == 0:
                pygame.draw.circle(screen, BLACK, (center_x, center_y), radius)
            elif board[r][c] == 1:
                pygame.draw.circle(screen, RED, (center_x, center_y), radius)
            else: 
                pygame.draw.circle(screen, YELLOW, (center_x, center_y), radius)
    
    pygame.display.update()

def main():
    # Initialize game
    board = create_board()
    game_over = False
    turn = 0
    
    # Initialize pygame
    pygame.init()
    
    # Set up the display
    width = COLUMN_COUNT * SQUARESIZE
    height = (ROW_COUNT + 1) * SQUARESIZE
    size = (width, height)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Connect Four')
    
    # Draw the initial board
    draw_board(board, screen)
    
    # Font for messages
    myfont = pygame.font.SysFont("monospace", 75)
    
    # Game loop
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
            # Show piece preview at the top when moving mouse
            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
                posx = event.pos[0]
                if turn == 0:
                    pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), int(SQUARESIZE/2 - 5))
                else:
                    pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE/2)), int(SQUARESIZE/2 - 5))
                pygame.display.update()
                
            # Handle player moves
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
                
                # Get column from mouse position
                posx = event.pos[0]
                col = int(posx // SQUARESIZE)
                
                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    piece = turn + 1
                    drop_piece(board, row, col, piece)
                    
                    # Check for win
                    if winning_move(board, piece):
                        label = myfont.render(f"Player {piece} wins!", 1, RED if piece == 1 else YELLOW)
                        screen.blit(label, (40, 10))
                        game_over = True
                    
                    # Check for draw
                    if not any(0 in row for row in board) and not game_over:
                        label = myfont.render("Draw!", 1, BLUE)
                        screen.blit(label, (40, 10))
                        game_over = True
                    
                    # Update the display
                    draw_board(board, screen)
                    
                    # Switch turns
                    turn = 1 - turn
        
        # If game over, wait before closing
        if game_over:
            pygame.time.wait(3000)
            pygame.quit()
            sys.exit()

if __name__ == "__main__":
    main()