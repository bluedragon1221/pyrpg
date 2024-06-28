"""Some reusable components so that you don't have to make them yourself"""

from lib.character import Player
from lib.container import Weapon
from lib.environment import Environment


def equip_weapon_menu(player: Player):
    """Create a menu to help the player switch their weapon

    Args:
        player (Player): The player
    """

    environment = Environment("Equip Weapon Menu", text="Select a weapon to equip")

    def make_menu_item(item: Weapon):
        return lambda: player.equip_weapon(item)

    environment.extend_commands(
        {
            item.name: make_menu_item(item)
            for item in player.inventory
            if isinstance(item, Weapon)
        }
    )

    environment.show_menu(show_global_commands=False, err="No weapons in inventory!")
