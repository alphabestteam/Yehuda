import random
from hero import Hero


class Monster:
    def __init__(self, name_monster: str, hero_level) -> None:
        self._name_monster = name_monster
        if hero_level == 1:
            self._level = random.randint(hero_level, hero_level + 1)
        else:
            self._level = random.randint(hero_level - 1, hero_level + 1)
        self._damage = 1.2 * self.level
        self._hp = 5 * self.level
        self._hp_max = 6 * self.level

    life_percent = 30
    level_percent = 20
    k = 5

    @property
    def name_monster(self):
        return self._name_monster

    @name_monster.setter
    def name_monster(self, x: str):
        self._name_monster = x

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, x: int):
        self._hp = x

    @property
    def hp_max(self):
        return self._hp_max

    @hp_max.setter
    def hp_max(self, x: int):
        self._hp_max = x

    @property
    def damage(self):
        return self._damage

    @damage.setter
    def damage(self, x: int):
        self._damage = x

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, x: int):
        self._level = x

    @property
    def coins(self):
        return self._coins

    @coins.setter
    def coins(self, x: int):
        self._coins = x

    def attack(self, hero: Hero):
        hero.reduce_health(self)
        print("monster attack !")

    def reduce_health(self, hero: Hero):
        self.hp -= hero.damage
        if self.hp < 0:
            self.hp = 0
        print("monster hp is:", self.hp)
