from lib.container import Container, Object, Armor, Weapon
from enum import Enum

from random import randint


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
        self.name = name
        self.race = race
        self.armor: Armor = None
        self.holding: Weapon = None
        self.max_hp = 9
        self.hp = self.max_hp
        self.level = 1

    def level_up(self):
        self.level += 1
        self.max_hp += randint(1, 8) + 1

    def heal(self):
        self.hp = self.max_hp

    def take_damage(self, amount: int):
        self.hp -= amount

    def deal_damage(self) -> int:
        self.holding.roll_die() + self.level
        
    def calc_ac(self):
        ac_modifier = 0
        if self.level <= 3:
            ac_modifier = 1
        elif self.level:
            ac_modifier = 2

        return min(10 + ac_modifier + self.armor.ac_bonus, 20)

    def calc_hp(self):
        return self.hp

    def attack_roll(self):
        randint(1, 20) + min(self.level, 10)


class Player(Character):
    def __init__(self, name: str):
        super().__init__(name, Race.HUMAN)
        self.inventory = Container("Inventory")
        self.gold = 80

    def give_item(self, item: Object) -> None:
        self.inventory.add(item)

    def give_gold(self, amount: int) -> None:
        self.gold += amount

    def equip_armor(self, armor: Armor):
        # remove item from slot
        if not self.armor == None:
            self.inventory.add(self.armor)
            self.armor = None

        if armor in self.inventory:
            self.inventory.remove(armor)
            self.armor = armor
        else:
            raise Exception(f"{armor.name} is not in inventory")

    def equip_weapon(self, weapon: Weapon):
        # remove item from slot
        if not self.holding == None:
            self.inventory.add(self.holding)
            self.holding = None

        if weapon in self.inventory:
            self.inventory.remove(weapon)
            self.holding = weapon
        else:
            raise Exception(f"{weapon.name} is not in inventory")
