# import json

import pandas as pd
import numpy as np

# obj = '''
#     {"name": "Wes",
#      "places_lived": ["United States", "Spain", "Germany"],
#      "pet": null,
#      "siblings": [{"name": "Scott", "age": 30, "pets": ["Zeus", "Zuko"]},
#                   {"name": "Katie", "age": 38,
#                    "pets": ["Sixes", "Stache", "Cisco"]}]
# } '''
# result = json.loads(obj)
# asjson = json.dumps(result)
# siblings = pd.DataFrame(result['siblings'], columns=['name', 'age'])
# data = pd.read_json('examples/example.json')

# url = 'https://api.github.com/repos/pandas-dev/pandas/issues'
# resp = requests.get(url)
# print(resp)
# data = pd.Series([1, np.nan, 3.5, np.nan, 7])
# df = pd.DataFrame([[1., 6.5, 3.], [1., np.nan, np.nan], [np.nan, np.nan, np.nan], [np.nan, 6.5, 3.]])
# df = pd.DataFrame(np.random.randn(6, 3))
# data = pd.DataFrame({'k1': ['one', 'two'] * 3 + ['two'], 'k2': [1, 1, 2, 3, 3, 4, 4]})
# data = pd.DataFrame({'food': ['bacon', 'pulled pork', 'bacon', 'Pastrami', 'corned beef', 'Bacon', 'pastrami', 'honey ham', 'nova lox'], 'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})
# meat_to_animal = {
#     'bacon': 'pig',
#     'pulled pork': 'pig',
#     'pastrami': 'cow',
#     'corned beef': 'cow',
#     'honey ham': 'pig',
#     'nova lox': 'salmon'
# }
# lowercased = data['food'].str.lower()
# lowercased.map(meat_to_animal)
# data['food'].map(lambda x: meat_to_animal[x.lower()])
#
# data = pd.Series([1., -999., 2., -999., -1000., 3.])
# data.replace([-999, -1000], np.nan)
#
# data = pd.DataFrame(np.arange(12).reshape((3, 4)), index=['Ohio', 'Colorado', 'New York'], columns=['one', 'two', 'three', 'four'])
# transform = lambda x: x[:4].upper()
# data.index.map(transform)
# data.rename(index=str.title, columns=str.upper)
# ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
# bins = [18, 25, 35, 60, 100]
# cats = pd.cut(ages, bins)
# group_names = ['Youth', 'YoungAdult', 'MiddleAged', 'Senior']
# pd.cut(ages, bins, labels=group_names)


# data = {'Dave': 'dave@google.com', 'Steve': 'steve@gmail.com', 'Rob': 'rob@gmail.com', 'Wes': np.nan}
# data = pd.Series(data)

# ind = [['a', 'a', 'a', 'b', 'b', 'c', 'c', 'd', 'd'], [1, 2, 3, 1, 3, 1, 2, 2, 3]]
#
# data = pd.Series(np.random.randn(9), index=ind)
#
# frame = pd.DataFrame(np.arange(12).reshape((4, 3)), index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]], columns=[['Ohio', 'Ohio', 'Colorado'], ['Green', 'Red', 'Green']])
# frame2 = pd.DataFrame({'a': range(7), 'b': range(7, 0, -1), 'c': ['one', 'one', 'one', 'two', 'two', 'two', 'two'], 'd': [0, 1, 2, 0, 1, 2, 3]})
# df1 = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'], 'data1': range(7)})
# df2 = pd.DataFrame({'key': ['a', 'b', 'd', 'd'], 'data2': range(4)})
#
# left1 = pd.DataFrame({'key': ['a', 'b', 'a', 'a', 'b', 'c'],
#                       'value': range(6)})
# right1 = pd.DataFrame({'group_val': [3.5, 7]}, index=['a', 'b'])
# left1.join(right1, on='key')
#
# left2 = pd.DataFrame([[1., 2.], [3., 4.], [5., 6.]],
#                      index=['a', 'c', 'e'],
#                      columns=['Ohio', 'Nevada'])
#
# right2 = pd.DataFrame([[7., 8.], [9., 10.], [11., 12.], [13, 14]],
#                       index=['b', 'c', 'd', 'e'],
#                       columns=['Missouri', 'Alabama'])
# pd.merge(left2, right2, left_index=True, right_index=True, how='outer')
# left2.join(right2, how='outer')

# #############################################################################
# stack: columns in the data to the rows
# unstack: from the rows into the columns
data = pd.DataFrame(np.arange(6).reshape(2, 3),
                    index=pd.Index(['Ohio', 'Colorado'], name='state'),
                    columns=pd.Index(['one', 'two', 'three'], name='number'))
result = data.stack()
result.unstack()

s1 = pd.Series([0, 1, 2, 3], index=['a', 'b', 'c', 'd'])
s2 = pd.Series([4, 5, 6], index=['c', 'd', 'e'])

data2 = pd.concat([s1, s2], keys=['one', 'two'])
data2.unstack()

# MultiIndex(levels=[['one', 'two'], ['a', 'b', 'c', 'd', 'e']],labels=[[0, 0, 0, 0, 1, 1, 1], [0, 1, 2, 3, 2, 3, 4]])
# levels和labels对应关系 [['one'->0, 'two'->1], ['a'->0, 'b'->1, 'c'->2, 'd'->3, 'e'->4]]
# labels,指定了levels间对应关系，labels=[第一列[0->'one', 0, 0, 0, 1->'two', 1, 1], 第二列[0->'a', 1->'b', 2->'c', 3->'d', 2->'c', 3->'d', 4->'e']])
# 可以调整labels的对应关系，则数据展示顺序会变
# 参考https://www.cnblogs.com/shigubuhua/p/8459125.html
# one  a    0
#      b    1
#      c    2
#      d    3
# two  c    4
#      d    5
#      e    6
print(data2.index)
