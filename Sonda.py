import pygame

 
class Sonda:
    def __init__(self, x, y):
        self.x = x
        self.y = y
 
    def muovi(self, dx, dy):
        self.x += dx
        self.y += dy
 
    def disegna(self, schermo):
        pygame.draw.circle(schermo, (200, 220, 255), (self.x, self.y), 10)
 
argo = Sonda(400, 300)
argo.muovi(5, 0)