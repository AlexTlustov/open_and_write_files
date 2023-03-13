from pprint import pprint
import os
# Прочтение файла с блюдами.
with open('recipes.txt', 'rt', encoding='utf-8') as recipes:
    cook_book = {}
    for str in recipes:
        recipe = str.strip()
        ingredient_quantity = int(recipes.readline())
        ingredient_list = []
        for i in range(ingredient_quantity):
            ingredient, quantity, measure = recipes.readline().strip().split(' | ')
            ingredient_list.append({
                'ingredient_name': ingredient,
                'quantity': quantity,
                'measure': measure
            })
        recipes.readline()
        cook_book[recipe] = ingredient_list
# Функция подсчет ингридентов исходя из количества персон.
def get_shop_list_by_dishes(dishes, person_count):
    all_dishes = cook_book.keys()
    shop_list_by_dishes = {}
    if set(dishes_list).issubset(all_dishes):
        for element in dishes:
            new_list = cook_book.get(element)
            new_dic = {}
            for i in new_list:
                ing = i.get('ingredient_name')
                meas = i.get('measure')
                quan = int(i.get('quantity'))
                if ing in shop_list_by_dishes.keys():
                    new_ele = shop_list_by_dishes[ing]
                    er = new_ele['quantity']
                    new_dic = {
                        'quantity': (quan * person_count) + er,
                        'measure': meas 
                        }
                elif ing not in shop_list_by_dishes.keys():
                    new_dic = {
                        'quantity': quan * person_count,
                        'measure': meas 
                        }
                shop_list_by_dishes[ing] = new_dic
    else:
        dishes_notfound = set(dishes_list).difference(all_dishes)
        return (f'Блюда {dishes_notfound} нет в меню.')
    return shop_list_by_dishes
# Пример с ингредиентами и количеством для блюд.
pprint(get_shop_list_by_dishes(['Фахитос', 'Запеченный картофель', 'Омлет'], 4), sort_dicts=False)  
# Объединение файлов в один с параметрами.
def work_with_files():
    count_rows = {}
    sorted_count_rows = []
    directory = 'sorted/'
    files = [file for file in os.listdir(directory) if os.path.isfile(f'{directory}/{file}')]
    for file in files:
        with open(f'{directory}/{file}', 'r', encoding='UTF=8') as text:
            count_rows[file] = len(text.readlines())
    sorted_count_rows = sorted(count_rows, key=count_rows.get)
    for file in sorted_count_rows:
        with open('sorted/new_file.txt', 'a', encoding="UTF-8") as my_file, open(f'{directory}/{file}', 'rt', encoding="UTF-8") as text:
            my_file.write(file + '\n')
            my_file.write(repr(count_rows[file]) + '\n')
            my_file.write(''.join(text.readlines()) + '\n')
work_with_files()










