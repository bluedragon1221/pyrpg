"""Some helper commands so that you don't have to write them yourself"""

from lib.character import Player
from lib.container import Weapon
from lib.environment import Environment


class EquipWeaponMenu:
    def __init__(self, player: Player):
        self.environment = Environment("Equip Weapon Menu")
        self.environment.set_text("Select a weapon to equip")
        self.player: Player = player
        self.count = 0

    def make_menu_item(self, item: Weapon):
        self.count += 1
        return lambda: self.player.equip_weapon(item)

    def show_menu(self):
        self.environment.extend_commands(
            {
                item.name: self.make_menu_item(item)
                for item in self.player.inventory
                if isinstance(item, Weapon)
            }
        )

        self.environment.show_menu(
            show_global_commands=False, err="No weapons in inventory!"
        )
