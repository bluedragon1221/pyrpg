from lib.container import Object, Weapon
from lib.character import Player
from lib.environment import Environment
from lib.equip_weapon_menu import equip_weapon_menu

player = Player("Collin")

middle_meadow = Environment("middle meadow")
middle_meadow.text = """You arive in a meadow, surounded by a dense, lushous forest.
To the left, you see a patch of flowers.
To the right there is a dark, cluster of trees that almost looks like it's hiding something..."""

# --- Flower Patch

flower_patch = Environment("flower patch")
flower_patch.text = """You walk over to the patch of flowers.
They are beautiful and you can't help but wonder if your mom would like them.
Do you want to pick them?"""

@flower_patch.command("Pick them")
def pick_flowers():
    print("You pick the flowers")
    flowers = Object("flowers", 5)
    player.give_item(flowers)

    flower_patch.rm_command("Pick them")
    flower_patch.text = "You walk over to where you picked the patch of flowers."

    flower_patch.show_menu()

@flower_patch.command("Go back to the meadow")
def dont_pick_flowers():
    print("You turn around and head back to the middle of the meadow")
    middle_meadow.show_menu()

@middle_meadow.command("Go to the patch of flowers")
def patch_of_flowers():
    flower_patch.show_menu()

# --- Tree Cluster

tree_cluster = Environment("tree cluster")
tree_cluster.text = """You walk over to the cluster of trees.
Looking around further, you see an old, rusty sword hidden in the log of the tree.
Do you want to take it?"""


@middle_meadow.command("Go to the dark cluster of trees")
def trees():
    tree_cluster.show_menu()

@middle_meadow.command("Pick up knife in grass")
def take_knife_in_grass():
    print("You take the knife laying in the grass")
    knife = Weapon("knife", 4)
    player.give_item(knife)

    middle_meadow.rm_command("Pick up knife in grass")
    middle_meadow.show_menu(False)

@middle_meadow.command("Quit")
def exit_game():
    print("Thanks for playing!")

@tree_cluster.command("Take it")
def take_it():
    print("You stuff the sword in your backpack")
    sword = Weapon("rusty sword", 6)
    player.give_item(sword)

    tree_cluster.rm_command("Take it")
    tree_cluster.text = "Now you're at the cluster of trees, where you picked up the sword"
    tree_cluster.show_menu()

@tree_cluster.command("Turn back to the meadow")
def dont_take_it():
    print("You return back to the middle of the meadow")
    middle_meadow.show_menu()

@Environment.global_command("Equip Weapon")
def equip_weapon():
    equip_weapon_menu(player)

@Environment.global_command("All Info")
def all_info():
    player.all_player_info()

middle_meadow.show_menu()
