from data import *
import json

class Command:
    def __init__(self, name:str, action:callable):
        self.name = name
        self.action = action
        self.help = "no info"
    
    def showHelp(self):
        print(self.help)
    # def genSyntax(self):
    #     if self.name == "show":
    #         self.syntax = "show [filter_option] [*keywords]"

    def __call__(self, *args, **kwds):
        self.action(*args)


def readData(filename:str="data.json") -> dict:
    with open(filename, "r") as data:
        json_data = data.read()
        
    return json.loads(json_data)

DEFAULT_NAME

def loadData(filename:str="data.json"):
    global DATA
    new_data = readData(filename)
    DATA = new_data
    MANAGER.reload(DATA)
    setName(filename)

def displayArticles(option = "search", *filters):
    if not("tag" in option):
        MANAGER.display(option, " ".join(filters))
    else:
        MANAGER.display(option, filters)
        
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

def editField(id, field, *new_value):
    if len(new_value) != 0:
        value = " ".join(new_value)
    else:
        value = "None"
    
    MANAGER.edit(id, field, value)


def addtag(id, *tags):
    for tag in tags:
        try:
            MANAGER.getById(id).addtag(tag)
        except ValueError:
            pass
        

def remtag(id, *tags):
    for tag in tags:
        try:
            MANAGER.getById(id).remtag(tag)
        except ValueError:
            pass
        
def showHelp(*command_args):
    if len(command_args) == 0:
        COMMANDS["help"].showHelp()
    else:
        COMMANDS[command_args[0]].showHelp()

    

COMMANDS = {
    "load": Command("load", loadData), #load [filename]
    "show": Command("show", displayArticles), #show [option] [values]
    "clear": Command("clear", MANAGER.clear), #clear
    "save": Command("save", MANAGER.save), #save (current state) [filename]
    "create": Command("create", createArticle), #create [id] (following by costume input for convinience)
    "delete": Command("delete", MANAGER.delete), #delete [id]
    "edit": Command("edit", editField), #edit [id] [field] [new_val]
    "addtag": Command("addtag", addtag), #addtag [id] [tagname] [tagname]...
    "remtag": Command("remtag", remtag), #remtag [id] [tagname] [tagname]...

    "help": Command("help", showHelp)
}

COMMANDS["load"].help = """
The load command loads a json file to use.
Syntax: > load [filename]"""

COMMANDS["show"].help = """
The show command shows all the articles with filter options.
Syntax: > show [option/0] [values/0]
Options: \n\tserach (part of words or whole tags), \n\ttag (all the articles that contains at least one of the tags), \n\ttags (all the articles that contains all of the tags)
Examples: \n\t> show search payment \n\t> show tag checkout email"""

COMMANDS["clear"].help = """
The clear command clears the file without saving.
Syntax: > clear"""

COMMANDS["save"].help = """
The save command saves the changes to the last loaded file (data.json is default).
Syntax: > save [filename/0]"""

COMMANDS["create"].help = """
The create command creates a new article and show some dialogs to fill the data.
Syntax: > create [id] [title/0]"""

COMMANDS["delete"].help = """
The delete command deletes an entire article completly by id
Syntax: > delete [id]"""

COMMANDS["edit"].help = """
The edit command edits a specific field of an article by id.
Syntax: > edit [id] [field] [new_value]"""

COMMANDS["addtag"].help = """
The addtag command adds a tag to an article by id.
Syntax: > addtag [id] [tag_name] [tag_name] ..."""

COMMANDS["remtag"].help = """
The remtag command removes a tag from an article by id.
Syntax: > remtag [id] [tag_name] [tag_name] ..."""

COMMANDS["help"].help = f"""
Welcome to KBM! (Knowladge base Manager)
here you can manage your articles: load, create, remove, save, edit, search and more!
avalible commands: \n\t{"\n\t".join(COMMANDS.keys())}

you can check each command with: > help [command_name]
"""