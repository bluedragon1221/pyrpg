import questionary


class Environment:
    def __init__(self, name):
        self.name = name
        self.commands = {}

    def command(self, trigger):
        def decorator(func):
            self.commands[trigger] = func
            return func

        return decorator

    def add_command(self, trigger, action):
        self.commands[trigger] = action

    def rm_command(self, trigger):
        del self.commands[trigger]

    def show_menu(self, msg=""):
        choices = list(self.commands.keys()) + ["Command", "Quit"]
        action = questionary.select(
            message=msg, choices=choices, instruction=" ", qmark=""
        ).ask()

        if action == "Quit":
            return False
        elif action in self.commands:
            self.commands[action]()
        else:
            print("Invalid command. Try again.")
        return True

    def execute_command(self, trigger):
        if trigger in self.commands:
            self.commands[trigger]()
        else:
            print("Invalid command. Try again.")

class CurrentEnvironment():
    def __init__(default: Environment):
        self.current_environment = default

    def get_environment(self):
        self.current_environment

    def set_environment(self, env):
        self.current_environment = env
