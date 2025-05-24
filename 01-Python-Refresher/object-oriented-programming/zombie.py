"""
ZOMBIE CLASS INHERITED FROM ENEMY
"""
from enemy import *


class Zombie(Enemy):
    def __init__(self, health_points:int=10, attack_damage:int=1):
        super().__init__(
            type_of_enemy="Zombie",
            health_points=health_points,
            attack_damage=attack_damage
        )

    def talk(self):
        print("***Grumbling...***")

    def spread_disease(self):
        print("The Zombie is trying to spread infection")