# Some helper commands so that you don't have to write them yourself
from lib.environment import Environment
from lib.character import Player
from lib.container import Object, Weapon

class EquipWeaponMenu:
    def __init__(self):
        self.environment = Environment("Equip Weapon")

    @staticmethod
    def make_menu_item(player: Player, weapon: Weapon):
        return lambda: player.equip_weapon(weapon)

    def show_menu(self, player: Player):
        weapon_count = 0
        for item in player.inventory:
            if isinstance(item, Weapon):
                weapon_count += 1
                self.environment.add_command(f"{item.name}", EquipWeaponMenu.make_menu_item(player, item))

        if weapon_count > 0:
            self.environment.set_text("Select the weapon to equip")
            self.environment.show_menu(show_global_commands=False)
        else:
            print("No weapons in inventory!")
        
