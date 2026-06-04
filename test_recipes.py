from __future__ import annotations

import sys
sys.path.insert(0, '.')

import pytest

from recipe.ingredient import Ingredient
from recipe.recipe import Recipe
from recipe.shoppinglist import ShoppingList

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

def test_shoppinglist_add():
    arr = ShoppingList()
    newr = Recipe("Nutella", [Ingredient("Сахар", 100.0, "г")])
    arr.add_recipe(newr, 10)
    assert arr.get_list()[0].quantity == 1000.0
    f = False
    try:
        arr.add_recipe(newr, -10)
    except ValueError:
        f = True
    assert f


def test_shoppinglist_remove():
    arr = ShoppingList()
    arr.add_recipe(Recipe("Nutella", [Ingredient("Сахар", 100.0, "г")]), 1)
    arr.remove_recipe("Nutella")
    assert arr.get_list() == []
    arr.add_recipe(Recipe("Nutella", [Ingredient("Сахар", 100.0, "г")]), 1)
    arr.remove_recipe("Milka")
    assert len(arr.get_list()) == 1


def test_shoppinglist_get_list():
    arr = ShoppingList()
    newr1 = Recipe("Nutella", [Ingredient("Сахар", 100.0, "г")])
    newr2 = Recipe("Milka", [Ingredient("Сахар", 200.0, "г")])
    arr.add_recipe(newr1, 1)
    arr.add_recipe(newr2, 2)
    ress= arr.get_list()
    assert len(ress) == 1
    assert ress[0].name == "Сахар"
    assert ress[0].quantity == 500.0


def test_shoppinglist_get_listsort():
    arr = ShoppingList()
    newr = Recipe("Nutella", [Ingredient("Сахар", 100.0, "г"), Ingredient("Масло", 50.0, "г"), Ingredient("Какао", 30.0, "г"), Ingredient("Орехи", 40.0, "г")])
    arr.add_recipe(newr, 1)
    ress = arr.get_list()
    ans = []
    for i in range(len(ress)):
        ans.append(ress[i].name)
    assert ans== sorted(ans)

def test_shoppinglist_add_new():
    arr1 = ShoppingList()
    arr2 = ShoppingList()
    newr1 = Recipe("Nutella", [Ingredient("Сахар", 100.0, "г")])
    newr2 = Recipe("Milka", [Ingredient("Масло", 50.0, "г")])
    arr1.add_recipe(newr1, 1)
    arr2.add_recipe(newr2, 1)
    arr3 = arr1 + arr2
    assert len(arr3._items) == 2
    assert len(arr1._items) == 1
    assert len(arr2._items) == 1
