from typing import List, Iterator

class Object:
    def __init__(self, name: str, weight: int, price: int):
        self.name = name
        self.weight = weight
        self.description = ""
        self.price = price

    def set_description(self, txt: str):
        self.description = txt
    
    def get_description(self):
        return self.description


class Weapon(Object):
    def __init__(self, name: str, weight: int, price: int, damage: int):
        super().__init__(name, weight, price)
        self.damage = damage

    def format(self):
        return f"""    Name: {self.name}
    Description: {self.description}
    Price: {self.price}"""


class Armor(Object):
    def __init__(self, name: str, weight: int, price: int, ac: int):
        super().__init__(name, weight, price)
        self.ac_bonus = ac

class Container:
    def __init__(self, name: str):
        self.name = name
        self.items: List[Object] = []

    def __iter__(self) -> Iterator[Object]:
        return iter(self.items)

    def remove(self, item_name: str) -> None:
        self.items = [item for item in self.items if item.get_name() != item_name]

    def add(self, item: Object) -> None:
        self.items.append(item)

    def extend(self, items: List[Object]) -> None:
        for item in items:
            self.add(item)
