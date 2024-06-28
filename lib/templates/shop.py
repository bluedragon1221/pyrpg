from lib.character import Player
from lib.container import Object
from lib.environment import Environment


class Shop:
    def __init__(self, name: str, player: Player, items: dict[Object, int]):
        self.name = name
        self.items: dict[Object, int] = items
        self.shop = Environment(self.name)
        self.player = player

    def start_shop(self):
        self.shop.set_text(f"Welcome to {self.name}. What would you like to buy?")

        def exit_shop():
            print(f"Thank you for shopping at {self.name}. Have a nice day!")

        self.shop.extend_commands(
            {
                f"{item.name} - ${price}": self.make_shop_item(item, price)
                for item, price in self.items.items()
            }
            | {"Exit": exit_shop}
        )

        self.shop.show_menu()

    def make_shop_item(self, item: Object, price: int):
        def buy_item():
            if self.player.gold < price:
                print(
                    f"You can't afford {item.name}. It costs {price} gold, but you only have {self.player.gold}."
                )
                print("returning to shop")
                self.shop.show_menu()

            confirmation = Environment("confirm purchase")
            confirmation.set_text(
                f"""Are you sure you want to buy this item?
    Name: {item.name}
    Description: {item.description}
    Price: {price}"""
            )

            @confirmation.command("Yes")
            def confirm_buy():
                self.player.give_gold(-price)
                self.player.give_item(item)
                self.shop.rm_command(f"{item.name} - ${price}")
                print("Returning to shop")
                self.shop.show_menu()

            @confirmation.command("No, return to shop")
            def cancel_buy():
                print("Return to shop")
                self.shop.show_menu()

            confirmation.show_menu()

        return buy_item
