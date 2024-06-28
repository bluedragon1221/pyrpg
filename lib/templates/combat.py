"""Helpers for combat environments"""

from time import sleep

from lib.character import Character, Player
from lib.environment import Environment
from lib.templates.equip_item_menu import EquipWeaponMenu

class Combat:
    def __init__(self, player: Player, enemy: Character):
        self.player: Player = player
        self.enemy: Character = enemy

    def player_attack(self):
        player_options_env = Environment("Player Options")

        @player_options_env.command("Attack")
        def attack():
            if self.player.attack_roll() >= self.enemy.calc_ac():
                damage: int = self.player.calc_damage()
                print(f"You dealt {damage} damage to enemy")
                self.enemy.take_damage(damage)
            else:
                print("You missed!")

        @player_options_env.command("Switch Weapon")
        def switch_weapon():
            menu = EquipWeaponMenu(self.player)
            menu.show_menu()

        @player_options_env.command("Quit")
        def exit_env():
            pass

        print(f"Enemy now has {self.enemy.hp}/{self.enemy.max_hp} HP")
        player_options_env.show_menu()

        if self.enemy.hp <= 0:
            print("Enemy died")
        else:
            self.enemy_attack()

    def enemy_attack(self):
        sleep(.7)

        if self.enemy.attack_roll() >= self.player.calc_ac():
            damage = self.enemy.calc_damage()
            print(f"Enemy dealt {damage} damage to you")
            self.player.take_damage(damage)
        else:
            print("Enemy missed")

        print(f"You now have {self.player.hp}/{self.player.max_hp} HP")

        if self.player.hp <= 0:
            print("You died")
        else:
            self.player_attack()

    def initiate_combat(self):
        if self.player.holding is None:
            print("You probably don't want to go into combat without a weapon drawn!")
            menu = EquipWeaponMenu(self.player)
            menu.show_menu()

        self.player_attack()
