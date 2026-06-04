from __future__ import annotations

import sys
sys.path.insert(0, '.')

import pytest

from recipe.ingredient import Ingredient
from recipe.recipe import Recipe

def test_creation():
    a = Ingredient("Яблоко", 30.0, "шт")
    assert a.name == "Яблоко"
    assert a.quantity == 30.0
    assert a.unit == "шт"

def test_str():
    a = Ingredient("Яблоко", 30.0, "шт")
    assert str(a) == "Яблоко: 30.0 шт"

def test_eq_same():
    a = Ingredient("Яблоко", 30.0, "шт")
    b = Ingredient("Яблоко", 66.0, "шт")
    assert a==b

def test_eq_notsame_name():
    a = Ingredient("Клубника", 30.0, "шт")
    b = Ingredient("Яблоко", 30.0, "шт")
    assert a!=b

def test_eq_notsame_unit():
    a = Ingredient("Клубника", 300.0, "шт")
    b = Ingredient("Клубника", 300.0, "г")
    assert a!=b



def test_recipe_creation():
    a = Ingredient("Клубника", 300.0, "шт")
    b = Ingredient("Яблоко", 30.0, "шт")
    recipe = Recipe("Йогурт", [a, b])
    assert recipe.title == "Йогурт"
    assert recipe.ingredients[0].name == "Клубника"
    assert recipe.ingredients[1].name == "Яблоко"

def test_add_new_ingredient():
    neww = Ingredient("Клубника", 300.0, "шт")
    r = Recipe("Шоколадка", [neww])
    r.add_ingredient(Ingredient("Молоко", 300.0, "г"))
    assert r.ingredients[0].name == "Клубника"
    assert r.ingredients[1].name == "Молоко"
    assert r.ingredients[1].quantity == 300.0

def test_add_old_ingredient():
    neww = Ingredient("Клубника", 300.0, "шт")
    r = Recipe("Шоколадка", [neww])
    r.add_ingredient(Ingredient("Клубника", 210.0, "шт"))
    assert r.ingredients[0].name == "Клубника"
    assert r.ingredients[0].quantity == 510.0
    assert len(r.ingredients) == 1

def test_scale_new_recipe():
    neww = Ingredient("Клубника", 300.0, "шт")
    r = Recipe("Шоколадка", [neww])
    newrrr = r.scale(2)
    assert newrrr.title == r.title
    assert newrrr is not r

def test_scale_new_quantity():
    neww = Ingredient("Клубника", 300.0, "шт")
    r = Recipe("Шоколадка", [neww])
    newrrr = r.scale(2)
    assert newrrr.ingredients[0].quantity == 600.0

def test_scale_invalid_ratio():
    neww = Ingredient("Клубника", 300.0, "шт")
    r = Recipe("Шоколадка", [neww])
    f = False
    try:
        r.scale(-1)
    except ValueError:
        f = True
    assert f

def test_uniq():
    neww = Ingredient("Клубника", 300.0, "шт")
    new1 = Ingredient("Яблоко", 300.0, "шт")
    new2 = Ingredient("Мармеладка", 300.0, "шт")
    r = Recipe("Шоколадка", [neww, new1, new1, new2, neww])
    assert len(r) == 3

