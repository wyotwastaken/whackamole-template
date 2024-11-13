import pygame
import random


def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        screen = pygame.display.set_mode((640, 512))
        mole_image = pygame.image.load("mole.png")
        mole_initial_position = [0, 0]
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.fill("light green")
            pygame.draw.line(screen, (0, 0, 0), (32, 0), (32, 640))
            pygame.draw.line(screen, (0, 0, 0), (64, 0), (64, 640))
            pygame.draw.line(screen, (0, 0, 0), (96, 0), (96, 640))
            pygame.draw.line(screen, (0, 0, 0), (128, 0), (128, 640))
            pygame.draw.line(screen, (0, 0, 0), (160, 0), (160, 640))
            pygame.draw.line(screen, (0, 0, 0), (192, 0), (192, 640))
            pygame.draw.line(screen, (0, 0, 0), (224, 0), (224, 640))
            pygame.draw.line(screen, (0, 0, 0), (256, 0), (256, 640))
            pygame.draw.line(screen, (0, 0, 0), (288, 0), (288, 640))
            pygame.draw.line(screen, (0, 0, 0), (320, 0), (320, 640))
            pygame.draw.line(screen, (0, 0, 0), (352, 0), (352, 640))
            pygame.draw.line(screen, (0, 0, 0), (384, 0), (384, 640))
            pygame.draw.line(screen, (0, 0, 0), (416, 0), (416, 640))
            pygame.draw.line(screen, (0, 0, 0), (448, 0), (448, 640))
            pygame.draw.line(screen, (0, 0, 0), (480, 0), (480, 640))
            pygame.draw.line(screen, (0, 0, 0), (512, 0), (512, 640))
            pygame.draw.line(screen, (0, 0, 0), (544, 0), (544, 640))
            pygame.draw.line(screen, (0, 0, 0), (576, 0), (576, 640))
            pygame.draw.line(screen, (0, 0, 0), (608, 0), (608, 640))
            pygame.draw.line(screen, (0, 0, 0), (0, 32), (640, 32))
            pygame.draw.line(screen, (0, 0, 0), (0, 64), (640, 64))
            pygame.draw.line(screen, (0, 0, 0), (0, 96), (640, 96))
            pygame.draw.line(screen, (0, 0, 0), (0, 128), (640, 128))
            pygame.draw.line(screen, (0, 0, 0), (0, 160), (640, 160))
            pygame.draw.line(screen, (0, 0, 0), (0, 192), (640, 192))
            pygame.draw.line(screen, (0, 0, 0), (0, 224), (640, 224))
            pygame.draw.line(screen, (0, 0, 0), (0, 256), (640, 256))
            pygame.draw.line(screen, (0, 0, 0), (0, 288), (640, 288))
            pygame.draw.line(screen, (0, 0, 0), (0, 320), (640, 320))
            pygame.draw.line(screen, (0, 0, 0), (0, 352), (640, 352))
            pygame.draw.line(screen, (0, 0, 0), (0, 384), (640, 384))
            pygame.draw.line(screen, (0, 0, 0), (0, 416), (640, 416))
            pygame.draw.line(screen, (0, 0, 0), (0, 448), (640, 448))
            pygame.draw.line(screen, (0, 0, 0), (0, 480), (640, 480))
            screen.blit(mole_image, mole_image.get_rect(topleft=(0, 0)))
            if pygame.MOUSEBUTTONDOWN:
                pass
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
