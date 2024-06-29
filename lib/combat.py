"""Helpers for combat environments"""

from time import sleep

from lib.character import Character, Player
from lib.environment import Environment
from lib.equip_weapon_menu import equip_weapon_menu


class Combat:
    """Helpers for combat environments"""

    def __init__(self, player: Player, enemy: Character):
        self.player: Player = player
        self.enemy: Character = enemy

    def player_attack(self):
        attack_roll = self.player.attack_roll()
        if attack_roll >= self.enemy.calc_ac():
            damage: int = self.player.roll_damage()
            print(f"You rolled {attack_roll} and dealt {damage} damage with your {self.player.weapon.name}.")
            self.enemy.take_damage(damage)
        else:
            print(f"You rolled {attack_roll} and missed.")

    def player_turn(self):
        player_options_env = Environment("Player Options")

        # fmt: off
        player_options_env.extend_commands({
            "Attack": self.player_attack,
            "Switch Weapon": lambda: equip_weapon_menu(self.player)
        })
        # fmt: on

        player_options_env.show_menu()

        if self.enemy.hp <= 0:
            print(f"{self.enemy.name} died. You won!")
        else:
            self.enemy_turn()

    def enemy_turn(self):
        sleep(0.7)
        attack_roll = self.enemy.attack_roll()
        if attack_roll >= self.player.calc_ac():
            damage = self.enemy.roll_damage()
            self.player.take_damage(damage)
            print(f"""{self.enemy.name} rolled {attack_roll} and dealt {damage} damage with their {self.enemy.weapon.name}.
You now have {self.player.hp}/{self.player.max_hp} HP""")
        else:
            print(f"Enemy rolled {attack_roll} and missed.")

        print()

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
