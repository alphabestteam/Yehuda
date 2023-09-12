from monster import Monster
from hero import Hero

def choose_action(monster:Monster,hero:Hero):
    action =int(input("enter 1 - for attack ,enter 2 - for level up , enter 3- for heal, enter 4 - for defend    "))
    if action == 1:
        hero.increase_coins(1)
        hero.attack(monster)
    elif action == 2:
        hero.increase_coins(1)
        hero.level_up()
    elif action == 3:
        hero.heal()
        hero.increase_coins(1)
    elif action == 4:
        hero.defend()
        hero.increase_coins(1)
    else:
        print("pls enter 1 or 2 or 3 or 4")
    

def main():
    h = Hero("yehuda")
    m = Monster("you",h.level)
    while h.hp !=0:
        choose_action(m,h)
        if m.hp ==0:
            m = Monster("you",h.level)
        if m.hp>1:
            m.attack(h)
        if h.hp ==0:
            print("you loser go back to mommy")

    

if __name__ == "__main__":
    main()