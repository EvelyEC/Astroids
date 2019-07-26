import pygame

class rock(pygame.sprite.Sprite):
    def __init__(self,x,y,scale, speedx,speedy):
        super().__init__()
#        pygame.sprite.Sprite__init__(self)
        print ("Making Astriod")
        self.image = pygame.image.load('Spacerock2.png')
        self.image = pygame.transform.smoothscale(self.image,(scale,scale))
        self.rect = self.image.get_rect()
#        self.rect.center = pos
        self.speed = pygame.math.Vector2(speedx,speedy)
#        self.movex = x
#        self.movey = y
        self.rect.x = x
        self.rect.y = y

    def move(self):
        screen_info = pygame.display.Info()
        size = (width, height) = (int(screen_info.current_w), int(screen_info.current_h))

        self.rect.x += self.speed [0]
        if self.rect.top < 0 or self.rect.bottom > height:
            self.speed[1] *= -1
            self.image = pygame.transform.flip(self.image, True, False)

        if self.rect.left < 0 or self.rect.right > width:
            self.speed[0] *= -1
            self.image = pygame.transform.flip(self.image, True, False)

#    def update(self):
#        self.rect.move_ip(self.speed)

