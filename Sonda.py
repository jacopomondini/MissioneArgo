import pygame

 
class Sonda:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.__energia = 100

    def muovi(self, dx, dy):
        self.x += dx
        self.y += dy
 
    def disegna(self, schermo):
        pygame.draw.circle(schermo, (200, 220, 255), (self.x, self.y), 10)

    @property
    def energia(self):
        return self.__energia
 
    @energia.setter
    def energia(self, valore):
        self.__energia = max(0, min(100, valore))  # resta tra 0 e 100
 

argo = Sonda(400, 300)
argo.muovi(5, 0)
