from Vector2 import Vector2
import pygame

class Result:
    results_coordinate = Vector2(501,281)

    def __init__(self, name : str, image_url : str, size: int):
        pygame.init()
        self.name = name
        self.result_size = size

        self.result_ressource = pygame.image.load(image_url)
        self.result_ressource = pygame.transform.scale(self.result_ressource, (self.result_size, self.result_size))
        self.rect_ressource = self.result_ressource.get_rect(topleft=(self.results_coordinate.x, self.results_coordinate.y))


    def draw(self, window):
        window.blit(self.result_ressource, (Result.results_coordinate.x, Result.results_coordinate.y))


