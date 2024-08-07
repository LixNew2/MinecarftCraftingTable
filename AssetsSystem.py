from Button import Button
import json
from Vector2 import Vector2
from Item import Item
from Result import Result

class AssetsSystem:
    assets_data = "./data/items.json"
    assets_size = 48

    def __init__(self):
        self.buttons_items = []
        self.items = []
        self.result = []
        self.data = {}
        self.add_button() 

    def add_button(self):
        with open(AssetsSystem.assets_data, "r") as file:
            data = json.loads(file.read())

        x_offset = 0
        y_offset = 0
        for button in data:
            coordinates = Vector2(x_offset, y_offset)
            self.buttons_items.append(Button(data[button][0], data[button][1], coordinates, AssetsSystem.assets_size))
            x_offset += AssetsSystem.assets_size + 10

    def draw(self, window):
        def draw_buttons():
            for button in self.buttons_items:
                button.draw(window)

        def draw_items():
            for item in self.items:
                item.draw(window)

        def draw_result():
            for result in self.result:
                result.draw(window)
        
        draw_buttons()
        draw_items()
        draw_result()

    def buttons_clicked(self, pos):
        for button in self.buttons_items:
            if button.button_clicked(pos):
                    with open(AssetsSystem.assets_data, "r") as file:
                        data = json.loads(file.read())
                    for item in data:
                        if data[item][0] == button.BUTTON_ID:
                            self.items.append(Item(data[item][0], item, data[item][1], Vector2(button.button_coordinate.x, button.button_coordinate.y + 50), AssetsSystem.assets_size))

    def items_move(self, pos):
        for item in self.items:
            item.item_check_move(pos)

    def delete_item(self, pos):
        for item in self.items:
            item.delete_item(pos, self.items)
        
    def create_result(self, name : str, iamge_url : str):
        self.result.clear()
        self.result.append(Result(name, iamge_url, AssetsSystem.assets_size))
