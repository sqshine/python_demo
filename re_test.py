import re

p = re.compile(r'(\d+)-(\d+)-(\d+)')
# print(p.match('2018-10-18'))
# year, month, day = p.match('2018-10-18').groups()
# print(year)
# print(p.match('2018-10-18').groupdict())
# print(p.match('2018-10-18').group())

print(p.search('aaa2018-10-18ddd2018-10-18').group())
print(p.search('aaa2018-10-18ddd'))
