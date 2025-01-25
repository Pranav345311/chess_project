import pygame as p
from pygame import Color
from Chess import ChessEngine

WIDTH = HEIGHT = 512
DIMENSION = 8  # dimensions of a chess board are 8x8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 30
IMAGES = {}

'''
Initialize a global dictionary of images, This will be called exactly once in the main
'''
def load_images():
    pieces = ['wp', 'wR', 'wB', 'wK', 'wQ', 'wN', 'bp', 'bR', 'bB', 'bK', 'bQ', 'bN']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))
    # Note: we can access an image by saying 'IMAGES'['wp']

'''
The main driver for our code. This will handle user input and updating the graphics
'''
def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    load_images()  # only do this once, before the while loop
    running = True
    while running:
        for event in p.event.get():
            if event.type == p.QUIT:
                running = False

        drawGameState(screen, gs)  # Call the function to draw the game state
        clock.tick(MAX_FPS)
        p.display.flip()


'''
Responsible for all the graphics within the current game state,
'''
def drawGameState(screen, gs):
    drawBoard(screen)  # Draws squares on the board
    # Add in piece highlighting or move suggestions (later)
    drawPieces(screen, gs.board)  # Draw pieces on the top of those squares


'''
Draw the squares on the board. The top left square is always light.
'''
def drawBoard(screen):
    colors = [p.Color("white"), p.Color("grey")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[(r + c) % 2]  # Correct the indexing
            p.draw.rect(screen, color, p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))  # Fix width and height


'''
Draw the pieces on the board using the current GameState.board
'''
def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--":  # not empty square
                screen.blit(IMAGES[piece], (c * SQ_SIZE, r * SQ_SIZE))  # Swap r and c to fix positioning


if __name__ == "__main__":  # Correct the __main__ check
    main()























