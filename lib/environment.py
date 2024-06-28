"""Classes for managing environments that the player might be in"""

from typing import Callable
from typing import ClassVar
from typing import TypeAlias

import questionary


CommandTable: TypeAlias = dict[str, Callable]


def exec_picker(commands: CommandTable):
    choices = commands.keys()
    action = questionary.select(
        message="", choices=choices, instruction=" ", qmark="", pointer=">"
    ).ask()

    if not action:
        raise EOFError("Picker closed unexpectedly")

    if action in commands:
        commands[action]()
    else:
        raise AttributeError(f"There is no command with the name {action}")


class Environment:
    """An Environment is anywhere where the player can make a choice"""

    global_commands: ClassVar[CommandTable] = {}

    def __init__(self, name):
        self.name = name
        self.commands: CommandTable = {}
        self.text = ""

    def add_command(self, trigger: str, action):
        self.commands[trigger] = action

    def command(self, trigger: str):
        """helper decorator for add_command"""

        def decorator(func):
            self.add_command(trigger, func)

        return decorator

    def extend_commands(self, commands: CommandTable):
        if not isinstance(commands, CommandTable):
            raise ValueError("That's not a valid command table. I can't append it")

        self.commands |= commands

    def rm_command(self, trigger: str):
        if trigger in self.commands:
            del self.commands[trigger]
        else:
            raise KeyError(f"There is no command with the name {trigger}")

    def show_menu(self, intro=True, show_global_commands=True, err="You haven't added any commands to the environment yet"):
        commands_len = len(self.commands)
        if show_global_commands and len(Environment.global_commands) != 0:
            def open_global_picker():
                exec_picker(Environment.global_commands)
                self.show_menu(False)

            new_commands = self.commands | {"Command": open_global_picker}
        else:
            new_commands = self.commands

        if intro:
            print(self.text)

        if commands_len > 0:
            exec_picker(new_commands)
        else:
            raise ValueError(err)

    def set_text(self, text: str):
        self.text = text

    def get_text(self):
        return self.text

    @staticmethod
    def add_global_command(trigger: str, action):
        Environment.global_commands[trigger] = action

    @staticmethod
    def global_command(trigger: str):
        def decorator(func):
            Environment.add_global_command(trigger, func)

        return decorator
