import pygame

class rock(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
#        pygame.sprite.Sprite__init__(self)
        self.image = pygame.image.load('Spacerock.png')
        self.image = pygame.transform.smoothscale(self.image,(100,100))
        self.rect = self.image.get_rect()
#        self.rect.center = pos
        self.speed = pygame.math.Vector2(5,5)
#        self.movex = x
#        self.movey = y
        self.rect.x = x
        self.rect.y = y

    def move(self):
        self.rect.x += self.speed [0]

    def update(self):
        self.rect.move_ip(self.speed)

