import questionary
from typing import Dict, Callable

def exec_picker(commands: Dict[str, Callable]):
        choices = commands.keys()
        action = questionary.select(
            message="", choices=choices, instruction=" ", qmark="", pointer=">"
        ).ask()

        if not action:
            raise Exception("Picker failed")
        elif action in commands:
            commands[action]()
        else:
            raise Exception(f"There is no command with the name {action}")

class Environment:
    global_commands = {}

    def __init__(self, name):
        self.name = name
        self.commands = {}
        self.text = ""

    def command(self, trigger: str):
        def decorator(func):
            self.add_command(trigger, func)

        return decorator

    def add_command(self, trigger: str, action):
        self.commands[trigger] = action

    def rm_command(self, trigger: str):
        if trigger in self.commands:
            del self.commands[trigger]
        else:
            raise Exception(f"There is no command with the name {trigger}")

    def show_menu(self, intro=True, show_global_commands=True):
        if show_global_commands == True and (Environment.global_commands) != 0:
            def open_global_picker():
                exec_picker(Environment.global_commands)
                self.show_menu(False)

            new_commands = self.commands | {"Command": open_global_picker}
        else:
            new_commands = self.commands
        
        if intro:
            print(self.text)
        exec_picker(new_commands)

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
