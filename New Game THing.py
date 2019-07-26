#pygame setup here
import pygame
from pygame.locals import *
from Ship import Ship
from Astroids import rock
from G_O import GameOver
from Space import Space
from Win import Win
from Hearts import Heart
pygame.init()
screen_info = pygame.display.Info()
size = (width, height) = (int(screen_info.current_w),int(screen_info.current_h))
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (50, 100, 100)


#LevelData = df.iloc[Level]
#Player = Ship (((LevelData['PlayerX'], LevelData['PlayerY'])))
Player = Ship()
Go = GameOver()
Bg = Space()
enemy = rock(500, 300, 40, 25,5)
enemy2 = rock(300, 400, 90, 8, 30)
enemy3 = rock(700, 600, 70, 16, 6)
W = Win()
H = Heart(2, 90)
H2 = Heart (1, 60)
H3 = Heart (0, 30)

enemyGroup = pygame.sprite.Group()
enemyGroup.add(enemy)
enemyGroup.add(enemy2)
enemyGroup.add(enemy3)

Hgroup = pygame.sprite.Group()
Hgroup.add(H)
Hgroup.add(H2)
Hgroup.add(H3)


def main():
    while True:
        global color
        clock.tick(60)
        screen.fill(color)
        screen.blit(Bg.image, Bg.rect)
        screen.blit(Player.image, Player.rect)
        #screen.blit(enemy.image, enemy.rect)
        enemyGroup.draw(screen)
        Hgroup.draw(screen)
        screen.blit(Player.image, Player.rect)




        Player.update(enemyGroup)
        Go.update(Player.health)
        W.update(Player.win)
        Hgroup.update(Player.health)

        screen.blit(Go.image, Go.rect)
        screen.blit(W.image, W.rect)


        for en in enemyGroup:
            en.move()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit();
                sys.exit()
                main = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    Player.speed[0] = 5
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    Player.speed[0] += -5
                if event.key == pygame.K_UP or event.key == ord('w'):
                    Player.speed[1] += -5
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    Player.speed[1] += 5
                if event.key == pygame.K_SPACE:
                    Player.speed[1] += -5
                if event.key == event.key == ord('q'):
                    Player.speed[1] += -5
                    Player.speed[0] += -5
                if event.key == event.key == ord('e'):
                    Player.speed[1] += 5
                    Player.speed[0] += 5

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
        pygame.display.flip()


#
if __name__ == "__main__":
    main()