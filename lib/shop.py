from lib.environment import Environment
from lib.character import Player
from lib.container import Object

class Shop:
    def __init__(self, name: str, items: list[Object]):
        self.name = name
        self.items = items

    def start_shop(self, player: Player):
        shop = Environment(self.name)
        shop.set_text(f"Welcome to {self.name}. What would you like to buy?")

        for item in self.items:
            command_name = f"{item.name} - ${item.price}"
            @shop.command(command_name)
            def buy_item():
                if player.gold < item.price:
                    print(f"You can't afford {item.name}. It costs {item.price} gold, but you only have {player.gold}.")
                    print("returning to shop")
                    shop.show_menu()

                confirmation = Environment("confirm purchase")
                confirmation.set_text(f"Are you sure you want to buy this item?\n{item.format()}")

                @confirmation.command("Yes")
                def confirm_buy():
                    player.give_gold(-item.price)
                    player.give_item(item)
                    shop.rm_command(command_name)
                    print("Returning to shop")
                    shop.show_menu()

                @confirmation.command("No, return to shop")
                def cancel_buy():
                    print("Return to shop")
                    shop.show_menu()

                confirmation.show_menu()

        @shop.command("Exit")
        def exit_shop():
            print(f"Thank you for shopping at {self.name}. Have a nice day!")

        shop.show_menu()

