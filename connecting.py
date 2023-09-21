import pymongo


client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["Aviv's_people"]
family = db["my_family"]
friends = db["my_friends"]
army = db["my_army"]

family.drop()
friends.drop()
army.drop()


army_friend_list = [{'name':'Aviv','age':20, 'role':'Backend'},
{'name':'Lihi','age':21, 'role':'QA'},
{'name':'Gabi','age':22, 'role':'DevOps'},
{'name':'Ori','age':23, 'role':'Frond-end'},
{'name':'Ido','age':22, 'role':'developer'},
{'name':'Yarden','age':24, 'role':'DevOps'}]

family_list = [{'name':'mother','age':45, 'role':'teacher'},
{'name':'father','age':46, 'role':'engineer'},
{'name':'brother','age':12, 'role':'school'},
{'name':'sister','age':24, 'role':'student'}]

friends_group = [
        {"name": "Amit", "age": 20, "role": "waiter"},
        {"name": "Yonatan", "age": 24, "role": "doctor"},
        {"name": "Noa", "age": 22, "role": "student"},
        {"name": "Michal", "age": 21, "role": "baker"},
    ]

for i in family_list:
    result = family.insert_one(i)
    
result = army.insert_many(army_friend_list)
result = friends.insert_many(friends_group)

for x in family.find():
    print(x)
print('///////////////////////////////////')
for x in friends.find():
    print(x)
print('///////////////////////////////////')
for x in army.find():
    print(x)

query = {"name": "Lihi"}
results = army.delete_one(query)

friend_dev =army.find_one({"role" : "DevOps", "age" : {"$lt" : 23}})
# print(friend_dev)

    
friend_dev['age']
friend_work =army.find_one({'age':friend_dev['age'],'name':{"$ne":friend_dev['name']}})
army.update_one({'name':friend_dev['name']},{ "$set": { "role": friend_work['role'] } })

army_friends_sort = army.aggregate([{"$sort" : {"age" : -1}}, {"$out" : "army"}])

print('///////////////////////////////////')
for x in army.find():
    print(x)

delete_query = {"age" : {"$gt" : 23}}
moving_soldiers = army.find(delete_query)
add_friend = friends.insert_many(moving_soldiers)

del_from_army = army.delete_many(delete_query)

print('///////////////////////////////////')

for x in friends.find():
    print(x)
print('///////////////////////////////////')
for x in army.find():
    print(x)