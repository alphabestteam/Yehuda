import json
from Product import Product
from Costumer import Costumer
from register import Register

p = Product("milk",2,2)
m = Product("milk",5,6)
e = Product("emilk",1,5)
c = Costumer("yehuda")
r = Register()

c.Add_product(m)
c.Add_product(p)
c.Add_product(e)
c.Remove_product(e)
c.Remove_product(p)

r.checkout_customer(c)
r.print_summary()
print((c.shopping_list))
print(c.receipt)
dict_json ={}
for i in r._total_sales:
    cart = [p for p in c.shopping_list]
    dict_json[i] = {"customer:" :i , "cart :": cart  , "total :" :r.profit_amount}
    
with open("items.json", "w") as outfile:
    json.dump(dict_json, outfile)

