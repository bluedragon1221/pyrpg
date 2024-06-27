from lib.container import Object, Player
from lib.environment import CurrentEnvironment, Environment

player = Player("Collin")

middle_meadow = Environment("middle meadow")
middle_meadow.set_text("""You arive in a meadow, surounded by a dense, lushous forest, tangled with vines and thick grasses.
To the left, you see a patch of flowers.
To the right there is a dark, cluster of trees that almost looks like it's hiding something...""")

env = CurrentEnvironment()

# --- Flower Patch

flower_patch = Environment("flower patch")
flower_patch.set_text("""You walk over to the patch of flowers.
They are beautiful and you can't help but wonder if your mom would like them.
Do you want to pick them?""")


@middle_meadow.command("Go to the patch of flowers")
def patch_of_flowers():
    env.set_environment(flower_patch)

    # Override the command so that you can't pick up the flowers again
    @middle_meadow.command("Go to the patch of flowers")
    def no_more_flowers():
        print("""There are no more flowers. You picked them all!
You turn around and head back to the middle of the meadow""")
        env.set_environment(middle_meadow)


@flower_patch.command("Pick them")
def pick_flowers():
    print("You pick the flowers and head back to the middle of the meadow")
    flowers = Object.new_item("flowers x5")
    player.give_item(flowers)
    env.set_environment(middle_meadow)


@flower_patch.command("Don't")
def dont_pick_flowers():
    print("You turn around and head back to the middle of the meadow")
    env.set_environment(middle_meadow)


# --- Tree Cluster

tree_cluster = Environment("tree cluster")
tree_cluster.set_text("""You walk over to the cluster of trees.
Looking around further, you see an old, rusty sword hidden in the log of the tree.
Do you want to take it?""")


@middle_meadow.command("Go to the dark cluster of trees")
def trees():
    env.set_environment(tree_cluster)


@tree_cluster.command("Take it")
def take_it():
    print("You stuff the sword in your backpack and return to the middle of the meadow")
    sword = Object.new_weapon("rusty sword")
    player.give_item(sword)


@tree_cluster.command("Dont")
def dont_take_it():
    print(
        "You don't take the sword, instead returning back to the middle of the meadow"
    )


if __name__ == "__main__":
    env.set_environment(middle_meadow)
    while True:
        if not env.get_environment().show_menu("What do you do?"):
            print("Thanks for playing!")
            break
