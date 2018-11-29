import collections
import datetime

ImmutableThingTuple = collections.namedtuple("ImmutableThingTuple", "a b c d")


class MutableThing:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d


class ImmutableThing:
    __slots__ = ['_a', 'b', 'c', 'd']

    def __init__(self, a, b, c, d):
        self._a = a
        self.b = b
        self.c = c
        self.d = d

    @property
    def a(self):
        return self._a


print("Uncomment just 1 of these 4 loops below")
print("after the program pauses on input, check the process memory")

count = 1000000
print("Working with {:,} instances.".format(count))
data = []

t0 = datetime.datetime.now()

# Loop 1: Tuples
# print("tuple")
# for n in range(count):
#     data.append((1 + n, 2 + n, 3 + n, 4 + n))

# Loop 2: Named tuple
# print("named tuple")
# for n in range(count):
#     data.append(ImmutableThingTuple(1 + n, 2 + n, 3 + n, 4 + n))

# Loop 3: Standard mutable class
# print("standard class")
# for n in range(count):
#     data.append(MutableThing(1 + n, 2 + n, 3 + n, 4 + n))

# Loop 4: Slot based immutable class
print("slot based class")
for n in range(count):
    data.append(ImmutableThing(1 + n, 2 + n, 3 + n, 4 + n))

t1 = datetime.datetime.now()

input("Finished, waiting... done in {:,} s".format((t1 - t0).total_seconds()))
