import pygame

class Space(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        screen_info = pygame.display.Info()
        size = (width, height) = (int(screen_info.current_w), int(screen_info.current_h))
        self.image = pygame.image.load('space.png')
        self.image = pygame.transform.smoothscale(self.image,(width,height))

        self.rect = self.image.get_rect()
        self.rect.center = (width/2, height/2)
