from lib.character import Player
from lib.container import Object
from lib.container import Weapon
from lib.environment import Environment
from lib.templates import Shop


player = Player("Collin")
player.give_gold(200)

flower_patch = Environment("flower patch")
flower_patch.set_text("The testing environment, code name `Flower Patch`")


@flower_patch.command("Enter shop")
def enter_shop():
    club = Weapon("Club", 10)
    club.set_description("A big bludgeoning stick")
    axe = Weapon("Axe", 12)
    axe.set_description("It chops stuff")

    shop_items: dict[Object, int] = {club: 10, axe: 12}

    weaponary = Shop("Collin's Weaponary", player, shop_items)
    weaponary.start_shop()

    # return to flower patch after shop exits
    flower_patch.show_menu()


@flower_patch.command("Quit")
def exit_game():
    pass


@Environment.global_command("Inventory")
def view_inventory():
    print(player.inventory.format())

@Environment.global_command("HP")
def view_hp():
    print(f"HP: {player.calc_hp()}/{player.max_hp}")

flower_patch.show_menu()
