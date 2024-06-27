# Some helper commands so that you don't have to write them yourself
from lib.character import Player
from lib.container import Weapon
from lib.environment import Environment


class EquipWeaponMenu:
    def __init__(self):
        self.environment = Environment("Equip Weapon Menu")
        self.environment.set_text("Select a weapon to equip")
        self.no_entries_messages: str = "No weapons in inventory!"

    @staticmethod
    def make_menu_item(player: Player, item: Weapon):
        return lambda: player.equip_weapon(item)

    @staticmethod
    def get_iterator(player: Player):
        return [item for item in player.inventory if isinstance(item, Weapon)]

    def show_menu(self, player: Player):
        entry_count = 0
        if entry_count > 0:
            for item in self.get_iterator(player):
                entry_count += 1
                self.environment.add_command(f"{item.name}", self.make_menu_item(player, item))
            self.environment.show_menu(show_global_commands=False)
        else:
            print(self.no_entries_messages)
