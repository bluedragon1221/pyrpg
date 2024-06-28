"""classes for defining game objects, such as Weapons and Armor, as well as Containers to group them together"""

from random import randint
from typing import Iterator
from typing import List


class Object:
    def __init__(self, name: str, count=1):
        self.name = name
        self.weight = 0
        self.description = ""
        self.price = 0
        self.count = count

    def set_description(self, txt: str):
        self.description = txt

    def get_description(self):
        return self.description

    def format(self):
        if self.count > 1:
            return f"{self.name} x{self.count}"
        else:
            return self.name


class Weapon(Object):
    def __init__(self, name: str, die: int):
        super().__init__(name)
        if die not in [1, 4, 6, 8, 10, 12, 20]:
            raise AttributeError(f"{die} is not a valid die.")
        self.damage_die = die

    def roll_die(self):
        return randint(1, self.damage_die)


class Armor(Object):
    def __init__(self, name: str, ac: int):
        super().__init__(name)
        self.ac_bonus = ac


class Container:
    def __init__(self, name: str):
        self.name = name
        self.items: List[Object] = []

    def as_list(self):
        return self.items

    def __iter__(self) -> Iterator[Object]:
        return iter(self.items)

    def txt_list(self) -> list[str]:
        return [item.name for item in self.items]

    def remove(self, item_to_remove: Object) -> None:
        new_list = [item for item in self.items if item != item_to_remove]

        if self.items == new_list:
            raise AttributeError(f"{item_to_remove} is not in {self.name}")
        else:
            self.items = new_list

    def find(self, item_name: str) -> Object:
        if item_name not in self.txt_list():
            raise AttributeError(f"{item_name} is not in {self.name}")
        else:
            return next(i for i in self.items if i.name == item_name)

    def add(self, item: Object) -> None:
        self.items.append(item)

    def extend(self, items: List[Object]) -> None:
        for item in items:
            self.add(item)

    def format(self):
        ret = f"{self.name}:\n"
        for i in self.items:
            ret += f"- {i.format()}\n"

        return ret
