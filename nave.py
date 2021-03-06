import pygame 

class Nave:
    def __init__(self, a_game):
        self.screen = a_game.screen
        self.screen_rect = a_game.screen.get_rect()
        self.image = pygame.image.load("nave.jpg")
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.mover_derecha= False
        self.mover_izquierda = False

    def mover(self):
        if self.mover_derecha:
            self.rect.x += 1
        if self.mover_izquierda:
            self.rect.x -= 1

    def corre(self):
        self.screen.blit(self.image,self.rect)