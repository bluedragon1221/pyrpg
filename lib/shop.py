"""Helper for building a shop"""

from lib.character import Player
from lib.container import Object
from lib.environment import Environment


class Shop:
    """Helper for building a shop"""

    def __init__(self, name: str, player: Player, items: dict[Object, int]):
        self.name = name
        self.items: dict[Object, int] = items
        self.shop = Environment(
            self.name, text=f"Welcome to {self.name}. What would you like to buy?"
        )
        self.player = player

    def start_shop(self):
        def exit_shop():
            print(f"Thank you for shopping at {self.name}. Have a nice day!")

        # fmt: off
        self.shop.extend_commands({
            f"{item.name} - ${price}": self.make_shop_item(item, price)
            for item, price in self.items.items()
        } | {"Exit": exit_shop})
        # fmt: on

        self.shop.show_menu()

    @staticmethod
    def item_info(item: Object, price: int):
        return f"""Name: {item.name}
Description: {item.description}
Price: {price}"""

    def make_confirmation_env(self, item: Object, price: int) -> Environment:
        confirmation = Environment("confirm purchase")
        confirmation.text = f"""Are you sure you want to buy this item?
{self.item_info(item, price)}"""

        def confirm_buy():
            self.player.give_gold(-price)
            self.player.give_item(item)
            self.shop.rm_command(f"{item.name} - ${price}")
            print("Returning to shop")
            self.shop.show_menu()

        def cancel_buy():
            print("Return to shop")
            self.shop.show_menu()

        # fmt: off
        confirmation.extend_commands({
            "Yes": confirm_buy,
            "No, return to shop": cancel_buy
        })
        # fmt: on

        return confirmation

    def make_shop_item(self, item: Object, price: int):
        def buy_item():
            if self.player.gold < price:
                print(
                    f"""You can't afford {item.name}.
It costs {price} gold, but you only have {self.player.gold}."""
                )
                print("returning to shop")
                self.shop.show_menu()

            confirmation = self.make_confirmation_env(item, price)

            confirmation.show_menu()

        return buy_item
