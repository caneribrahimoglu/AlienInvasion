import pygame.font

class Scoreboard:
    """Score verme bilgisini bildiren bir sinif"""
    def __init__(self, ai_game):
        """Skor tutan niteliklere ilk deger ata"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        #skor verme bilgisi icin yazi tipi ayarlari
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont('comicsans', 48)

        #Baslangic skor resmini hazirla.
        self.prep_score()
        self.prep_high_score()

    def prep_high_score(self):
        """Yuksek skoru islenmis bir resme donustur"""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)

        #Yuksek skoru ekranin ust kisminda merkeze yerlestir
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.center = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top


    def prep_score(self):
        """Skoru islenmis bir resime donustur"""
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str.upper(), True, self.text_color, self.settings.bg_color)

        #skoru ekranin sag ust tarafinda goruntule
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def check_high_score(self):
        """Yeni bir yuksek skor olup olmadigini gormek icin denetle"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def show_score(self):
        """Skoru ekrana ciz"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)