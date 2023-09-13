import time
#1. decorators can change and add on a func to do something else for example func do "hello world" change to "bay world"
#2. you call the func inside func in this way function_to_be_used = hello_decorator(function_to_be_used)
# it will go first inside to hello_decorator than when we call to fun_to_be_used  and than return 
#3. it is func that you import from another file tha you can use for example in dict an when you input 2 number it will return the sum of that numbers
#4. because args is for accepts a variable number of parameters, kwargs give you number of name parameters
#5. when we use getters @property def something(self):return self.x
def cal_time(t):
    def result(*args, **kwargs):
        start = time.time()
        t(*args, **kwargs)
        end = time.time()
        print("is take to us : ", end - start ,"sec")
    return result

@cal_time
def print_something():
    time.sleep(1)
    print("hey how you doing")
 
print_something()
# when we use decorator in class when we make it we need to use __call__ in that way we can use that in some func in  the class


################################################################################################################
#1. this is object that contain endless number of values with that we can over(dict list tuple )
#2. dict list tuple set
#3. it will del this
#4. we use methods __iter__() and __next__().
class People :
    def __init__(self ) -> None:
        self._names =[]
    
    def __iter__(self):
        return self

    def __next__(self):
        try:
            n = self._names[0]
            del self._names[0]
            return n 
        except:
            print("end of the list")
            
    def add_person(self, name):
        self._names.append(name)
           
p= People()
p.add_person("ari")
p.add_person("yehuda")
p.add_person("dan")
iter_p =iter(p)

for _ in range(len(iter_p._names)):
    print(next(iter_p))
    
########################################################################################################
#1. is func that return iterator  is good when we wont large sequence of values
#2. you have more control then regular func  and is good with large sequence of values
#3. because is iterable and you can use expression like  i * i for i in range(5)
#4. yield is used to produce value form generator until the next value is request
#5. 

def fibonacci():
    x = 0
    y = 1
    while True:
        z =x
        x = y
        y = z+y
        yield y

f = fibonacci()
num = int(input("enter number: "))
for _ in range(num):
    print(next(f))





