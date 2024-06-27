import questionary
from result import Result, Ok, Err


class Environment:
    def __init__(self, name):
        self.name = name
        self.commands = {}
        self.text = ""

    def command(self, trigger: str):
        def decorator(func):
            self.add_command(trigger, func)

        return decorator

    def add_command(self, trigger: str, action) -> None:
        self.commands[trigger] = action

    def rm_command(self, trigger: str) -> Result[None, str]:
        if trigger in self.commands:
            del self.commands[trigger]
            return Ok(None)
        else:
            return Err(f"There is no command with the name {trigger}")

    def show_menu(self, msg="") -> Result[None, str]:
        print(self.text)
        choices = self.commands.keys()
        action = questionary.select(
            message=msg, choices=choices, instruction=" ", qmark="", pointer=">"
        ).ask()

        if not action:
            return Err("The action failed to execute")
        elif action in self.commands:
            return Ok(self.commands[action]())
        else:
            return Err(f"There is no command with the name {action}")

    def set_text(self, text: str):
        self.text = text

    def get_text(self):
        return self.text
