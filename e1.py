class Student(object):
    lvl = 2
    type = 'ученик'

    def __init__(self, name, surname, strange):
        self.name = name
        self.surname = surname
        self.strange = strange


class Parent(Student):
    lvl = 1
    type = 'родитель'


class Teacher(Student):
    lvl = 3
    type = 'студент'


class Director(Student):
    lvl = 4
    type = 'директор'


class Act(object):
    lvl = 1
    type = 'актовый зал'

    def __init__(self, number):
        self.number = number


class Lessons(Act):
    lvl = 2
    type = 'кабинет для занятий'


class Teachroom(Act):
    lvl = 2
    type = 'учительская'

class Dirroom(Act):
    lvl = 4
    type = 'кабинет директора'


def WriteUser(user):
    print(user.type, "-", user.name, user.surname, '-', user.strange)


def WriteRoom(room):
    print(room.type, '-', room.number)

def Prov(user, room):
    print(user.type, user.name, user.surname, 'пытается войти в', room.type, room.number, ': ', end="")
    if user.lvl >= room.lvl:
        print('успеx')
    else:
        print('неуспех')


user1 = Student('Епишенков', 'Кирилл', 'любит носить треугольку')
user2 = Student('Иван', 'Даркхольм', 'любит носить кожу')
user3 = Parent('Гамаз', 'Иван', 'умеет чинить компьютеры')
user4 = Teacher('Медисон', 'Илья', 'состоит в ЛДПР')
user5 = Teacher('Хованский', 'Юрий', 'состоял в ЛДПР')
user6 = Director('Цаль', 'Виталий', 'аскет')
users = [user1, user2,  user3,  user4,  user5,  user6]
for i in users:
    WriteUser(i)
print()
room1 = Act("1")
room2 = Lessons("6")
room3 = Lessons("7")
room4 = Teachroom('3')
room5 = Teachroom('4')
room6 = Dirroom("2")
rooms = [room1, room2, room3, room4, room5, room6]
for i in rooms:
    WriteRoom(i)
print()
for i in rooms:
    Prov(user3, i)
print()
for i in users:
    Prov(i, room1)
print()
Prov(user2, room6)
Prov(user6, room2)