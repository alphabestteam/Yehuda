from django.test import TestCase
from .models import Person,Parent
from django.test import Client
import json 
from django.urls import reverse




class PersonTestCase(TestCase):
    
    # fixtures = ['people_fixture.json'] // use all the database
    def setUp(self):
        Person.objects.create(  name ="hen",  id =10001,  date_of_birth ='1999-3-9' ,hometown ="Raanana" )
        Person.objects.create(  name ="dan",  id =10002,  date_of_birth ='2009-07-09' ,hometown ="Tel aviv")
        
        self.p1 = Parent.objects.create( name= "aba",id= 3, date_of_birth= "1980-12-02",hometown = "Bat Yam",work_space = "Google",salary = 50000)
        self.p2 = Parent.objects.create( name= "saba",id= 4, date_of_birth= "1880-12-02",hometown = "Bat Yam",work_space = "Google_old",salary = 25500)
        self.p3 = Parent.objects.create( name= "del",id= 10004, date_of_birth= "1880-12-02",hometown = "Bat Yam",work_space = "Google_old",salary = 25500)
        
        self.p1.child.set([10001, 10002])
        self.p2.child.set([3])
        self.client = Client()

    
    def test_age_person(self):
        hen = Person.objects.get(id = 10001)    
        dan = Person.objects.get(id = 10002)    
        self.assertEqual(hen.under_18(), True)
        self.assertEqual(dan.under_18(), False)
        
    def test_get_all_parents(self):
        response = self.client.get("/people/AllParent/")
        self.assertEqual(response.status_code, 200)
        data_length = len(response.json())
        self.assertEqual(data_length, 3)
        
    def test_add_parents(self):
        response = self.client.post("/people/AddParent/",{"id": 22, "name": "Dor", "date_of_birth": "1952-06-01", "hometown": "Haifa", "work_space": "Google", "salary": 41000, "child": [3]},content_type='application/json')
        self.assertEqual(response.status_code, 201)
    
    def test_del_parents(self):
        response = self.client.delete(f"/people/delParent/{10004}/")
        self.assertEqual(response.status_code, 204)
        
        with self.assertRaises(Parent.DoesNotExist):
             Parent.objects.get(id=10004)
    
    # def test_Update_parents(self):
    #     response = self.client.put("/people/UpdateParent/",json.dumps({id: 22, "name": "Dor", "date_of_birth": "1952-06-01", "hometown": "Haifa", "work_space": "-", "salary": 0, "child": [3]}))
    #     self.assertEqual(response.status_code, 200)
    
    def test_ConnectChild(self):
        response = self.client.put("/people/ConnectChild/",json.dumps({"id_parent":10004,"id_child":10001}))
        self.assertEqual(response.status_code, 200)
        
    # def test_ParentAndChild(self):
    #     response = self.client.get("/people/ParentAndChild/",{'id':4})
    #     self.assertEqual(response.status_code, 200)
            
    def test_rich_kid_view(self):
        response = self.client.get(reverse('richKid'))
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content.decode('utf-8'))
        self.assertIsInstance(data, list)
    
    def test_find_parent(self):
        response = self.client.get(f"/people/findParent/{10001}/")
        self.assertEqual(response.status_code, 200)
    
    def test_find_son(self):
        response = self.client.get(f"/people/findSon/{10004}/")
        self.assertEqual(response.status_code, 200)
    
    def test_findGrandfather(self):
        response = self.client.get(f"/people/findGrandfather/{10001}/")
        self.assertEqual(response.status_code, 200)
    
    def test_findSiblings(self):
        response = self.client.get(f"/people/findSiblings/{10001}/")
        self.assertEqual(response.status_code, 200)
        
        
        
        
        
    