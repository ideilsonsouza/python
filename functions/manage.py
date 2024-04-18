import sys

class Command:
    def __init__(self):
        self.commands = {}
        
    def register(self, name, func):
        self.commands[name] = func
        
    def execute(self, name, *args):
        if name in self.commands:
            self.commands[name](*args)
        else:
            print("Comando '{name}' não encontrado")

    def help(self):
        print("Lista de comandos registrados:")
        for command in self.commands:
            print(f" {command}")

if __name__ == "__main__":
    manage = Command()
    manage.register("help", manage.help)
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        args = sys.argv[2:]

        manage.execute(command, *args)
    else:
        print("Uso: python manage.py <comando> [argumentos]")