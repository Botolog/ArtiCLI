from funcs import *
from data import *

DATA:dict = {}

MANAGER = TicketManager()

def updateData(filename:str):
    global DATA
    new_data = readData(filename)
    DATA = new_data
    MANAGER.reload(DATA)

def displayTickets(option = "search", filters = None):
    MANAGER.display(option, filters)

COMMANDS = {
    "update": Command("update", updateData),
    "show": Command("show", displayTickets),
    "clear": Command("clear", MANAGER.clear)
}


while True:
    try:
        command_string = input("> ").split(" ")
        command_name =  command_string[0]
        command_args = command_string[1:]
        command = COMMANDS[command_name]
        # command(*command_args)
        try:
            command(*command_args)
        except Exception as E:
            print(f"Error while executing \"{command_name}\": {E}")
            raise SyntaxError

    except SyntaxError:
        pass
    
    except KeyboardInterrupt:
        print("quitting...")
        quit()
    except KeyError as E:
        print(f"Command not found: \"{E.args[0]}\"")
    except Exception as E:
        print(E)
        quit()
