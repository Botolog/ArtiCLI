from funcs import *
from data import *
from commands import *



# todo: complete thoes commands and add help for each with syntax





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
