import pygame.font

class Button:

    def __init__(self, ai_game, msg):
        """Dugmenin niteliklerine ilk degeri ata"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        #dugmenin ozelliklerini ve boyutlarini ayarla
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont('comicsans', 48)

        #dugmenin rext nesnesini olustur ve merkeze koy
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        #dugmenin mesajinin sadece bir kez hazirlamasi gerekir
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """msg'yi islenmis bir resme donustur ve metni dugmenin merkezine yerlestir"""

        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """bos bir dugme ciz ve sonra mesaji ciz"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
