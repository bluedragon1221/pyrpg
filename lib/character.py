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
        self.has_shield = False
        self.holding: Weapon = None
        self.max_hp = 9
        self.hp = self.max_hp
        self.level = 1

    def level_up(self):
        self.level += 1
        self.max_hp += randint(1, 8) + 1

    def heal(self):
        self.hp = self.max_hp

    def do_damage(self, amount: int):
        self.hp 

    def equip_armor(self, armor: Armor):
        self.armor = armor

    def equip_shield(self):
        self.has_shield = True

    def calc_ac(self):
        ac_modifier = 0
        if self.level <= 3:
            ac_modifier = 1
        elif self.level:
            ac_modifier = 2

        return min(10 + ac_modifier + self.armor.ac_bonus, 20)

    def calc_hp(self):
        return self.hp

class Player(Character):
    def __init__(self, name: str):
        super().__init__(name, Race.HUMAN)
        self.inventory = Container("inventory")
        self.gold = 80
    
    def give_item(self, item: Object) -> None:
        self.inventory.add(item)

    def remove_item(self, item: str) -> None:
        self.inventory.remove(item)

    def get_inventory(self) -> Container:
        return self.inventory

    def give_gold(self, amount: int) -> None:
        self.gold += amount

