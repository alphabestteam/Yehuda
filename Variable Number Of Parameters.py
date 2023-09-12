#1. to get more flax in python for example why do we need that is print() that way we can add who match word number that we want
#2 if you use *args in func the func can get endless vars if you print(args) you get tuple
#3 is like args except is save it in dict 
#4 is tuple and is dict and yes you can use them together
#5 unpacking is take this and make a lot of arguments and packing is make this one argument
def Unpacking(a, b):
    print(a, b)
d = {'a':2, 'b':4}
Unpacking(**d)

def packing(**kwargs) :
    print(kwargs)
packing( a =  "asdas",b ="sdfg" )

def words_length(*word):
    length=0
    for i in word:
        length += len(i)
    print(length)
words_length("hey","hey")

def total_age(**age):
    print(age)
    sum =0
    for x in age:
        sum += age[x]
    print(sum)
total_age(age1 = 12 , age2= 18)
    
