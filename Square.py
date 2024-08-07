import pygame

class Square:
    def __init__(self, x, y, width, height, color):
        pygame.init()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)