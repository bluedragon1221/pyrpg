from lib.character import Character, Player
from lib.container import Weapon
from lib.combat import Combat

players_knife = Weapon("Knife", 4)
enemy_sword = Weapon("Sword", 6)

player = Player("Collin")
player.give_item(players_knife)
player.equip_weapon(players_knife)

enemy = Character("Bob", enemy_sword)

combat_env = Combat(player, enemy)
combat_env.initiate_combat()
