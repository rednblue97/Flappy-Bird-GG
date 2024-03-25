import pygame.sprite
import assets
import configs

class Background(pygame.sprite.Sprite):
    def __init__(self, *groups):


        self.image = assets.get_sprite("background")
        self.rect = self.image.get_rect(topleft=(0,0))

        super().__init__(*groups)

        def update(self):
            self.rect.x -= 1

        if self.rect.right <= 0:
            self.rect.x = configs.SCREEN_WIDTH