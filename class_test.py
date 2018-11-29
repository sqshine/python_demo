class Monster:
    """define a Monster class"""

    def __init__(self, hp=100):
        self.hp = hp

    def run(self):
        print('Monster(hp=%s)移动到某个位置' % self.hp)

    def whoami(self):
        print('我是怪物之父')

    def __str__(self):
        return 'Monster(hp=%s)' % self.hp

    __repr__ = __str__


class Animals(Monster):
    """define a normal Monster"""

    def __init__(self, hp=10):
        super().__init__(hp)


class Boss(Monster):
    """Boss Monster"""

    def whoami(self):
        print('我是怪物BOSS')


monster = Monster(100)

print(monster)
# print(monster.hp)
# monster.run()
# monster.whoami()
#
# animal = Animals()
# print(animal.hp)
# animal.run()
#
# boss = Boss(200)
# print(boss.hp)
# boss.run()
# boss.whoami()
print(type(Monster))
print(type(monster))
