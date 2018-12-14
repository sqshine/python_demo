import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime

# data = np.arange(10)
# print(data)
# plt.plot(data)
# plt.show()

# Figures and Subplots
# fig = plt.figure()
# ax1 = fig.add_subplot(2, 2, 1)
# ax2 = fig.add_subplot(2, 2, 2)
# ax3 = fig.add_subplot(2, 2, 3)
# plt.plot(np.random.randn(50).cumsum(), 'k--')
# _ = ax1.hist(np.random.randn(100), bins=20, color='k', alpha=0.3)
# ax2.scatter(np.arange(30), np.arange(30) + 3 * np.random.randn(30))

# fig, axes = plt.subplots(2, 2, sharex=True, sharey=True)
# for i in range(2):
#     for j in range(2):
#         axes[i, j].hist(np.random.randn(500), bins=50, color='k', alpha=0.5)
# plt.subplots_adjust(wspace=0, hspace=0)

# Colors, Markers, and Line Styles

# plt.plot(np.random.randn(30).cumsum(), 'ko--')
# # plt.plot(np.random.randn(30).cumsum(), color='k', linestyle='dashed', marker='o')


# Setting the title, axis labels, ticks, and ticklabels

# fig = plt.figure()
# ax = fig.add_subplot(1, 1, 1)
# ax.plot(np.random.randn(1000).cumsum())
# ticks = ax.set_xticks([0, 250, 500, 750, 1000])
# labels = ax.set_xticklabels(['one', 'two', 'three', 'four', 'five'], rotation=30, fontsize='small')
# # ax.set_title('My first matplotlib plot')
# # ax.set_xlabel('Stages')
# props = {
#     'title': 'My first matplotlib plot',
#     'xlabel': 'Stages',
#     'ylabel': 'y-label'
# }
# ax.set(**props)


# Adding legends

# fig = plt.figure()
# ax = fig.add_subplot(1, 1, 1)
# ax.plot(np.random.randn(1000).cumsum(), 'k', label='one')
# ax.plot(np.random.randn(1000).cumsum(), 'k--', label='two')
# ax.plot(np.random.randn(1000).cumsum(), 'k.', label='three')
# ax.legend(loc='best')


# Annotations and Drawing on a Subplot

# fig = plt.figure()
# ax = fig.add_subplot(1, 1, 1)
# data = pd.read_csv('examples/spx_less.csv', index_col=0, parse_dates=True)
# spx = data['SPX']
# # data.plot(ax=ax, style='k-')
# spx.plot(ax=ax, style='k-')
# crisis_data = [
#     (datetime(2007, 10, 11), 'Peak of bull market'),
#     (datetime(2008, 3, 12), 'Bear Stearns Fails'),
#     (datetime(2008, 9, 15), 'Lehman Bankruptcy')
# ]
# for date, label in crisis_data:
#     ax.annotate(label, xy=(date, spx.asof(date) + 75),
#                 xytext=(date, spx.asof(date) + 225),
#                 arrowprops=dict(facecolor='black', headwidth=4, width=2, headlength=4),
#                 horizontalalignment='left', verticalalignment='top')
# # Zoom in on 2007-2010
# ax.set_xlim(['1/1/2007', '1/1/2011'])
# ax.set_ylim([600, 1800])
# ax.set_title('Important dates in the 2008-2009 financial crisis')
# # plt.savefig('financial.svg', dpi=400, bbox_inches='tight')  # Saving Plots to File

# matplotlib Configuration

# plt.rc('figure', figsize=(10, 10))
# font_options = {'family': 'monospace',
#                 'weight': 'bold',
#                 'size': 'small'}
# plt.rc('font', **font_options)


# Plotting with pandas and seaborn

# Line Plots
# s = pd.Series(np.random.randn(10).cumsum(), index=np.arange(0, 100, 10))
# s.plot()
#
# df = pd.DataFrame(np.random.randn(10, 4).cumsum(0), columns=['A', 'B', 'C', 'D'], index=np.arange(0, 100, 10))
# df.plot.line()

# Bar Plots
# fig, axes = plt.subplots(2, 1)
# data = pd.Series(np.random.rand(16), index=list('abcdefghijklmnop'))
# data.plot.bar(ax=axes[0], color='k', alpha=0.7)
# data.plot.barh(ax=axes[1], color='k', alpha=0.7)
#
# df = pd.DataFrame(np.random.rand(6, 4),
#                   index=['one', 'two', 'three', 'four', 'five', 'six'],
#                   columns=pd.Index(['A', 'B', 'C', 'D'], name='Genus'))
# ax = df.plot.bar()
# ax.legend(loc='best')
# df.plot.barh(stacked=True, alpha=0.5)

plt.show()
