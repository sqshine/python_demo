import os

with open('hello.py', 'r') as f:
    s = f.read()
    print(s)
    for line in f.readlines():
        print(line.strip())

print(os.environ)
