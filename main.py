from funcs import *
from data import *

COMMANDS = {
    "load": Command("load", loadData),
    "show": Command("show", displayArticles),
    "clear": Command("clear", MANAGER.clear),
    "save": Command("save", MANAGER.save), #save (current state) filename
    "create": Command("create", createArticle), #create [id] (following by costume input for convinience)
    "delete": Command("delete", MANAGER.delete), #delete [id]
    "edit": Command("edit", editField), #edit [id] [field] [new_val]
    # "addtag": , #addtag [id] [tagname]
    # "remtag": , #remtag [id] [tagname]

}

loadData()
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
