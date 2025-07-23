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

    def save(self, filemame:str="copy.json"):
        dump = json.dumps({"articles":self.articles}, indent=2, default=json_serializer)
        with open(filemame, "w") as output:
            output.write(dump)

    def create(self, id):
        for article in self.articles:
            if article.id == id:
                raise ValueError("Article with this id is already existing")
        new_article = Article()
        new_article.id = id
        self.articles.append(new_article)
        return new_article
        
    def delete(self, id):
        for i in range(len(self.articles)):
            print(i)
            if self.articles[i].id == id:
                return self.articles.pop(i)
        raise ValueError(f"Article id {id} not found")

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
        

        elif (option == "tag"):
            return (filters.lower() in self.tags)
        
        else:
            raise RuntimeError(f"no filter mode named {option}")
            
        return False
    

    def addtag(self, tag_name):
        if not (tag_name in self.tags):
            self.tags.append(tag_name)

    def remtag(self, tag_name):
        if (tag_name in self.tags):
            self.tags.remove(tag_name)
        else:
            raise ValueError(f"tag {tag_name} wasn't fount in {self.tags}")

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
    