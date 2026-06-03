from recipe.ingredient import Ingredient
from __future__ import annotations #добавила, чтобы не подчеркивалось, когда внутри класса ссылаюсь на тот же класс, ссылка на документацию в ридми


class Recipe:
    def __init__(self, title: str, ingredients: list[Ingredient]) -> None: #не помню, что конструкцию list[Ingredient] обсуждали на семинарах и не придумала, как по-другому написать, поэтому в ридми прикреплю ссылку на документацию
        self.title = title
        self.ingredients = ingredients.copy()

    def add_ingredient(self, ingredient: Ingredient) -> None:
        for i in range(len(self.ingredients)):
            if self.ingredients[i] == ingredient:
                self.ingredients[i].quantity += ingredient.quantity
                break
        else:
            self.ingredients.append(ingredient)

    @staticmethod
    def is_valid_ratio(ratio) -> bool:
        if type(ratio) in (int, float) and ratio > 0:
            return True
        else:
            return False

    def scale(self, ratio: float)-> Recipe:
        ingr = []
        for i in range(len(self.ingredients)):
            neww = Ingredient(self.ingredients[i].name, self.ingredients[i].quantity*ratio, self.ingredients[i].unit)
            ingr.append(neww)
        ans = Recipe(self.title, ingr)
        return ans

    def __len__ (self) -> int:
        count = 0
        arr = []
        for i in range(len(self.ingredients)):
            if arr.count(self.ingredients[i]) == 0:
                arr.append(self.ingredients[i])
                count += 1
        return count

    def __str__(self) -> str:
        ress = []
        for i in range(len(self.ingredients)):
            ress.append(f"  {self.ingredients[i]}")
        resstr = "\n".join(ress)
        return f"{self.title}:\n{resstr}"

