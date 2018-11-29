#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import choice


class Person:

    def __init__(self, name):
        self.greeting = "Hello {name},{n},{age}"
        self.name = name
        self.age = 1

    def __str__(self):

        return self.make_greeting()

    def make_greeting(self):
        return self.greeting.format(name=self.name, n='great!', age=self.age)


def main():
    people = [
        Person('jane'),
        Person('jill那'),
        Person('sqshine')
    ]
    person = choice(people)
    person.age = 10
    print(person)


if __name__ == '__main__':
    main()
