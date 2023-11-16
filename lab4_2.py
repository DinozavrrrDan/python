# TODO решите задачу
import json


def task() -> float:
    with open("input.json", 'r') as file:
        data = json.load(file)
        products = [entry["score"] * entry["weight"] for entry in data]
        return float('%.3f' % sum(products))

print(task())
