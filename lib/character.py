from enum import Enum
from random import randint

from lib.container import Armor
from lib.container import Container
from lib.container import Object
from lib.container import Weapon


class Race(Enum):
    NONE = "none"
    DRAGONBORN = "dragonborn"
    DWARF = "dwarf"
    ELF = "elf"
    GNOME = "gnome"
    HALFELF = "half-elf"
    HALFLING = "halfling"
    HALFORC = "half-orc"
    HUMAN = "human"
    TIEFLING = "tiefling"


class Character:
    def __init__(self, name: str, race: Race):
        self.name: str = name
        self.race: Race = race
        self.armor: Armor | None = None
        self.holding: Weapon | None = None
        self.max_hp: int = 9
        self.hp: int = self.max_hp
        self.level: int = 1

    def level_up(self):
        self.level += 1
        self.max_hp += randint(1, 8) + 1

    def heal(self):
        self.hp = self.max_hp

    def take_damage(self, amount: int):
        self.hp -= amount

    def deal_damage(self) -> int:
        return self.holding.roll_die() + self.level

    def calc_ac(self) -> int:
        ac_modifier = 0
        if self.level <= 3:
            ac_modifier = 1
        elif self.level:
            ac_modifier = 2

        return min(10 + ac_modifier + self.armor.ac_bonus, 20)

    def calc_hp(self) -> int:
        return self.hp

    def attack_roll(self) -> int:
        return randint(1, 20) + min(self.level, 10)


class Player(Character):
    def __init__(self, name: str):
        super().__init__(name, Race.HUMAN)
        self.inventory: Container = Container("Inventory")
        self.gold: int = 80

    def give_item(self, item: Object):
        self.inventory.add(item)

    def give_gold(self, amount: int):
        self.gold += amount

    def equip_armor(self, armor: Armor):
        # remove item from slot
        if self.armor is not None:
            self.inventory.add(self.armor)
            self.armor = None

        if armor in self.inventory:
            self.inventory.remove(armor)
            self.armor = armor
        else:
            raise Exception(f"{armor.name} is not in inventory")

    def equip_weapon(self, weapon: Weapon):
        # remove item from slot
        if self.holding is not None:
            self.inventory.add(self.holding)
            self.holding = None

        if weapon in self.inventory:
            self.inventory.remove(weapon)
            self.holding = weapon
        else:
            raise Exception(f"{weapon.name} is not in inventory")
