import re

# p = re.compile(r'(\d+)-(\d+)-(\d+)')
# print(p.match('2018-10-18'))
# year, month, day = p.match('2018-10-18').groups()
# print(year)
# print(p.match('2018-10-18').groupdict())
# print(p.match('2018-10-18').group())

# print(p.search('aaa2018-10-18ddd2018-10-18').group())
# print(p.search('aaa2018-10-18ddd'))


text = """Dave dave@google.com
    Steve steve@gmail.com
    Rob rob@gmail.com
    Ryan ryan@yahoo.com
    """
pattern = r'[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}'
regex = re.compile(pattern, flags=re.IGNORECASE)
print(regex.findall(text))
m = regex.search(text)
print(text[m.start():m.end()])

print(regex.match(text))
print(regex.sub('REDACTED', text))

pattern = r'([A-Z0-9._%+-]+)@([A-Z0-9.-]+)\.([A-Z]{2,4})'
regex = re.compile(pattern, flags=re.IGNORECASE)

m = regex.match('wesm@bright.net')
print(m.groups())
print(regex.findall(text))
print(regex.sub(r'Username: \1, Domain: \2, Suffix: \3', text))
