import collections
import uuid

Measurement = collections.namedtuple('Measurement', 'id x y value')

measurements = [
    Measurement(str(uuid.uuid4()), 1, 1, 72),
    Measurement(str(uuid.uuid4()), 2, 1, 40),
    Measurement(str(uuid.uuid4()), 3, 1, 11),
    Measurement(str(uuid.uuid4()), 2, 1, 90),
    Measurement(str(uuid.uuid4()), 2, 2, 60),
    Measurement(str(uuid.uuid4()), 2, 3, 73),
    Measurement(str(uuid.uuid4()), 3, 1, 40),
    Measurement(str(uuid.uuid4()), 3, 2, 44),
    Measurement(str(uuid.uuid4()), 3, 3, 90)
]

# C-style
high_measurements1 = []  # all with value over 70
for m in measurements:
    if m.value > 70:
        high_measurements1.append(m.value)

# list comprehension
high_measurements2 = [m.value for m in measurements if m.value > 70]

# generator expression
high_measurements_gen = (m.value for m in measurements if m.value > 70)
print(high_measurements_gen)

# process the generator to get something printable.
high_measurements3 = list(high_measurements_gen)

# dict comprehension
high_m_by_id = {m.id: m.value for m in measurements if m.value > 70}

# set comprehension
high_values_distinct = {m.value for m in measurements if m.value > 70}

print(high_measurements1)
print(high_measurements2)
print(high_measurements3)
print(high_m_by_id)
print(high_values_distinct)


