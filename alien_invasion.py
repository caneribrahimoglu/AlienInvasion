import sys
import pygame
from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien
from time import sleep


class AlienInvasion():
    """Oyun degerlerini ve davranisini yonetmek icin bir sinif"""
    def __init__(self):
        """Oyunu baslat ve oyun kaynaklarini olustur"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption('Alien Invasion')
        #Oyun istatistiklerini saklamak icin bir ornek olustur
        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        #Arka plan rengini ayarla
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """Oyun icin ana donguyu baslat"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
            self._update_screen()

    def _check_events(self):
        """Klavye ve fare olaylarina yanit ver"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)


    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            # Gemiyi saga hareket ettir
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Yeni bir mermi olustur ve bu mermiyi mermi grubuna ekle"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Mermi ve Uzayli carpismasina izin ver"""
        #Uzaylilara carpan mermileri kontrol et ve bulustular ise ikisinden de kurtul
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if not self.aliens:
            #var olan mermileri imha et ve yeni filo olustur
            self.bullets.empty()
            self._create_fleet()

    def _update_aliens(self):
        """Filonun kenarda olup olmadigini kontrol et ve daha sonra  Filodaki tum uzaylilarin konumlarini guncelle"""
        self._check_fleet_edges()
        self.aliens.update()

        if pygame.sprite.spritecollide(self.ship, self.aliens, False):
            self._ship_hit()
        self._check_aliens_bottom()

    def _update_screen(self):
        """Ekrandaki resimleri guncelle ve yeni ekrana don"""
        # donguden her geciste ekrani yeniden cizdir
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # en son cizilen ekrani gorunur yap
        self.aliens.draw(self.screen)
        pygame.display.flip()

    def _create_fleet(self):
        """Uzayli filosunu olustur"""
        #Bir uzayli olustur ve satirdaki uzayli sayisini bul. Her bir uzayli arasindaki bosluk bir uzayli kadardir
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_alien_x = available_space_x // (2 * alien_width)

        #ekrana sigan uzayli sayisini belirle
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (15 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        #Tum bir uzayli filosunu olustur
        for row_number in range(number_rows):
            for alien_number in range(number_alien_x):
                self._create_alien(alien_number, row_number)


    def _create_alien(self, alien_number, row_number):
        """Bir uzayli olustur ve satira yerlestir"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien_height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """Herhangi bir uzayli kenara yaklasinca uygun bir sekilde yanit ver"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Tum bir filoyu dusur ve filonun yonunu degistir"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _ship_hit(self):
        """Uzayli tarafindan vurulan gemiye yanit ver"""
        if self.stats.ship_left > 0:
            # Kalan gemi sayisini azalt
            self.stats.ship_left -= 1
            # Geri kalan uzayli gemisi ve mermilerden kurtul
            self.aliens.empty()
            self.bullets.empty()

            # Yeni bir filo olustur ve gemiyi merkeze koy
            self._create_fleet()
            self.ship.center_ship()
            # Durdur 1 sn
            sleep(1)
        else:
            self.stats.game_active = False



    def _check_aliens_bottom(self):
        """Herhangi bir uzaylinin ekranin alt kismina ulasip ulasmadigini kontrol et"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break


if __name__ == '__main__':
    #bir oyun ornegi olustur ve oyunu calistir
    ai = AlienInvasion()
    ai.run_game()