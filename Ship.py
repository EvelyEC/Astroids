import pygame

class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('spaceship4.png')
        self.image = pygame.transform.smoothscale(self.image,(100,100))
        self.rect = self.image.get_rect()
#        self.rect.center = pos
        self.speed = pygame.math.Vector2(0,0)
        self.movex = 400
        self.movey = 400
        self.health = 3
        self.win = 0

    def update(self, enemyGroup):
        screen_info = pygame.display.Info()
        size = (width, height) = (int(screen_info.current_w), int(screen_info.current_h))

        if self.rect.bottom > height:
            self.win = 1
            print ("You WIN")


        self.rect.move_ip(self.speed)
        self.movex += self.speed[0]
        self.movey += self.speed[1]
        screen_info = pygame.display.Info()

        hitlist = pygame.sprite.spritecollide(self, enemyGroup, False)
        for enemy in hitlist:
            self.health -= 1
            print (self.health)
            enemyGroup.remove(enemy)
        if self.health == 0:
            self.image = pygame.transform.smoothscale(self.image, (1, 1))
 #           from G_O import GameOver
  #          screen.blit(GameOver.image, GameOver.rect)

