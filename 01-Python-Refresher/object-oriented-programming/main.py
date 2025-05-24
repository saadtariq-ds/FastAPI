"""
MAIN FILE
"""

from zombie import *
from ogre import *

zombie = Zombie(attack_damage=1, health_points=10)

print(zombie.health_points)


print(zombie.get_type_of_enemy())
print(zombie.talk())
print(zombie.spread_disease())

ogre = Ogre(attack_damage=3, health_points=20)

print(ogre.talk())
print()

print(f"{zombie.get_type_of_enemy()} has {zombie.health_points} health points and attack of {zombie.attack_damage}")
print(f"{ogre.get_type_of_enemy()} has {ogre.health_points} health points and attack of {ogre.attack_damage}")