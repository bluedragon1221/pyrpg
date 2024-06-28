"""Classes for managing environments that the player might be in"""

from typing import Callable, ClassVar, TypeAlias, Any

import questionary

Action: TypeAlias = Callable[[], Any]
CommandTable: TypeAlias = dict[str, Action]


def exec_picker(commands: CommandTable):
    choices: list[str] = list(commands.keys())
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

    def __init__(self, name: str, text: str=""):
        self.name = name
        self.text = text
        self.commands: CommandTable = {}

    def add_command(self, trigger: str, action: Action):
        self.commands[trigger] = action

    def command(self, trigger: str) -> Callable[[Callable[..., Any]], None]:
        """helper decorator for add_command"""

        def decorator(func: Callable[..., Any]):
            self.add_command(trigger, func)

        return decorator

    def extend_commands(self, commands: CommandTable):
        self.commands |= commands

    def rm_command(self, trigger: str):
        if trigger in self.commands:
            del self.commands[trigger]
        else:
            raise KeyError(f"There is no command with the name {trigger}")

    def show_menu(
        self,
        intro: bool=True,
        show_global_commands: bool=True,
        err: str="You haven't added any commands to the environment yet",
    ):
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
            print(err)

    @staticmethod
    def add_global_command(trigger: str, action: Action):
        Environment.global_commands[trigger] = action

    @staticmethod
    def global_command(trigger: str) -> Callable[[Callable[..., Any]], None]:
        def decorator(func: Callable[..., Any]):
            Environment.add_global_command(trigger, func)

        return decorator
