from prettytable import PrettyTable # for sisplaying the tickets nicely
from dateutil import parser
from datetime import datetime

class TicketManager:
    def __init__(self):
        self.tickets = []

    def clear(self):
        self.tickets.clear()

    def reload(self, data):
        self.clear()
        for ticket_data in data["tickets"]:
            self.tickets.append(Ticket(ticket_data))

    def display(self, option, filters):
        table = PrettyTable()
        table.align = "l"
        table.field_names=["id", "subject", "description", "status", "created_at"]
        for ticket in self.tickets:
            if ticket.matching(option, filters):
                table.add_row(ticket.asRow())
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
        dt_object = dt_object.replace(tzinfo=None, fold=1)
        return dt_object
    except ValueError:
        return None 

class Ticket:
    def __init__(self, ticket_data:dict):
        self.id          = prepro(ticket_data.get("ticketId"))
        self.subject     = prepro(ticket_data.get("subject"))
        self.description = prepro(ticket_data.get("description"))
        self.status      = prepro(ticket_data.get("status"))
        self.created_at  = convertTime(prepro(ticket_data.get("created_at")))

    def matching(self, option, filters) -> bool:
        if (filters == None): return True
        elif (option == "search"):
            return (filters.lower() in self.id.lower() or 
                filters.lower() in self.subject.lower() or 
                filters.lower() in self.description.lower() or
                filters.lower() in self.status.lower()    
            )
        
        elif (option == "after"):
            if (self.created_at == None): return False
            return (parser.parse(filters) < self.created_at)
        elif (option == "before"):
            if (self.created_at == None): return False
            return (parser.parse(filters) > self.created_at)
        
        elif (option == "status"):
            return (filters.lower() in self.status)
        
        else:
            raise RuntimeError(f"no filter mode named {option}")
            
        return False
    
    def asRow(self):
        return [self.id, self.subject, self.description, self.status, self.created_at]
    
    # def __str__(self):
    #     return f"| {self.id} | {self.status}  \t| {self.subject} |\t |"