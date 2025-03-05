from connection import *
from Employee import *
from Room import *

class Trainer(Employee):
    def __init__(self, ssn, email, phone, f, l, address):
        self.ssn = ssn
        self.fname = f
        self.lname = l
        self.address = address
        self.phone = phone
        self.email = email
        self.branch = 1
        createAssociate(ssn, id, email, phone, f, l, address, self.branch)
        self.id = getTrainerID(ssn)
  
        
    def getTrainer(self):
        return self.ssn
        
    def removeTrainer(self, ssn):
        deleteTrainer(ssn)
        
        
    def bookRoom(id, date, duration):
        return True