from typing import List, Iterator


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
    def __init__(self, name: str, damage: int):
        super().__init__(name)
        self.damage = damage


class Armor(Object):
    def __init__(self, name: str, ac: int):
        super().__init__(name)
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

    def format(self):
        ret = f"{self.name}:\n"
        for i in self.items:
            ret+=f"- {i.format()}\n"

        return ret
