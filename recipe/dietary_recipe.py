from __future__ import annotations
from recipe.recipe import Recipe
from recipe.ingredient import Ingredient

class DietaryRecipe(Recipe):
    def __init__(self, title: str, diet_type: str, ingredients: list[Ingredient]=None)->None:
        self.diet_type = diet_type
        if ingredients is None:
            ingredients = []
        super().__init__(title, ingredients)

    def scale(self, ratio: float) -> DietaryRecipe:
        scaled_recipe = super().scale(ratio)
        return DietaryRecipe(scaled_recipe.title, self.diet_type, scaled_recipe.ingredients)

    def __str__(self) -> str:
        ress = []
        for i in range(len(self.ingredients)):
            ress.append(f"  {self.ingredients[i]}")
        resstr = "\n".join(ress)
        return f"[{self.diet_type}] {self.title}:\n{resstr}"
