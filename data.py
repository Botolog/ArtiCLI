from prettytable import PrettyTable # for sisplaying the articles nicely
from dateutil import parser
from datetime import datetime
import json

class ArticleManager:
    def __init__(self):
        self.articles = []

    def clear(self):
        self.articles.clear()

    def reload(self, data):
        self.clear()
        for article_data in data["articles"]:
            self.articles.append(Article(article_data))

    def getById(self, id):
        for article in self.articles:
            if article.id == id:
                return article
        raise ValueError(f"No Article found with id {id}")

    def save(self, filename:str=None):
        global DEFAULT_NAME
        if filename == None: filename = DEFAULT_NAME
        else: DEFAULT_NAME = filename
        

        dump = json.dumps({"articles":self.articles}, indent=2, default=json_serializer)
        with open(filename, "w") as output:
            output.write(dump)

    def create(self, id):
        for article in self.articles:
            if article.id == id:
                raise ValueError(f"Article with id \"{id}\" already exists")
        new_article = Article()
        new_article.id = id
        self.articles.append(new_article)
        return new_article
    
    def edit(self, id, field, new_value):
        article = self.getById(id)
        article.edit(field, new_value)
        
    def delete(self, id):
        for i in range(len(self.articles)):
            if self.articles[i].id == id:
                return self.articles.pop(i)
        raise ValueError(f"Article id \"{id}\" not found")

    def display(self, option, filters):
        table = PrettyTable()
        table.align = "l"
        table.field_names=["id", "title", "content", "tags"]
        for article in self.articles:
            if article.matching(option, filters):
                table.add_row(article.asRow())
        if len(table.rows) == 0:
            print("No Data."); return 
        print(table)

def prepro(field):
    if field == None or field == "":
        return "None"
    return field

def convertTime(time_string:str) -> datetime:
    try:
        dt_object = parser.parse(time_string)
        dt_object = dt_object.replace(tzinfo=None)
        return dt_object
    except ValueError:
        return None 

class Article:
    def __init__(self, article_data:dict=None):
        self.tags = []
        if (article_data != None):
            self.id      = prepro(article_data.get("id"))
            self.title   = prepro(article_data.get("title"))
            self.content = prepro(article_data.get("content"))
            self.tags    = article_data.get("tags")
            if (type(self.tags) != list): self.tags = [self.tags]
        
    def matching(self, option, filters) -> bool:
        if (filters == None): return True
        elif (option == "search"):
            return (filters.lower() in self.id.lower() or 
                filters.lower() in self.title.lower() or 
                filters.lower() in self.content.lower() or
                filters.lower() in self.tags    
            )
        

        elif (option == "tags"):
            for tag in filters:
                if not(tag in self.tags):
                    return False
            return True
            
        elif (option == "tag"):
            for tag in filters:
                if (tag in self.tags):
                    return True
            return False
            # return (filters.lower() in self.tags)
        
        else:
            raise RuntimeError(f"no filter mode named \"{option}\"")
            
        return False
    

    def addtag(self, tag_name):
        if not (tag_name in self.tags):
            self.tags.append(tag_name)
        else:
            raise ValueError(f"tag \"{tag_name}\" already exists")

    def remtag(self, tag_name):
        if (tag_name in self.tags):
            self.tags.remove(tag_name)
        else:
            raise ValueError(f"tag \"{tag_name}\" wasn't fount in \"{self.tags}\"")

    def edit(self, field, new_value):
        if (field == "title"): self.title = new_value
        elif (field == "content"): self.content = new_value
        else:
            raise ValueError(f"you can't change the \"{field}\" of an Article")

    def asRow(self):
        return [self.id, self.title, self.content, self.tags]
    
    def toDict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "tags": self.tags 
        }
    
    # def __str__(self):
    #     return f"| {self.id} | {self.tags}  \t| {self.title} |\t |"

def json_serializer(object):
    if (hasattr(object, "toDict")):
        return object.toDict()
    

DEFAULT_NAME = "data.json"
def setName(name):
    global DEFAULT_NAME
    DEFAULT_NAME = name

DATA:dict = {}

MANAGER = ArticleManager()

