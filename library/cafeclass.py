"""Задание
Создайте небольшую программу для сети кофеен. Программа должна вычислять
стоимость заказанного кофе с учетом возможных добавок (сахара, молока, взбитых
сливок). Например, эспрессо с сахаром или американо с сахаром, молоком и взбитыми
сливками.
В программе обязательно должны быть реализованы следующие классы:
• класс Coffee – базовый класс для напитка. Должен содержать метод
getCost(), который будет возвращать стоимость напитка, и метод
getDescription(), который будет возвращать описание напитка.
• класс Espresso
• класс Americano
• класс DarkRoast
• класс Milk
• класс Sugar
• класс Whip
Перегрузите магические методы str и repr. Поддержите
возможность выводить информацию о заказе в файл."""


class Coffee:
    cost = 0
    description = []

    # def __init__(self):
    #     # self.cost=cost
    #     self.ingr = []

    # def getCost(self):

    def getDescription(self):
        return self.description


    def getCost(self):
        # self.cost +=self.cost
        return self.cost

    def append_ingr(self, ingrid):
        return self.description.append(ingrid)

    def __str__(self):
        return f'{self.description}-{self.cost}'

    # def __repr__(self):
    #     return f'{self.description}-{self.cost}'



class Espresso(Coffee):
    name ='Espresso'
    def __init__(self):
        self.cost = 5

    # def __str__(self):
    #     return self.name

class Americano(Coffee):
    name = 'Americano'
    cost = 15


class DarkRoast(Coffee):
    name='DarkRoast'
    cost = 25



class Milk:
    name = 'Milk'
    cost = 10
    def __str__(self):
        return f'{self.name}'

class Sugar:
    name='Sugar'
    cost = 13


class Whip:
    name='Whip'
    cost = 18


# p=Espresso()
b={1: Espresso(),2:Americano(),3:DarkRoast()}
ingr = {1: Milk(), 2: Sugar(), 3: Whip()}
for i in range(1,len(b)+1):
    print(f'{i}.{b[i].name}  ')
a = int(input(f'Выберите кофе (Ввести цифру):'))
b[a].append_ingr(b[a].name)
bool_flag=input('Будем заказывать ингридиенты (да/нет)?:')


while bool_flag.lower()=='да':

    for i in range(1, len(b) + 1):
        print(f'{i}.{ingr[i].name}')
    d = int(input('Выберите ингридиент(Ввести цифру):'))



    b[a].append_ingr(ingr[d].name)
    b[a].cost=b[a].cost+ingr[d].cost

    bool_flag=input('Еще добавим ингридиентов (да/нет)?:')


print(b[a])
#
# with open('coffee.txt', 'w') as f:
#     for i in range(len(b))
#     f.write(b[a])




# class Pizza(object):
#     def prepare(self):
#         print('prepare pizza')
#
#     def bake(self):
#         print('bake pizza')
#
#     def cut(self):
#         print('cut pizza')
#
#     def box(self):
#         print('box pizza')
#
#
# class CheesePizza(Pizza):
#     def __init__(self):
#         self.name = "cheese pizza"
#
#
# class ClamPizza(Pizza):
#     def __init__(self):
#         self.name = "clam pizza"
#
#
# class VeggiePizza(Pizza):
#     def __init__(self):
#         self.name = "veggie pizza"
#
#
# class SimplePizzaFactory(object):
#     def create_pizza(self, type):
#         pizza = None
#
#         if type == "cheese":
#             pizza = CheesePizza()
#         elif type == "clam":
#             pizza = ClamPizza()
#         elif type == "veggie":
#             pizza = VeggiePizza()
#
#         return pizza
#
#
# class PizzaStore(object):
#     def __init__(self, factory):
#         self.factory = factory
#
#     def order_pizza(self, type):
#         pizza = self.factory.create_pizza(type)
#         pizza.prepare()
#         pizza.bake()
#         pizza.cut()
#         pizza.box()
#         return pizza
#
#
# if __name__ == "__main__":
#     store = PizzaStore(SimplePizzaFactory())
#     pizza = store.order_pizza('clam')
#     print(pizza.name)
