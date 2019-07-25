import pygame

class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('ufo.png')
        self.image = pygame.transform.smoothscale(self.image,(100,100))
        self.rect = self.image.get_rect()
#        self.rect.center = pos
        self.speed = pygame.math.Vector2(0,0)
        self.movex = 100
        self.movey = 100
        self.health = 3

    def update(self, enemyGroup):
        self.rect.move_ip(self.speed)
        self.movex += self.speed[0]
        self.movey += self.speed[1]
        hitlist = pygame.sprite.spritecollide(self, enemyGroup, False)
        for enemy in hitlist:
            self.health -= 1
            print (self.health)
