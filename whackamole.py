import pygame
import random

screen = pygame.display.set_mode((640, 512))
mole_image = pygame.image.load("mole.png")

def main():
    #variable initialization
    x_rows = 20
    y_rows = 16
    box_dim = 32
    mole_row = 0
    mole_col = 0
    try:
        pygame.init()
        clock = pygame.time.Clock()
        running = True
        while running:
            #filling board
            screen.fill("light green")
            for i in range(1, x_rows):
                pygame.draw.line(screen, (0, 0, 0), (i * box_dim, 0), (i * box_dim, 512))
            for j in range(1, y_rows):
                pygame.draw.line(screen, (0, 0, 0), (0, j * box_dim), (640, j * box_dim))
            #mole display
            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_row*box_dim, mole_col*box_dim)))
            pygame.display.flip()
            #event conditions
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    row = x // box_dim
                    col = y // box_dim
                    if row == mole_row and col == mole_col:
                        mole_row = random.randrange(0, x_rows)
                        mole_col = random.randrange(0, y_rows)
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
