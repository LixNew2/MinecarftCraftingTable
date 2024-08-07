import pygame, json
from Vector2 import Vector2
from Square import Square
from Result import Result

class CraftTable:
    def __init__(self, window):
        pygame.init()
        self.craft_squares = []
        self.result_square = None
        self.result = []
        self.WINDOW = window
        self.coordinates = Vector2(200, 220)
        self.schemas = "./data/crafts_schemas.json"
        self.last_schema = ""
        self.add_craft_square()
        self.add_result_square()

    def add_craft_square(self):
        for i in range(1, 10):
            self.craft_squares.append(Square(self.coordinates.x, self.coordinates.y, 50, 50, (255, 255, 255)))

            if i % 3 == 0:
                self.coordinates.x = 200
                self.coordinates.y += 60
            else:
                self.coordinates.x += 60

    def add_result_square(self):
        self.result_square = Square(500, 280, 50, 50, (255, 255, 255))

    def draw(self):
        for square in self.craft_squares:
            pygame.draw.rect(self.WINDOW, square.color, square.rect)

        pygame.draw.rect(self.WINDOW, self.result_square.color, self.result_square.rect)

        for result in self.result:
            result.draw(self.WINDOW)

    def check_schemas(self, ass_sys : list):
        with open(self.schemas, "r") as file:
            data = json.loads(file.read())
        
        square_used = [0] * len(self.craft_squares)

        for index, square in enumerate(self.craft_squares):
            for item in ass_sys.items:
                if square.rect.colliderect(item.rect_ressource):
                    item.rect_ressource.center = square.rect.center
                    item.item_coordinate = Vector2(item.rect_ressource.x, item.rect_ressource.y)
                    square_used[index] = item.ITEM_ID

        for schema in data:
            if square_used == data[schema][0]:
                ass_sys.create_result(schema, data[schema][1])
                self.last_schema = schema
            else:
                if self.last_schema:
                    if square_used != data[self.last_schema][0]:
                        ass_sys.result.clear()