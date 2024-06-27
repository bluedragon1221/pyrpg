from lib.environment import Environment
from lib.character import Player
from lib.container import Object
from typing import Dict


class Shop:
    def __init__(self, name: str, items: Dict[Object, int]):
        self.name = name
        self.items: Dict[Object, int] = items
        self.shop = Environment(self.name)

    def start_shop(self, player: Player):
        print(self.items)
        self.shop.set_text(f"Welcome to {self.name}. What would you like to buy?")

        for item, price in self.items.items():
            command_name = f"{item.name} - ${price}"
            self.shop.add_command(
                command_name, self.make_shop_item(item, price, player)
            )

        @self.shop.command("Exit")
        def exit_shop():
            print(f"Thank you for shopping at {self.name}. Have a nice day!")

        self.shop.show_menu()

    def buy_item(player, item, price):
        player.give_gold(-price)
        player.give_item(item)

    def make_shop_item(self, item: Object, price: int, player: Player):
        def buy_item():
            if player.gold < price:
                print(
                    f"You can't afford {item.name}. It costs {price} gold, but you only have {player.gold}."
                )
                print("returning to shop")
                self.shop.show_menu()

            confirmation = Environment("confirm purchase")
            confirmation.set_text(f"""Are you sure you want to buy this item?
    Name: {item.name}
    Description: {item.description}
    Price: {price}""")

            @confirmation.command("Yes")
            def confirm_buy():
                self.buy_item(player, item, price)
                self.shop.rm_command(f"{item.name} - ${price}")
                print("Returning to shop")
                self.shop.show_menu()

            @confirmation.command("No, return to shop")
            def cancel_buy():
                print("Return to shop")
                self.shop.show_menu()

            confirmation.show_menu()

        return buy_item
