from funcs import *
from data import *

DATA:dict = {}

MANAGER = ArticleManager()

def loadData(filename:str="data.json"):
    global DATA
    new_data = readData(filename)
    DATA = new_data
    MANAGER.reload(DATA)

def displayArticles(option = "search", *filters):
    MANAGER.display(option, " ".join(filters))

def createArticle(id, *title):
    new_article = MANAGER.create(id)
    if len(title) != 0:
        title = " ".join(title)
        new_article.title = title
    else:
        new_article.title = input("Article Title: ")
    
    new_article.content = input("Article Content: ")
    last = "/"
    while last != "":
        last = input("Add Tag to Article (Empty to finish): ")
        if last != "":
            new_article.addtag(last)



# todo: complete thoes commands and add help for each with syntax
COMMANDS = {
    "load": Command("load", loadData),
    "show": Command("show", displayArticles),
    "clear": Command("clear", MANAGER.clear),
    "save": Command("save", MANAGER.save), #save (current state) filename
    "create": Command("create", createArticle), #create [id] (following by costume input for convinience)
    "delete": Command("delete", MANAGER.delete), #delete [id]
    # "edit": , #edit [id] [field] [new_val]
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
