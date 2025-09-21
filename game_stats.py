class GameStats:
    """Uzayli istilasi icin istatistik tut"""
    def __init__(self, ai_game):
        """istatistiklere ilk deger ata"""
        self.settings = ai_game.settings
        self.reset_stats()
        #Oyunu Aktif olmayan bir durumda baslat
        self.game_active = False



    def reset_stats(self):
        """Oyun esnasinda degisebilecek istatistiklere ilk deger ata"""
        self.ship_left = self.settings.ship_limit
        self.score = 0

        #en yuksek skor hicbir zaman resetlenmemeli
        self.high_score = 0


