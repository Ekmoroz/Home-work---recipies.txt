from pprint import pprint


def recepies(file):
    cook_book = dict()
    with open(file, encoding='utf-8') as f:
        for line in f:
            name = line.strip()
            ingr_count = int(f.readline().strip())
            ingridient_list = list()
            for i in range(ingr_count):
                ingridients = ['ingredient_name', 'quantity', 'measure']
                ingridient_dict = dict(zip(ingridients, f.readline().strip().split('|')))
                ingridient_list.append(ingridient_dict)
            f.readline().strip()
            cook_book[name] = ingridient_list
    return cook_book


recepies('recipes.txt')


def get_shop_list_by_dishes(dishes, person_count):       # как функцию передать в аргумент не разобралась
    cook_book = recepies('recipes.txt')
    person_dict = {}
    ingridients_dict = {}
    for dish in dishes:
        # print(dish)
        # print(cook_book[dish])
        for i in cook_book[dish]:
            # print(i)
            person_dict[i['ingredient_name']] = {'measure': i['measure'], 'quantity': int(i['quantity']) * person_count}
            if ingridients_dict.get(i['ingredient_name']):
                sum_ingridients = int(person_dict[i['ingredient_name']]['quantity']) + int(
                    ingridients_dict[i['ingredient_name']]['quantity'])
                ingridients_dict[i['ingredient_name']]['quantity'] = sum_ingridients
            else:
                ingridients_dict.update(person_dict)

    pprint(ingridients_dict)


get_shop_list_by_dishes(['Фахитос', 'Омлет'], 8)
