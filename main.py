from lib.container import Object, Weapon
from lib.character import Player
from lib.environment import Environment

player = Player("Collin")

middle_meadow = Environment("middle meadow")
middle_meadow.set_text("""You arive in a meadow, surounded by a dense, lushous forest, tangled with vines and thick grasses.
To the left, you see a patch of flowers.
To the right there is a dark, cluster of trees that almost looks like it's hiding something...""")

# --- Flower Patch

flower_patch = Environment("flower patch")
flower_patch.set_text("""You walk over to the patch of flowers.
They are beautiful and you can't help but wonder if your mom would like them.
Do you want to pick them?""")

@flower_patch.command("Pick them")
def pick_flowers():
    print("You pick the flowers")
    flowers = Object("flowers x5")
    player.give_item(flowers)

    flower_patch.rm_command("Pick them")
    flower_patch.set_text("You walk over to where you picked the patch of flowers.")
    
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
tree_cluster.set_text("""You walk over to the cluster of trees.
Looking around further, you see an old, rusty sword hidden in the log of the tree.
Do you want to take it?""")


@middle_meadow.command("Go to the dark cluster of trees")
def trees():
    tree_cluster.show_menu()

@middle_meadow.command("Quit")
def exit_game():
    print("Thanks for playing!")

@tree_cluster.command("Take it")
def take_it():
    print("You stuff the sword in your backpack")
    sword = Weapon("rusty sword", 3)
    player.give_item(sword)

    tree_cluster.rm_command("Take it")
    tree_cluster.set_text("Now you're at the cluster of trees, where you picked up the sword")
    tree_cluster.show_menu()


@tree_cluster.command("Turn back to the meadow")
def dont_take_it():
    print("You return back to the middle of the meadow")
    middle_meadow.show_menu()


middle_meadow.show_menu()
