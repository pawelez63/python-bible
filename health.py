import random

health = 50

difficulty = 1

potion_health = random.randint(25,50) / difficulty

health = health + potion_health

print(health)
