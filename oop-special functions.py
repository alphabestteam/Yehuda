from Point import Point

# 1. magic functions are __some__that defining objects to be sub plus str pow ect..'__abs__', '__add__', '__and__', '__bool__', 
# 2. it will print to as 0xsdjsdfjsdf and not the string that we wont
# 3. the same he compere the 0xsjdfkdsf and not the string 
# 4. you can use + in int and in str how ?  because you overloaded by int class and str 
# 5.
def with_magic_functions():
    p1 = Point(5,6)
    p2 = Point(5,6)
    
    print(p1==p2)
    print(p1,p2)
    print(p1+p2)
    
#the output is False and Point.Point object at 0x00000227029A4FD0> <Point.Point object at 0x00000227029A4F70>
# and error because cant + two Point

if __name__=="__main__":
    with_magic_functions()