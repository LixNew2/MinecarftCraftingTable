from Vector2 import Vector2
import pygame

class Button:
    def __init__(self, id : int, image_url : str, xy : Vector2, size : int) -> None:
        pygame.init()
        self.button_coordinate = xy
        self.button_size = size
        self.BUTTON_ID = id

        self.button_ressource = pygame.image.load(image_url)
        self.button_ressource = pygame.transform.scale(self.button_ressource, (self.button_size, self.button_size))
        self.rect_ressource = self.button_ressource.get_rect(topleft=(self.button_coordinate.x, self.button_coordinate.y))


    def draw(self, window):
        window.blit(self.button_ressource, (self.button_coordinate.x, self.button_coordinate.y))

    def button_clicked(self, pos):
        if self.rect_ressource.collidepoint(pos):
            return True
            
