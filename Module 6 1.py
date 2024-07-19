class Animal:
    alive = True
    fed = False
    def __init__(self, name):
        self.name = name
    def eat(self, food):
        if food.edible is True:
            print(f'{self.name} съел {food.name}.')
            self.fed = True #c скушал и насытился
        else:
            print(f'{self.name} не стал есть {food.name}.')
            self.alive = False # не съел ничего и умер от голода

class Plant:
    edible = False
    def __init__(self, name):
        self.name = name

class Mammal(Animal):
    pass

class Predator(Animal):
    pass

class Flower(Plant):
    pass

class Fruit(Plant):
    edible = True



if __name__ == '__main__':

    a1 = Predator('Волк с Уолл-Стрит')
    a2 = Mammal('Хатико')
    p1 = Flower('Цветик-семицветик')
    p2 = Fruit('Заводной апельсин')

    print(a1.name)
    print(p1.name)

    print(a1.alive)
    print(a2.fed)
    a1.eat(p1)
    a2.eat(p2)
    print(a1.alive)
    print(a2.fed)






#
# class Animal:
#     alive = True
#     fed = False
#     def __init__(self, name):
#         self.name = name
#     def eat(self, food):
#         #self.food = food.edible #food - это весь класс целиком
#         #if self.food is True:
#         if food.edible is True:
#             print(f'{self.name} съел {food.name}')
#             #print(f'self.fed before eat: {self.fed}')
#             self.fed = True
#             #print(f'self.fed after eat: {self.fed}')
#         else:
#             print(f'{self.name} не стал есть {food.name}')
#             #print(f'fed after not eat: {self.fed}')
#             self.fed = False
#             self.alive = False # не съел ничего и умер от голода
#             #print(f'fed after not eat: {self.fed}')
#
# class Plant:
#     edible = False
#     def __init__(self, name):
#         self.name = name
#
# class Mammal(Animal):
#     pass
#
# class Predator(Animal):
#     pass
#
# class Flower(Plant):
#     pass
#
# class Fruit(Plant):
#     edible = True
#
#
#
# if __name__ == '__main__':
#
#     a1 = Predator('Волк с Уолл-Стрит')
#     a2 = Mammal('Хатико')
#     p1 = Flower('Цветик семицветик')
#     p2 = Fruit('Заводной апельсин')
#
#     print(a1.name)
#     print(p1.name)
#
#     print(f'alive: {a1.alive}')
#     print(f'fed: {a2.fed}')
#     a1.eat(p1)
#     a2.eat(p2)
#     print(f'alive: {a1.alive}')
#     print(f'fed: {a2.fed}')