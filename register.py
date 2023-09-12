from Costumer import Costumer

class Register:
    def __init__(self, )-> None:
        self._profit_amount = 0
        self._total_sales = []
        
    @property
    def profit_amount(self):
        return self._profit_amount
    
    @profit_amount.setter  
    def profit_amount(self, x:str):
        self._profit_amount = x
    
    @property
    def total_sales(self):
        return self._total_sales
    
    @total_sales.setter
    def total_sales(self, x:dict):
        self._total_sales = x
    
    def checkout_customer(self,new_cost:Costumer):
        self.profit_amount+=new_cost.receipt
        self.total_sales.append(new_cost.name_clint)
    
    def print_summary(self):
        print(self.profit_amount)
        print(self.total_sales)