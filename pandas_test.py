import numpy as np
import pandas as pd

# from pandas import Series, DataFrame

# obj = pd.Series([4, 5, 6, -7])
# print(obj)
# print(obj.index)
# print(obj.values)


# obj2 = pd.Series([4, 5, 6, 8], ['d', 'c', 'b', 'a'])
# obj2['c'] = 6
#
# print(obj2)
# print('c' in obj2)


# dictData = {'beijing': 35000, 'shanghai': 30000, 'hangzhou': 50000, 'shenzhen': 20000}
# obj3 = pd.Series(dictData)
# print(obj3)
# print(type((4, 5, 6, -7)))

# Series
obj = pd.Series([4, 7, -5, 3])
print(obj)
print(obj.values)
obj.index = ['Bob', 'Steve', 'Jeff', 'Ryan']
print(obj)

print('#' * 50)

obj2 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
print(obj2)
print(obj2['a'])

# obj2['d'] = 6
obj2.a = 10

print(obj2.a)
print(obj2)

print(obj2[obj2 > 4])
obj2 = obj2 * 2

print(obj2)
print('#' * 50)
sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj3 = pd.Series(sdata)
print(obj3)

states = ['California', 'Ohio', 'Oregon', 'Texas']
obj4 = pd.Series(sdata, index=states)
print(obj4)

pd.isnull(obj4)
obj4.isnull()

obj3 + obj4

obj4.name = 'population'
obj4.index.name = 'state'

# DataFrame
print('#' * 50)
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002, 2003],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}

frame = pd.DataFrame(data)
print(frame)
print('#' * 20)
frame = pd.DataFrame(data, columns=['year', 'state', 'pop'])
print(frame)
print(frame.head())

print('#' * 50)
frame2 = pd.DataFrame(data, columns=['year', 'state', 'pop', 'debt'],
                      index=['one', 'two', 'three', 'four', 'five', 'six'])
print(frame2)
print(frame2.columns)
print(frame2['state'])
print(frame2.year)
print(type(frame2.year))

print('#' * 20)

print(frame2.loc['three'])

frame2['debt'] = 16.5
print(frame2)

print('#' * 20)
frame2['debt'] = np.arange(6.)
print(frame2)

print('#' * 20)
val = pd.Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
frame2['debt'] = val
print(frame2)

print('#' * 20)
frame2['eastern'] = frame2.state == 'Ohio'
print(frame2)

print('#' * 20)
print(frame2.columns)
del frame2['eastern']
print(frame2.columns)

print('#' * 50)
pop = {
    'Nevada': {2001: 2.4, 2002: 2.9},
    'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}
}
frame3 = pd.DataFrame(pop)
print(frame3)
print(frame3.values)
# frame3.T
print('#' * 20)
pdata = {
    'Ohio': frame3['Ohio'][:-1],
    'Nevada': frame3['Nevada'][:2]
}
print(pd.DataFrame(pdata))

print('#' * 50)
print('Essential Functionality')
print('#' * 20)
print('Reindexing')
obj = pd.Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
print(obj)
print()
obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])
print(obj2)

print('#' * 20)
obj3 = pd.Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
print(obj3)
print(obj3.reindex(range(6), method='ffill'))

print('#' * 20)
frame = pd.DataFrame(np.arange(9).reshape((3, 3)),
                     index=['a', 'c', 'd'],
                     columns=['Ohio', 'Texas', 'California'])
print(frame)
frame2 = frame.reindex(['a', 'b', 'c', 'd'])
print()
print(frame2)

states = ['Texas', 'Utah', 'California']
print(frame.reindex(columns=states))
print('#' * 20)
print('Dropping Entries from an Axis')
print('#' * 20)
obj = pd.Series(np.arange(5.), index=['a', 'b', 'c', 'd', 'e'])
print(obj)
new_obj = obj.drop('c')
print(new_obj)

print('#' * 20)
data = pd.DataFrame(np.arange(16).reshape((4, 4)),
                    index=['Ohio', 'Colorado', 'Utah', 'New York'],
                    columns=['one', 'two', 'three', 'four'])
print(data)
data.drop(['Colorado', 'Ohio'])
data.drop('two', axis=1)
data.drop(['two', 'four'], axis='columns')

print('#' * 20)
print('Indexing, Selection, and Filtering')
print('#' * 20)

obj = pd.Series(np.arange(4.), index=['a', 'b', 'c', 'd'])
print(obj)
print(obj['b'])
print(obj[1])
print(obj[2:4])
print(obj[['a', 'b', 'd']])
print(obj[[1, 3]])
print(obj[obj < 2])

data = pd.DataFrame(np.arange(16).reshape((4, 4)),
                    index=['Ohio', 'Colorado', 'Utah', 'New York'],
                    columns=['one', 'two', 'three', 'four'])
print(data)
# data['two']
# data[['three', 'one']]

# data[:2]
# data[data['three'] > 5]
# data[data < 5] = 0
# data.loc['Colorado', ['two', 'three']]
# data.iloc[2, [3, 0, 1]]
# data.iloc[[1, 2], [3, 0, 1]]
# data.loc[:'Utah', 'two']
# data.iloc[:, :3][data.three > 5]

print('#' * 50)
print('#' * 20)
s1 = pd.Series([7.3, -2.5, 3.4, 1.5], index=['a', 'c', 'd', 'e'])
s2 = pd.Series([-2.1, 3.6, -1.5, 4, 3.1], index=['a', 'c', 'e', 'f', 'g'])
print(s1 + s2)

print('#' * 20)
df1 = pd.DataFrame(np.arange(9.).reshape((3, 3)), columns=list('bcd'), index=['Ohio', 'Texas', 'Colorado'])
df2 = pd.DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'), index=['Utah', 'Ohio', 'Texas', 'Oregon'])
arr = np.arange(12.).reshape((3, 4))
