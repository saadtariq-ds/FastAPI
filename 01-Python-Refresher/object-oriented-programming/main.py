"""
MAIN FILE
"""

from enemy import *

zombie = Enemy(type_of_enemy="Zombie", attack_damage=1, health_points=10)
big_zombie = Enemy(type_of_enemy="Big Zombie", attack_damage=3, health_points=15)

print(zombie.health_points)
print(big_zombie.health_points)

print(zombie.get_type_of_enemy())
print(big_zombie.get_type_of_enemy())
