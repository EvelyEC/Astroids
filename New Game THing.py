#pygame setup here
import pygame
from pygame.locals import *
from Ship import Ship
pygame.init()
screen_info = pygame.display.Info()
size = (width, height) = (int(screen_info.current_w),int(screen_info.current_h))
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (50, 100, 100)

LevelData = df.iloc[Level]
Player = Ship (((LevelData['PlayerX'], LevelData['PlayerY'])))

def main():
    while True:
        global color
        clock.tick(60)
        screen.fill(color)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit();
                sys.exit()
                main = False
#
if __name__ == "__main__":
    main()