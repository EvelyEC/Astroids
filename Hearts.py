import pygame

class Heart(pygame.sprite.Sprite):
    def __init__(self, idk, x):
        super().__init__()
        screen_info = pygame.display.Info()
        size = (width, height) = (int(screen_info.current_w), int(screen_info.current_h))
        self.image = pygame.image.load('heart.gif')
        self.image = pygame.transform.scale(self.image,(30,30))

        self.rect = self.image.get_rect()
        self.rect.center = (x, 10)
        self.idk = idk

    def update(self, health):
        if health == self.idk:
            self.rect.center = (5000, 5000)

