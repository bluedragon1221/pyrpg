from enum import Enum
from typing import List, Iterator


class ObjectType(Enum):
    WEAPON = "weapon"
    ITEM = "item"


class Object(Enum):
    def __init__(self, object_type: ObjectType, name: str):
        self.object_type = object_type
        self.name = name

    def get_name(self) -> str:
        return self.name

    @classmethod
    def new_weapon(cls, name: str) -> "Object":
        obj = cls(cls.WEAPON)
        obj.name = name
        return obj

    @classmethod
    def new_item(cls, name: str) -> "Object":
        obj = cls(cls.ITEM)
        obj.name = name
        return obj


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


class Player:
    def __init__(self, name: str):
        self.name = name
        self.inventory = Container("inventory")
        self.gold = 0

    def get_inventory(self) -> Container:
        return self.inventory

    def give_item(self, item: Object) -> None:
        self.inventory.add(item)

    def remove_item(self, item: str) -> None:
        self.inventory.remove(item)

    def give_gold(self, amount: int) -> None:
        self.gold += amount
