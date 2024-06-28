"""Helpers for combat environments"""

from time import sleep

from lib.character import Character, Player
from lib.environment import Environment
from lib.equip_weapon_menu import equip_weapon_menu

class Combat:
    def __init__(self, player: Player, enemy: Character):
        self.player: Player = player
        self.enemy: Character = enemy

    def player_attack(self):
        if self.player.attack_roll() >= self.enemy.calc_ac():
            damage: int = self.player.calc_damage()
            print(f"You dealt {damage} damage to enemy")
            self.enemy.take_damage(damage)
        else:
            print("You missed!")

    def player_turn(self):
        player_options_env = Environment("Player Options")

        player_options_env.extend_commands({
            "Attack": self.player_attack,
            "Switch Weapon": lambda: equip_weapon_menu(self.player),
            "Quit": lambda: None,
        })

        print(f"Enemy now has {self.enemy.hp}/{self.enemy.max_hp} HP")
        player_options_env.show_menu()

        if self.enemy.hp <= 0:
            print("Enemy died. You won!")
        else:
            self.enemy_turn()

    def enemy_turn(self):
        sleep(.7)

        if self.enemy.attack_roll() >= self.player.calc_ac():
            damage = self.enemy.calc_damage()
            print(f"Enemy dealt {damage} damage to you")
            self.player.take_damage(damage)
        else:
            print("Enemy missed.")

        print(f"You now have {self.player.hp}/{self.player.max_hp} HP")

        if self.player.hp <= 0:
            print("You died. Enemy won!")
        else:
            self.player_turn()

    def initiate_combat(self):
        if self.player.weapon is None:
            print("You probably don't want to go into combat without a weapon drawn!")
            equip_weapon_menu(self.player)
        else:
            self.player_turn()
