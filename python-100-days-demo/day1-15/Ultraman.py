from abc import ABCMeta,abstractmethod
from random import randint,randrange

class Fighter(object, metaclass=ABCMeta):
    __slots__ = ('_name', '_hp')

    def __init__(self, name, hp):
        self._name = name
        self._hp = hp

    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        self._hp = hp if hp >=0 else 0

    @property
    def alive(self):
        return self._hp > 0

    @abstractmethod
    def attack(self, other):
        pass

class Ultraman(Fighter):
    __slots__ = ('_name', '_hp', '_mp')

    def __init__(self,name,hp,mp):
        super().__init__(name,hp)
        self._mp = mp

    def attack(self, other):
        other.hp -= randint(1,25)

    def huge_attack(self,other):
        if self._mp >=50:
            self._mp -= 50
            limit = other.hp *3//4
            other.hp -= limit if limit >=50 else limit
            return True
        else:
            self.attack(other)
            return False

    def magic_attack(self, others):
        if self._mp >=20:
            self._mp -= 20
            for monster in others:
                if monster.alive:
                    monster.hp -= randint(10,15)
            return True
        else:
            return False

    def resume(self):
        self._mp -= randint(1,10)
        return self._mp

    def __str__(self):
        return """{}奥特曼
        生命值：{}
        魔法值：{}
        """.format(self._name,self._hp,self._mp)

class monsters(Fighter):
    __slots__ = ('_name', '_hp')
    def attack(self, other):
        other.hp -= randint(1,25)

    def __str__(self):
        return """{}小怪兽
                生命值：{}
                """.format(self._name, self._hp)

def is_any_alive(others):
    for other in others:
        if other.alive > 0:
            return True
    return False

# def select_an_monster(monsters):
#     """选中一只活着的小怪兽"""
#     monsters_len = len(monsters)
#     while True:
#         index = randrange(monsters_len)
#         monster = monsters[index]
#         if monster.alive > 0:
#             return monster
def select_an_monster(others):

    while True:
        index = randrange(len(others))
        monsters = others[index]
        if monsters.alive > 0:
            return monsters

def display_infos(other1, other2):
    print(other1)
    for other in other2:
        print(other,end='')


def main():
    u = Ultraman('lin',1000,100)
    m1 = monsters('xxx',1)
    m2 = monsters('ooo', 1)
    ms = [m1, m2]
    fight_round = 1
    while u.alive and is_any_alive(ms):
        print("========第{}回合========".format(fight_round))
        fight_module = randint(1,10)
        m = select_an_monster(ms)
        if fight_module <= 6:
            if u.attack(m):
                print('{}attack '.format(u.name))
        elif fight_module <=9:
            u.magic_attack(ms)
        else:
            u.huge_attack(m)
        if m.alive:
            m.attack(u)
        display_infos(u, ms)
        fight_round += 1
    if u.alive:
        print("ultraman win")
    else:
        print("monster win")


if __name__ == '__main__':
    main()



