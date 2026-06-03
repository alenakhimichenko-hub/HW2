from __future__ import annotations
from recipe.ingredient import Ingredient
from recipe.recipe import Recipe



class ShoppingList:
    def __init__(self) -> None:
        self._items = []

    def add_recipe(self, recipe: Recipe, portions: float) -> None:
        if portions <= 0:
            raise ValueError("Количество порций должно быть положительным")
        else:
            new = recipe.scale(portions)
            for i in range(len(new.ingredients)):
                self._items.append((new.ingredients[i], recipe.title))

    def remove_recipe(self, title: str) -> None:
        arr = []
        for i in range(len(self._items)):
            if self._items[i][1] != title:
                arr.append(self._items[i])
            else:
                continue
        self._items = arr

    def get_list(self) -> list[Ingredient]:
        dictt = {}
        res = []
        for i in range(len(self._items)):
            key = self._items[i][0]
            if (key.name, key.unit) not in dictt:
                dictt[(key.name, key.unit)] = key.quantity
            else:
                dictt[(key.name, key.unit)] += key.quantity
        for (x, y), z in dictt.items():
            newww = Ingredient(x, z, y)
            res.append(newww)
        res.sort(key = lambda x: x.name)
        return res

    def __add__(self, other: ShoppingList) -> ShoppingList:
        neww = ShoppingList()
        neww._items = self._items + other._items
        return neww