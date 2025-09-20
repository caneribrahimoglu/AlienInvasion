import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    """Gemiden ateslenen mermileri yoneten bir sinif"""
    def __init__(self, ai_game):
        """Geminin mevcut konumunda bir mermi nesnesi olustur"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        #0,0 da bir mermi rect'i olustur ve dogru konuma ayarla
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        #merminin konumunu ondalik bir deger olarak sakla
        self.y = float(self.rect.y)

    def update(self):
        """Mermiyi ekranda yukari dogru hareket ettir"""
        #merminin ondalik konumunu guncelle
        self.y -= self.settings.bullet_speed_factor
        #rect konumunu guncelle
        self.rect.y = self.y

    def draw_bullet(self):
        """Mermiyi ekrana ciz"""
        pygame.draw.rect(self.screen, self.color, self.rect)