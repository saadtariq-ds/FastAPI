"""
OGRE CLASS INHERITED FROM ENEMY
"""

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