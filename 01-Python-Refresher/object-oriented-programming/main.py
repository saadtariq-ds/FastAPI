"""
MAIN FILE
"""

from enemy import *
from zombie import *
from ogre import *

def battle(enemy1: Enemy, enemy2: Enemy
           ):
    enemy1.talk()
    enemy2.talk()

    while enemy1.health_points > 0 and enemy2.health_points > 0:
        print("*************")
        enemy1.special_attack()
        enemy2.special_attack()
        print(f"{enemy1.get_type_of_enemy()}: {enemy1.health_points} Health Points Left")
        print(f"{enemy2.get_type_of_enemy()}: {enemy2.health_points} Health Points Left")

        enemy2.attack()
        enemy1.health_points -= enemy2.attack_damage

        enemy1.attack()
        enemy2.health_points -= enemy1.attack_damage

    print("***********")

    if enemy1.health_points > 0:
        print(f"{enemy1.get_type_of_enemy()} Wins")
    else:
        print(f"{enemy2.get_type_of_enemy()} Wins")



zombie = Zombie(attack_damage=1, health_points=10)
ogre = Ogre(attack_damage=3, health_points=20)

battle(enemy1=zombie, enemy2=ogre)
