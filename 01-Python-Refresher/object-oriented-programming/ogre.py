"""
OGRE CLASS INHERITED FROM ENEMY
"""
import random
from enemy import *

class Ogre(Enemy):
    def __init__(self, health_points:int=10, attack_damage:int=1):
        super().__init__(
            type_of_enemy="Ogre",
            health_points=health_points,
            attack_damage=attack_damage
        )

    def talk(self):
        print("Ogre is slamming hands all around!")

    def special_attack(self):
        did_special_attack_work = random.random() < 0.20
        if did_special_attack_work:
            self.attack_damage += 4
            print("Ogre gets angry and increases attack by 4")