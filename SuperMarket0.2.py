def main():

    receipt=0
    shopping_list =[]

    while True:
        options= int(input("  1 - add item , 2 - remove item , 3- exit "))

        if 1<=options<=3:
            if options ==3:
                print(f"your total is: {receipt}" )
                print(shopping_list) 
                break
            
            item = input("enter name item: ")
            price = float(input("enter the price: "))
            unit = int(input("enter how match unit: "))
            
            if options ==1:    
                if any(item in _ for _ in shopping_list):                     
                    for i in range(len(shopping_list)):
                        if item in shopping_list[i]:                           
                           shopping_list[i][item]["unit"] = shopping_list[i][item]["unit"]+unit 
                           receipt =receipt+ shopping_list[i][item]["price"]*unit
                else:
                    shopping_list.append({item:{"price":price,"unit":unit}})
                    receipt += shopping_list[-1][item]["price"]*shopping_list[-1][item]["unit"] 
                    print(receipt)   
                    print(shopping_list)                     

            elif options ==2:    
                if any(item in _ for _ in shopping_list):                     
                    for i in range(len(shopping_list)):
                        if item in shopping_list[i]:
                            if shopping_list[i][item]["unit"] >= unit:
                                 if shopping_list[i][item]["unit"] == unit:
                                     shopping_list.remove(shopping_list[i])
                                 else:
                                     shopping_list[i][item]["unit"] = shopping_list[i][item]["unit"]-unit
                                     receipt -= shopping_list[i][item]["price"]*unit
                            elif shopping_list[i][item]["unit"]< unit:
                                print("there is not enough unit")
                            else:
                                print("the item is not exists")   
            else:
                print("not valid number")
            
if(__name__ == "__main__"):
    main()
