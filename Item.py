from Vector2 import Vector2
import pygame

class Item:
    def __init__(self, id : int, name : str, image_url : str, xy : Vector2, size : int) -> None:
        pygame.init()
        self.ITEM_ID = id
        self.name = name
        self.item_coordinate = xy
        self.item_size = size

        self.item_ressource = pygame.image.load(image_url)
        self.item_ressource = pygame.transform.scale(self.item_ressource, (self.item_size, self.item_size))
        self.rect_ressource = self.item_ressource.get_rect(topleft=(self.item_coordinate.x, self.item_coordinate.y))

    def draw(self, window):
        window.blit(self.item_ressource, (self.item_coordinate.x, self.item_coordinate.y))

    def item_check_move(self, pos):
        if self.rect_ressource.collidepoint(pos):
            self.item_coordinate.x = pos[0] - self.item_size // 2
            self.item_coordinate.y = pos[1] - self.item_size // 2
            self.rect_ressource.topleft = (self.item_coordinate.x, self.item_coordinate.y)

    def delete_item(self, pos, itemlist):
        if self.rect_ressource.collidepoint(pos):
            itemlist.remove(self)
            
            
