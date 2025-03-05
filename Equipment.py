from connection import *
from Associate import *

class Equipment:
    def __init__(self, no, amount, condition):
        self.no = no
        self.amount = amount
        self.condition = condition
        self.branch = 1
        createEquip(no, amount, condition, self.branch)
        
    def updateCondition(self, status):
        updateEquipCond(self.no, status)
        self.status = status
        
    def addAmount(self):
        updateEquipAmount(self.no)
        self.amount = self.amount +1
    
    def getAmount(self):
        return self.amount
    
    def getCondition(self):
        return self.condition