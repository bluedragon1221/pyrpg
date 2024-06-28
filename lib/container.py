"""Weapons and Armor, and Containers to hold them"""

from random import randint
from typing import Iterator
from typing import List


class Object:
    def __init__(self, name: str, count: int=1, description: str=""):
        self.name = name
        self.description = description
        self.count = count

    def format(self):
        if self.count == 1:
            return self.name
        return f"{self.name} x{self.count}"


class Weapon(Object):
    def __init__(self, name: str, die: int, count: int=1, description: str=""):
        super().__init__(name, count=count, description=description)
        if die not in [1, 4, 6, 8, 10, 12, 20]:
            raise AttributeError(f"{die} is not a valid die.")
        self.damage_die = die

    def roll_die(self):
        return randint(1, self.damage_die)


class Armor(Object):
    def __init__(self, name: str, ac: int, description: str=""):
        super().__init__(name, description=description)
        self.ac_bonus = ac
        self.is_stealthy = True


class Container:
    def __init__(self, name: str):
        self.name = name
        self.items: List[Object] = []

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
        if len(self.items) > 0:
            ret = f"{self.name}:\n"
            for i in self.items:
                ret += f"- {i.format()}\n"

            return ret
        else:
            return f"{self.name} is empty!"
