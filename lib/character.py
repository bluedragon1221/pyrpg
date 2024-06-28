"""Classes for creating players and other characters"""

from random import randint

from lib.container import Armor
from lib.container import Container
from lib.container import Object
from lib.container import Weapon

class Character:
    def __init__(self, name: str, weapon=None):
        self.name: str = name
        self.armor: Armor | None = None
        self.holding: Weapon | None = weapon
        self.max_hp: int = 9
        self.hp: int = self.max_hp
        self.level: int = 1

    def level_up(self):
        """When the character levels up, increment level by 1, and HP by 1d8 + 1"""
        self.level += 1
        self.max_hp += randint(1, 8) + 1

    def heal(self):
        self.hp = self.max_hp

    def take_damage(self, amount: int):
        self.hp -= amount

    def calc_damage(self) -> int:
        return self.holding.roll_die() + self.level

    def calc_ac(self) -> int:
        dex_modifier = 0
        if self.level <= 3:
            dex_modifier = 1
        elif self.level:
            dex_modifier = 2

        return min(10 + dex_modifier + (self.armor.ac_bonus if (self.armor is not None) else 0), 20)

    def calc_hp(self) -> int:
        return self.hp

    def attack_roll(self) -> int:
        return randint(1, 20) + min(self.level, 10)


class Player(Character):
    def __init__(self, name: str):
        super().__init__(name)
        self.inventory: Container = Container("Inventory")
        self.gold: int = 80

    def give_item(self, item: Object):
        self.inventory.add(item)

    def give_gold(self, amount: int):
        self.gold += amount

    def equip_armor(self, armor: Armor):
        """Unequip the current armor and equip this new one instead

        Args:
            armor (Armor): The armor to give the player

        Raises:
            ValueError: if item doesn't exist
        """
        # move item from slot to inventory
        if self.armor is not None:
            self.inventory.add(self.armor)
            self.armor = None

        if armor in self.inventory:
            self.inventory.remove(armor)
            self.armor = armor
        else:
            raise AttributeError(f"{armor.name} is not in inventory")

    def equip_weapon(self, weapon: Weapon):
        """Unequip current weapon and equip this one instead

        Args:
            weapon (Weapon): The weapon to equip

        Raises:
            ValueError: If weapon not in inventory
        """
        # move item from slot to inventory
        if self.holding is not None:
            self.inventory.add(self.holding)
            self.holding = None

        if weapon in self.inventory:
            self.inventory.remove(weapon)
            self.holding = weapon
        else:
            raise AttributeError(f"{weapon.name} is not in inventory")
