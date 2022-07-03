import pygame, sys
from nave import Nave
from Bala_GP import Bullet
from alien import Alien

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
pink = (255,0,255)
yellow = (0,255,255)
green =(0,255,0)
blue = (0,0,255)

class primerjuego:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800,500))
        pygame.display.set_caption("primer juego")
        self.color = (white)
        self.nave = Nave(self)
        self.velocidad=1
        self.anchobala=3
        self.altobala= 15
        self.colorbala= (255,0,0)
        self.bullets = pygame.sprite.Group()
        self.aliens= pygame.sprite.Group()
        self._create_fleet()

    def corre_juego(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.quit()                                          
                elif event.type==pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.nave.mover_derecha= True  
                    if event.key==pygame.K_LEFT:
                        self.nave.mover_izquierda= True
                    if event.key == pygame.K_SPACE:
                        self._fire_bullet()
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.nave.mover_derecha= False
                    if event.key==pygame.K_LEFT:
                        self.nave.mover_izquierda= False
            self.nave.mover()
            self.screen.fill(white)
            self.nave.corre()
            self.bullets.update()
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()
            self.aliens.draw(self.screen)
            #actualiza la pantalla
            pygame.display.flip()

    def _fire_bullet(self):
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)
    
    def _create_fleet(self):
        alien = Alien(self)
        self.aliens.add(alien)
            
#objeto primerjuego
if __name__ == "__main__":
    a = primerjuego()
    a.corre_juego()
    
