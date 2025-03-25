def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def is_empty_line(s):
    if s == '':
        return True

def is_ingredient(s):
    if any(c in '|' for c in s):
        return True

def fill_cook_book():
    cook_book = {}
    with (open('recipes.txt', 'r') as file):
        ingredients = []
        recipe_name = ''
        ingredients_count = 0
        for row in file:
            if not is_empty_line(row.strip()) and not is_number(row.strip()) and not is_ingredient(row.strip()):
                recipe_name = row.strip()
            elif is_number(row.strip()):
                ingredients_count = int(row.strip())
            elif ingredients_count > 0 and is_ingredient(row.strip()):
                _list = row.strip().split(' | ')
                ingredients += [{'ingredient_name': _list[0], 'quantity': _list[1], 'measure': _list[2]}]
                ingredients_count -= 1
                if ingredients_count == 0:
                    cook_book[recipe_name] = ingredients
            else:
                ingredients = []
    return cook_book
print(fill_cook_book())