import pandas as pd

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

data = {
    'city': ['shanghai', 'shanghai', 'shanghai', 'beijing', 'beijing'],
    'year': [2016, 2017, 2018, 2018, 2017],
    'pop': [1.5, 1.6, 1.7, 1.8, 1.9]
}
frame = pd.DataFrame(data)

print(frame)
