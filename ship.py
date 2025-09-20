import pygame

class Ship:
    """Gemiyi yonetecek bir sinif."""
    def __init__(self, ai_game):
        """Gemiyi baslat ve konumunu belirle"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #gemiyi yukle ve dikdortgenini al.\
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #Her gemiyi ekranin alt merkezinde baslat
        self.rect.midbottom = self.screen_rect.midbottom
        #Geminin yatay konumu icin ondalik bir degeri sakla
        self.x = float(self.rect.x)
        #Hareket bayragi
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """hareket bayragina bagli olarak geminin konumunu guncelle"""
        #rect'i degil de geminin x degerini guncelle
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed_factor
        #self.x'den rect nesnesini guncelle
        self.rect.x = self.x

    def blitme(self):
        """Gemiyi nevcut konumda ciz"""
        self.screen.blit(self.image, self.rect)