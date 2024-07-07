def get_cats_info(path):

    try:

        cats_info = []

        with open(path, 'r') as file:
                while True:
                    line = file.readline()
                    if not line:
                        break
                    
                    try:
                        id_cats, name_cats, age_cats = line.split(',')
                        cat_info = {
                            'id': id_cats,
                            'name': name_cats,
                            'age': int(age_cats)
                        }
                        cats_info.append(cat_info)
                    except ValueError:
                        print(f"Неможливо обробити строку: {line.strip()}")
                        continue

    except FileNotFoundError:
        print(f"Файл '{path}' не знайдено.")
    
    return cats_info
    

path_to_file = 'task_2/cats_info.txt'
cats = get_cats_info(path_to_file)
for cat in cats:
    print(cat)