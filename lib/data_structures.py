spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    pass
    the_names=[list["name"] for list in spicy_foods]
    return the_names

def get_spiciest_foods(spicy_foods):
    pass
    the_names=[list for list in spicy_foods if list['heat_level'] > 5]
    return the_names



def print_spicy_foods(spicy_foods):
    pass
    emoji='🌶'
    for list in spicy_foods:
        print(f"{list['name']} ({list['cuisine']}) | Heat Level: {emoji*list['heat_level']}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    pass
    result=[list for list in spicy_foods if list["cuisine"]==cuisine ]
    return result[0] if result else None

def print_spiciest_foods(spicy_foods):
    pass
    emoji = '🌶'
    the_names = [f"{food['name']} ({food['cuisine']}) | Heat Level: {emoji * food['heat_level']}" for food in spicy_foods if food['heat_level'] > 5]
    for name in the_names:
        print(name)

def get_average_heat_level(spicy_foods):
    pass
    sum=0
    for list in spicy_foods:
        sum +=list["heat_level"]
    return sum/len(list)

def create_spicy_food(spicy_foods, spicy_food):
    pass

    spicy_foods.append(spicy_food)
    return spicy_foods