from prettytable import PrettyTable # for sisplaying the tickets nicely
from dateutil import parser
from datetime import datetime

class TicketManager:
    def __init__(self):
        self.tickets = []

    def reload(self, data):
        for ticket_data in data["tickets"]:
            self.tickets.append(Ticket(ticket_data))

    def display(self, filters):
        table = PrettyTable()
        table.align = "l"
        table.field_names=["id", "subject", "description", "status", "created_at"]
        for ticket in self.tickets:
            if ticket.matching(filters):
                table.add_row(ticket.asRow())
        if len(table.rows) == 0:
            print("No Data. please load data first"); return 
        print(table)

def prepro(field):
    if field == None or field == "":
        return "None"
    return field

def convertTime(time_string:str) -> datetime:
    pass #TODO: make function

class Ticket:
    def __init__(self, ticket_data:dict):
        self.id          = prepro(ticket_data.get("ticketId"))
        self.subject     = prepro(ticket_data.get("subject"))
        self.description = prepro(ticket_data.get("description"))
        self.status      = prepro(ticket_data.get("status"))
        self.created_at  = prepro(ticket_data.get("created_at"))

    def matching(self, filters) -> bool:
        if (filters == None): return True
        if (filters in self.id or filters in self.subject or filters in self.description):
            return True
        return False
    
    def asRow(self):
        return [self.id, self.subject, self.description, self.status, self.created_at]
    
    def __str__(self):
        return f"| {self.id} | {self.status}  \t| {self.subject} |\t |"