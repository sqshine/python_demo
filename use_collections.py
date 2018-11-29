from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)
print(p)
print(type(p))
print(isinstance(p, Point))
print(isinstance(p, tuple))
# namedtuple('名称', [属性list]):
Circle = namedtuple('Circle', ['x', 'y', 'r'])

print(''.join(['hello', ' ', '9', '5', '2', '7']))


User = namedtuple('User', ['name', 'age', 'height'])
user_tuple = ('sqshine', 18, 180)
user_list = ['sqshine', 18, 180]
user_dict = {
    'name': 'sqshine',
    'age': 18,
    'height': 180
}

user = User(*user_tuple)
user1 = User(*user_list)
user2 = User(**user_dict)
user3 = User._make(user_dict.values())
user6 = User._make(user_dict)
user4 = User._make(user_list)
user5 = User._make(user_tuple)
print(user.name, user.age, user.height)
print(user1.name, user1.age, user1.height)
print(user2.name, user2.age, user2.height)
print(user3.name, user3.age, user3.height)
print(user6.name, user6.age, user6.height)
print(user4.name, user4.age, user4.height)
print(user5.name, user5.age, user5.height)
