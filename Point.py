class Point:
    def __init__(self,x,y) -> None:
        self._x =x 
        self._y =y
        
    def __add__(self,obj):
        return self._x+obj._x,self._y+obj._y  
    
    def __eq__(self,obj):
        if (self._x == obj._x) and (self._y == obj._y) :
            return True
        else:
            return False 
    def __str__(self):
        return  f"({self._x},{self._y})"    