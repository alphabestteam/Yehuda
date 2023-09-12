
class Hero:
    def __init__(self, name_hero:str)->None:
        self._name_hero = name_hero
        self._hp= 10
        self._hp_max =10
        self._damage = 2
        self._level = 1
        self._coins =0
        
    life_percent =30
    level_percent =20
    k = 2
            
    @property
    def name_hero(self):
        return self._name_hero
    
    @name_hero.setter  
    def name_hero(self, x:str):
        self._name_hero = x
        
    @property
    def hp(self):
        return self._hp
    
    @hp.setter  
    def hp(self, x:int):
        self._hp = x
    @property
    def hp_max(self):
        return self._hp_max
    
    @hp_max.setter  
    def hp_max(self, x:int):
        self._hp_max = x
    @property
    def damage(self):
        return self._damage
    
    @damage.setter  
    def damage(self, x:int):
        self._damage = x
    @property
    def level(self):
        return self._level
    
    @level.setter  
    def level(self, x:int):
        self._level = x
    @property
    def coins(self):
        return self._coins
    
    @coins.setter  
    def coins(self, x:int):
        self._coins = x
    
    
    def heal(self):
        h =self.hp+(Hero.life_percent/100)*self.hp        
        if h>=self.hp_max:
            self.hp = self.hp_max
            print("new you hp is max: ",self.hp)
        else:
            self.hp = h
            print("your life is :",self.hp)
            
    def level_up(self):
        if Hero.k*(self.level+1)<=self.coins:
            self.coins-=Hero.k*(self.level+1)
            self.level += 1
            self.damage += Hero.level_percent/100*self.damage
            self.hp = self.hp_max+((Hero.level_percent/100)*self.hp_max)
            self.hp_max = self.hp_max+((Hero.level_percent/100)*self.hp_max)
            print("hero is leveling up to ",self.level)
        else:
            print("the hero cant leveling up")
            
    def attack(self,monster):
        print("hero attack")
        monster.reduce_health(self)
        
    def defend(self):
        print("hero defend")
        return True
    
    
    defended = defend
    
    def reduce_health(self, monster):
        if Hero.defended == True:
            print("hero is defended 20%")
            self.hp -= 80/100*monster.damage
            print("the hp:",self.hp) 
        else:
            self.hp -= monster.damage
            print(f"Injured hero dropped to hp")
        Hero.defended = False
        if self.hp<=0:
            self.hp =0
        print("hero hp is :",self.hp)
        
    def increase_coins(self,coins):
        self.coins += coins
        
    
    
        
            
        
        

            
    