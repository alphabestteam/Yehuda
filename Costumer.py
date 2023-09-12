from Product import Product

class Costumer:
    def __init__(self, name_clint:str)-> None:
        self._name_clint = name_clint
        self._shopping_list = {}
        self._receipt = 0

    @property
    def name_clint(self):
        return self.name_clint
    
    @name_clint.setter  
    def name_clint(self, x:str):
        self._name_clint = x
    
    @property
    def shopping_list(self):
        return self._shopping_list
    
    @shopping_list.setter
    def shopping_list(self, x:dict):
        self._shopping_list = x
    
    @property    
    def receipt(self):
        return self._receipt
    
    @receipt.setter  
    def receipt(self, x:float):
        self._receipt = x
    
    def Add_product(self,new_product:Product):
        if new_product.name_product in self.shopping_list:
            self.shopping_list[new_product.name_product]["unit"]+= new_product.amount_unit
            self.receipt += self.shopping_list[new_product.name_product]["price"]*new_product.amount_unit
        else:
            self.shopping_list[new_product.name_product]={"product":new_product.name_product,"price":new_product.price_for_unit,"unit":new_product.amount_unit}
            self.receipt += new_product.price_for_unit*new_product.amount_unit
            
        
    def Remove_product(self,new_product:Product):
        if new_product.name_product in self.shopping_list:
            if new_product.amount_unit < self.shopping_list[new_product.name_product]["unit"] :
                self.shopping_list[new_product.name_product]["unit"]-= new_product.amount_unit
                self.receipt -= self.shopping_list[new_product.name_product]["price"]*new_product.amount_unit

            elif new_product.amount_unit >= self.shopping_list[new_product.name_product]["unit"]:
                print("removing the item")
                self.receipt -= self.shopping_list[new_product.name_product]["price"]*self.shopping_list[new_product.name_product]["unit"]
                print(self.shopping_list[new_product.name_product])
                del self.shopping_list[new_product.name_product]
        else:
            print("the item is not in the shopping list")
        


                
                

                               
    