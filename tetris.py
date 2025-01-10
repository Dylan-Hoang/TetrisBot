import pygame
import sys
import random
inttoletter = {1:"I",2:"O",3:"T",4:"S",5:"Z",6:"J",7:"L"}

class Tetromino:
    SHAPES = {
        "I": [[1, 1, 1, 1]],
        "O": [[1, 1], [1, 1]],
        "T": [[0, 1, 0], [1, 1, 1]],
        "S": [[0, 1, 1], [1, 1, 0]],
        "Z": [[1, 1, 0], [0, 1, 1]],
        "J": [[1, 0, 0], [1, 1, 1]],
        "L": [[0, 0, 1], [1, 1, 1]],
    }
    COLOR =  {
        "I": (0,255,255),
        "O": (255,255,0),
        "T": (128,0,128),
        "S": (0,255,0),
        "Z": (255,0,0),
        "J": (0,0,255),
        "L": (255,165,0),
    }

    def __init__(self, shape):
        self.shape = Tetromino.SHAPES[shape]
        self.color = Tetromino.COLOR[shape]
        self.x = 4
        self.y = 0
        self.name = shape

class Board:
    def __init__(self):
        self.box = [["Empty" for _ in range(10)] for _ in range(20)]

    def draw(self, screen, tetromino):
        """Draw the board and the current Tetromino on the screen."""
        screen.fill((0, 0, 0))  # Clear screen

        # Draw the board
        for row in range(len(self.box)):
            for col in range(len(self.box[row])):
                color = (255, 255, 255) if self.box[row][col] == "Empty" else tetromino.COLOR[self.box[row][col]]
                pygame.draw.rect(
                    screen,
                    color,
                    pygame.Rect(col * 30, row * 30, 30, 30),
                )

        # Draw the Tetromino
        for row in range(len(tetromino.shape)):
            for col in range(len(tetromino.shape[row])):
                if tetromino.shape[row][col] == 1:
                    temp_x = tetromino.x + col
                    temp_y = tetromino.y + row
                    if 0 <= temp_y < len(self.box) and 0 <= temp_x < len(self.box[0]):
                        pygame.draw.rect(
                            screen,
                            tetromino.color,
                            pygame.Rect(temp_x * 30, temp_y * 30, 30, 30),
                        )

        # Draw gridlines
        for x in range(0, 300, 30):
            pygame.draw.line(screen, (50, 50, 50), (x, 0), (x, 600))
        for y in range(0, 600, 30):
            pygame.draw.line(screen, (50, 50, 50), (0, y), (300, y))

        pygame.display.flip()


def move_tetromino(board, tetromino, direction):
    """Move the Tetromino left, right, or down."""
    if direction == "l" and tetromino.x > 0:
        tetromino.x -= 1
    elif direction == "r" and tetromino.x + len(tetromino.shape[0]) < len(board.box[0]):
        tetromino.x += 1
    elif direction == "d" and tetromino.y + len(tetromino.shape) < len(board.box):
        tetromino.y += 1

def place_piece(board, tetromino):
    """Add Tetromino to the board."""
    for row in range(len(tetromino.shape)):
        for col in range(len(tetromino.shape[row])):
            if tetromino.shape[row][col] == 1:
                board.box[tetromino.y + row][tetromino.x + col] = tetromino.name

def main():
    pygame.init()

    # Screen settings
    screen = pygame.display.set_mode((300, 600))
    pygame.display.set_caption("Tetris")

    clock = pygame.time.Clock()

    newboard = Board()
    current_piece = Tetromino("T")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Display the board
        newboard.draw(screen, current_piece)

        # Get user input
        print("Move Tetromino: (left/right/down/quit)")
        command = input().strip().lower()

        if command == "quit":
            break
        elif command == "l":
            move_tetromino(newboard, current_piece, "l")
        elif command == "r":
            move_tetromino(newboard, current_piece, "r")
        elif command == "d":
            move_tetromino(newboard, current_piece, "d")

        # Check if the Tetromino has reached the bottom
        if current_piece.y + len(current_piece.shape) >= len(newboard.box):
            place_piece(newboard, current_piece)
            randomnum = random.randint(1,7)
            current_piece = Tetromino(inttoletter[randomnum])

        clock.tick(10)  # Control frame rate

if __name__ == "__main__":
    main()
