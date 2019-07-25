#pygame setup here
import pygame
from pygame.locals import *
from Ship import Ship
from Astroids import rock
pygame.init()
screen_info = pygame.display.Info()
size = (width, height) = (int(screen_info.current_w),int(screen_info.current_h))
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (50, 100, 100)

#LevelData = df.iloc[Level]
#Player = Ship (((LevelData['PlayerX'], LevelData['PlayerY'])))
Player = Ship()
enemy = rock(0, 0)
enemy2 = rock(200, 200)


enemyGroup = pygame.sprite.Group()
enemyGroup.add(enemy)
enemyGroup.add(enemy2)


def main():
    while True:
        global color
        clock.tick(60)
        screen.fill(color)
        screen.blit(Player.image, Player.rect)
        screen.blit(enemy.image, enemy.rect)
        pygame.display.flip()

        enemyGroup.draw(screen)

        Player.update(enemyGroup)

        for en in enemyGroup:
            en.move()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit();
                sys.exit()
                main = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    Player.speed[0] = 2
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    Player.speed[0] += -2
                if event.key == pygame.K_UP or event.key == ord('w'):
                    Player.speed[1] += -2
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    Player.speed[1] += 2
                if event.key == pygame.K_SPACE:
                    Player.speed[1] += -2
                if event.key == event.key == ord('q'):
                    Player.speed[1] += -2
                    Player.speed[0] += -2
                if event.key == event.key == ord('e'):
                    Player.speed[1] += 2
                    Player.speed[0] += 2

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    Player.speed[0] = 0
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    Player.speed[0] = 0
                if event.key == pygame.K_UP or event.key == ord('w'):
                    Player.speed[1] = 0
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    Player.speed[1] = 0
                if event.key == pygame.K_SPACE:
                    Player.speed[1] += 1
                if event.key == ord('q'):
                    Player.speed[1] = 0
                    Player.speed[0] = 0
                if event.key == ord('e'):
                    Player.speed[1] = 0
                    Player.speed[0] = 0


#
if __name__ == "__main__":
    main()