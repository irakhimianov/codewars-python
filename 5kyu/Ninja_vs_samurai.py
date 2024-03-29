"""
Something is wrong with our Warrior class. All variables should initialize properly
and the attack method is not working as expected.

If properly set, it should correctly calculate the damage after an attack
(if the attacker position is == to the block position of the defender: no damage;
otherwise, the defender gets 10 damage if hit "high" or 5 damage if hit "low".
If no block is set, the defender takes 5 extra damage.

For some reason, the health value is not being properly set.

The following shows an example of this code being used:
ninja = Warrior('Hanzo Hattori')
samurai = Warrior('Ryōma Sakamoto')

samurai.block = 'l'
ninja.attack(samurai, 'h')
# samurai.health should be 90 now

The warrios must be able to fight to the bitter end, and good luck to the most skilled!
Notice that health can't be below 0: once hit to 0 health, a warrior attribute deceased
becomes true; if hit again, the zombie attribute becomes true too!

https://www.codewars.com/kata/517b2bcf8557c200b8000015
"""

Position = {'high': 'h', 'low': 'l'}  # don't change this!


class Warrior:
    def __init__(self, name, block=''):
        # each warrior should be created with a name and 100 health points
        self.name = name
        self.health = 100
        # default guard is "", that is unguarded
        self.block = block
        self.deceased = False
        self.zombie = False

    def attack(self, enemy, position):
        # attacking high deals 10 damage, low 5
        # 0 damage if the enemy blocks in the same position
        damage = 0
        if enemy.block != position:
            damage = 10 if position == Position['high'] else 5
        # and even more damage if the enemy is not blocking at all
        if enemy.block == "":
            damage += 5
        enemy.set_health(enemy.health - damage)

    def set_health(self, new_health):
        # health cannot have negative values
        self.health = new_health
        # if a warrior is set to 0 health he is dead
        if self.health <= 0:
            self.deceased = True
        # he would be a zombie only if he was already dead
        if self.health < 0 and self.deceased:
            self.health = 0
            self.zombie = True
