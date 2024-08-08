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

        # player turn env needs to persist
        self.player_turn_env: Environment = Environment("Player Options")
        self.player_turn_env.extend_commands({
            "Attack": self.player_attack,
            "Switch Weapon": lambda: equip_weapon_menu(self.player),
            "Move": self.player_move,
            "End Turn": self.player_end_turn
        })

    def player_attack(self):
        attack_roll = self.player.attack_roll()
        if attack_roll >= self.enemy.calc_ac():
            damage: int = self.player.roll_damage()
            print(f"You rolled {attack_roll} and dealt {damage} damage with your {self.player.weapon.name}.")
            self.enemy.take_damage(damage)
        else:
            print(f"You rolled {attack_roll} and missed.")
        
        self.player_turn_env.show_menu()

    def player_end_turn(self):
        if self.enemy.hp > 0:
            print(f"{self.enemy.name} died. You won!")
            return None
        self.player_turn_env.restore_commands()
        self.enemy_turn()

    def player_move(self):
        self.player_turn_env.show_menu()
        self.player_turn_env.hide_command("Move")

    def player_turn(self):
        self.player_turn_env.show_menu()

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
