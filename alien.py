import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Filodaki tek bir uzayliyi temsil eden bir sinif"""
    def __init__(self, ai_game):
        """uzayliyi baslat ve konumunu ayarla"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #Uzayli resmini ekle ve rect niteligini ayarla
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #her bir uzayliyi ekranin sol ust kismina yakin bir yerde baslat
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #uzaylinin tam yatay konumunu sakla
        self.x = float(self.rect.x)



    def check_edges(self):
        """Uzayli ekranin kenarinda ise True dondur"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Uzayliyi saga veya sola hareket ettir."""
        self.x += (self.settings.alien_speed_factor * self.settings.fleet_direction)
        self.rect.x = self.x