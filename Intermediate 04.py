#1. because variables are a volatile thing and file preserve even when the program is ended

#2.r - is when we wont only read and not change the file.   w- is mean you can create file and change it 
# a - create file and continue write from the end  b - binary file


#3.
# f = open("פיתון/חלק2/text.txt","r") 
# print(f.read())

# f=open("פיתון/חלק2/text.txt","a")
# f.write("Now the file has more content!")
# f.close()

#4.
import json

with open("פיתון/חלק2/j.json", 'r') as openfile:
    json_object = json.load(openfile)
 
json_object["data"]=json_object["data"].upper()
if json_object["silent"] == True:
    print(json_object["data"])
    
with open("פיתון/חלק2/j.json", "w") as outfile:
    json.dump(json_object, outfile)

# is format like dict to save data

# we use import json, and we use json.load() and json.dump()

with open("פיתון/חלק2/informtion", 'r') as openfile:
    json_object = json.load(openfile)
    
json_object["name"]="yehuda geller"
json_object["age"]=22
json_object["city"]="Bnei Brak"   

with open("פיתון/חלק2/my_info.json", "w") as outfile:
    json.dump(json_object, outfile)

