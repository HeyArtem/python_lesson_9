numbers = [1,2,3]
zxc = type(numbers)
print(zxc)

class Character():
    def __init__(self, race, damage = 10, armor = 20):
        self.race = race
        self.damage = damage
        self.armor = armor

unit = Character('Elf', damage=20, armor=40)

print(unit.race)
print(unit.damage)
print(unit.armor)

print()
print('Атрибуты и методы внутри класса')

class Character():
    max_speed = 100
    dead_health = 0

    def __init__(self, race, damage = 10, armor = 20):
        self.race = race
        self.damage = damage
        self.armor = armor
        self.health = 100

    def hit(self, damage): #наношу удары
        self.health -= damage

    def is_dead(self): # что бы понять скалько осталось жизни
        return self.health == Character.dead_health


unit = Character('Ork')
print(unit.race)
print(Character.max_speed)

unit.hit(20) #нанес удар 20
print('unit.health: ', unit.health)

print('unit.is_dead:', unit.is_dead())

unit.hit(80) # наношу удар, добиваю
print('после второго удара --> unit.health: ', unit.health)
print(unit.is_dead()) # получу True- мертв

unit.health = -200 #вручную прописал значение параметра
print('вручную приписанный unit.health: ', unit.health)

print()
print()
print('    Константы. Защищенный и приватные атрибуты')