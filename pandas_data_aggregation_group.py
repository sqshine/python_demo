import pandas as pd
import numpy as np
from datetime import datetime
from datetime import timedelta
from dateutil.parser import parse

# df = pd.DataFrame({'key1': ['a', 'a', 'b', 'b', 'a'],
#                    'key2': ['one', 'two', 'one', 'two', 'one'],
#                    'data1': np.arange(5),
#                    'data2': np.arange(5, 10)})

# grouped = df['data1'].groupby(df['key1'])
# grouped.mean()

# means = df['data1'].groupby([df['key1'], df['key2']]).mean()
# means.unstack()

# states = np.array(['Ohio', 'California', 'California', 'Ohio', 'Ohio'])
# years = np.array([2005, 2005, 2006, 2005, 2006])
# df['data1'].groupby([states, years]).mean()
# df.groupby('key1').mean()
# df.groupby(['key1', 'key2']).mean()
# df.groupby(['key1', 'key2']).size()

# Iterating Over Groups
# for name, group in df.groupby('key1'):
#     print(name)
#     print(group)
# pieces = dict(list(df.groupby('key1')))
# print(pieces['b'])
# print(df.dtypes)
# grouped = df.groupby(df.dtypes, axis=1)
# for dtype, group in grouped:
#     print(dtype)
#     print(group)

# Selecting a Column or Subset of Columns
# d_grouped = df.groupby(['key1', 'key2'])[['data2']]  # return DataFrameGroupBy
# d_grouped.mean()  # return DataFrame
# s_grouped = df.groupby(['key1', 'key2'])['data2']  # return SeriesGroupBy
# s_grouped.mean()  # return Series


# Grouping with Dicts and Series
# people = pd.DataFrame(np.random.randn(5, 5),
#                       columns=['a', 'b', 'c', 'd', 'e'],
#                       index=['Joe', 'Steve', 'Wes', 'Jim', 'Travis'])
# people.iloc[2:3, [1, 2]] = np.nan
# mapping = {'a': 'red', 'b': 'red', 'c': 'blue',
#            'd': 'blue', 'e': 'red', 'f': 'orange'}
# by_column = people.groupby(mapping, axis=1)
# by_column.sum()
#
# map_series = pd.Series(mapping)
# people.groupby(map_series, axis=1).count()
# now = datetime.now()
#
# delta = datetime(2011, 1, 7) - datetime(2008, 6, 24, 8, 15)
# start = datetime(2011, 1, 7)
# start + timedelta(12)
# stamp = datetime(2011, 1, 3)
# str(stamp)
# stamp.strftime('%Y-%m-%d')
#
# value = '2011-01-03'
# datetime.strptime(value, '%Y-%m-%d')
# datestrs = ['7/6/2011', '8/6/2011']
# [datetime.strptime(x, '%m/%d/%Y') for x in datestrs]
# parse('2011-01-03')
# parse('Jan 31, 1997 10:45 PM')
# parse('6/12/2011', dayfirst=True)
# datestrs = ['2011-07-06 12:00:00', '2011-08-06 00:00:00']
# pd.to_datetime(datestrs)
# idx = pd.to_datetime(datestrs + [None])
#
# dates = [datetime(2011, 1, 2), datetime(2011, 1, 5), datetime(2011, 1, 7), datetime(2011, 1, 8), datetime(2011, 1, 10), datetime(2011, 1, 12)]
# ts = pd.Series(np.random.randn(6), index=dates)
# ts + ts[::2]
# # stamp = ts.index[0]
# stamp = ts.index[2]
# ts[stamp]
# ts['20110110']
# ts['1/10/2011']
#
# longer_ts = pd.Series(np.random.randn(1000),
#                       index=pd.date_range('1/1/2000', periods=1000))
# longer_ts['2001']
# longer_ts['2001-05']
#
# ts[datetime(2011, 1, 7):]
# ts['1/6/2011':'1/11/2011']
#
# ts.truncate(after='2011-01-09')

# dates = pd.date_range('1/1/2000', periods=100, freq='W-WED')
# long_df = pd.DataFrame(np.random.randn(100, 4),
#                        index=dates,
#                        columns=['Colorado', 'Texas', 'New York', 'Ohio'])
# long_df.loc['2001-5']

# dates = pd.DatetimeIndex(['1/1/2000', '1/2/2000', '1/2/2000',
#                           '1/2/2000', '1/3/2000'])
# dup_ts = pd.Series(np.arange(5), index=dates)
# dup_ts.index.is_unique
# dup_ts['1/3/2000']
# dup_ts['1/2/2000']
# grouped = dup_ts.groupby(level=0)
# grouped.mean()
# grouped.count()


# dates = [datetime(2011, 1, 2), datetime(2011, 1, 5), datetime(2011, 1, 7), datetime(2011, 1, 8), datetime(2011, 1, 10), datetime(2011, 1, 12)]
# ts = pd.Series(np.random.randn(6), index=dates)
# resampler = ts.resample('D')
#
# index = pd.date_range('2012-04-01', '2012-06-01')
# pd.date_range(start='2012-04-01', periods=20)
# pd.date_range(end='2012-06-01', periods=20)
# pd.date_range('2000-01-01', '2000-12-01', freq='BM')
# pd.date_range('2012-05-02 12:56:31', periods=5)
# pd.date_range('2012-05-02 12:56:31', periods=5, normalize=True)


# values = pd.Series(['apple', 'orange', 'apple', 'apple'] * 2)
# pd.unique(values)
# pd.value_counts(values)

# values = pd.Series([0, 1, 0, 0] * 2)
# dim = pd.Series(['apple', 'orange'])
# dim.take(values)
# dim.take([0, 1, 0, 0] * 2)

# fruits = ['apple', 'orange', 'apple', 'apple'] * 2
# N = len(fruits)
# df = pd.DataFrame({'fruit': fruits,
#                    'basket_id': np.arange(N),
#                    'count': np.random.randint(3, 15, size=N),
#                    'weight': np.random.uniform(0, 4, size=N)},
#                   columns=['basket_id', 'fruit', 'count', 'weight'])
# fruit_cat = df['fruit'].astype('category')
# c = fruit_cat.values
# c.categories
# c.codes
data = pd.DataFrame({
    'x0': [1, 2, 3, 4, 5],
    'x1': [0.01, -0.01, 0.25, -4.1, 0.],
    'y': [-1.5, 0., 3.6, 1.3, -2.]})
