import random as rd
import json


class Test:

    def __init__(self):
        with open("bd.json", "r") as f:
            self.__dict__ = json.load(f)

    def __setitem__(self, key, value):
        self.__dict__[key] = value
        with open("bd.json", "w") as f:
            json.dump(self.__dict__, f)

    def __getitem__(self, item):
        return self.__dict__[item]


objet_test = Test()
print(objet_test["a"], objet_test["b"])
objet_test["a"] = rd.randint(1, 100)
objet_test["b"] = int(input("Un nbr."))