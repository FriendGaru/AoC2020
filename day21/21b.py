def build_food_list_and_allergens_dict(filename):
    allergen_dict = {}
    foods = []
    with open(filename) as file:
        for line in file:
            line = line.strip()
            if line == "":
                continue
            ingredients_chunk, allergens_chunk = line.split(("("))
            ingredients_chunk = ingredients_chunk.strip()
            ingredients = ingredients_chunk.split(" ")
            ingredients = [ingredient.strip() for ingredient in ingredients]
            allergens_chunk = allergens_chunk.replace("contains", "")
            allergens_chunk = allergens_chunk.replace(")", "")
            allergens = allergens_chunk.split(", ")
            allergens = [allergen.strip() for allergen in allergens]

            foods.append(set(ingredients))

            for allergen in allergens:
                if not allergen:
                    continue
                if allergen in allergen_dict:
                    allergen_dict[allergen].append(set(ingredients))
                else:
                    allergen_dict[allergen] = [set(ingredients), ]
    return foods, allergen_dict

def build_all_ingredients_set(allergens_possible_ingredients_dict: dict):
    full_set = set()
    for ingredients_sets in allergens_possible_ingredients_dict.values():
        for ingredients_set in ingredients_sets:
            full_set.update(ingredients_set)
    return full_set

def count_safe_ingredients(foods_list: list, safe_ingredients_set: set):
    total_count = 0
    for food in foods_list:
        assert isinstance(food, set)
        total_count += len(food.intersection(safe_ingredients_set))
    return total_count

def build_confirmed_ingredients_dict_and_set(allergens_possible_ingredients_dict: dict):
    confirmed_igredient_allergens_dict = {}
    confirmed_ingredients_with_allergens_set = set()
    working_allergens_possible_ingredients = {}
    for allergen, possible_ingredient_sets in allergens_possible_ingredients_dict.items():
        check_set = possible_ingredient_sets[0]
        for i in range(1, len(possible_ingredient_sets)):
            check_set = check_set.intersection(possible_ingredient_sets[i])
        working_allergens_possible_ingredients[allergen] = check_set

    while len(working_allergens_possible_ingredients) > 0:
        allergens_to_remove = []
        for allergen, possible_ingredients in working_allergens_possible_ingredients.items():
            if len(possible_ingredients) == 1:
                confirmed_ingredient = possible_ingredients.pop()
                confirmed_ingredients_with_allergens_set.add(confirmed_ingredient)
                confirmed_igredient_allergens_dict[confirmed_ingredient] = allergen
                allergens_to_remove.append(allergen)
        for allergen_to_remove in allergens_to_remove:
            working_allergens_possible_ingredients.pop(allergen_to_remove)
        for allergen, possible_ingredients in working_allergens_possible_ingredients.items():
            possible_ingredients.difference_update(confirmed_ingredients_with_allergens_set)
    return confirmed_igredient_allergens_dict, confirmed_ingredients_with_allergens_set

def build_safe_ingredients_set(confirmed_ingredients_with_allergens_set):
    return all_ingredients_set.difference(confirmed_ingredients_with_allergens_set)

def reverse_confirmed_ingredient_allergen_dict(confirmed_igredient_allergens_dict: dict):
    allergen_to_ingredient_dict = {}
    for k, v in confirmed_igredient_allergens_dict.items():
        allergen_to_ingredient_dict[v] = k
    return allergen_to_ingredient_dict

def alphabetized_allergeens(allergen_to_ingredient_dict: dict):
    return sorted(list(allergen_to_ingredient_dict.keys()))

def get_answer(allergen_to_ingredient_dict: dict, alphabetized_allergen_list):
    return ",".join([allergen_to_ingredient_dict[allergen] for allergen in alphabetized_allergen_list])


foods, allergens_possible_ingredients_dict = build_food_list_and_allergens_dict("input.txt")
all_ingredients_set = build_all_ingredients_set(allergens_possible_ingredients_dict)
confirmed_igredient_allergens_dict, confirmed_ingredients_with_allergens_set = build_confirmed_ingredients_dict_and_set(allergens_possible_ingredients_dict)
safe_ingredients = build_safe_ingredients_set(confirmed_igredient_allergens_dict)
allergen_to_ingredient_dict = reverse_confirmed_ingredient_allergen_dict(confirmed_igredient_allergens_dict)
alphabetized_allergens = alphabetized_allergeens(allergen_to_ingredient_dict)
answer = get_answer(allergen_to_ingredient_dict, alphabetized_allergens)
print(answer)