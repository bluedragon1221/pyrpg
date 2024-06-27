from lib.shop import Shop
from lib.character import Player
from lib.container import Weapon
from lib.environment import Environment

from result import Ok

player = Player("Collin")
player.give_gold(200)

flower_patch = Environment("flower patch")
flower_patch.set_text("The testing environment, code name `Flower Patch`")

@flower_patch.command("Enter shop")
def enter_shop():
    club = Weapon("Club", 2, 10, 10)
    club.set_description("A big bludgeoning stick")
    axe  = Weapon("Axe",  2, 12, 12)
    axe.set_description("It chops stuff")

    weaponry = Shop("Collin's Weaponry", [club, axe])
    weaponry.start_shop(player)

    # return to flower patch after shop exits
    flower_patch.show_menu()

@flower_patch.command("Quit")
def exit_game():
    pass


flower_patch.show_menu()
