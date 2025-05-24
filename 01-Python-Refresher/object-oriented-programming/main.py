"""
MAIN FILE
"""

from enemy import *
from zombie import *
from ogre import *

def battle(enemy: Enemy):
    enemy.talk()
    enemy.attack()

zombie = Zombie(attack_damage=1, health_points=10)
ogre = Ogre(attack_damage=3, health_points=20)

battle(zombie)
battle(ogre)
