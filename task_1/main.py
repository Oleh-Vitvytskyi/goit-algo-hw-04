def total_salary(path):

    try:
        total_salary = 0
        count = 0

        with open(path, 'r') as file:
            while True:
                line = file.readline()
                if not line:
                    break
                try:
                    name, money = line.split (',')
                    money = float(money)
                    total_salary += money
                    count += 1
                except ValueError:
                    print(f'Неможливо обробити строку: {line.strip()}')
        
        if count > 0:
            average_salary = total_salary / count
        else:
            average_salary = 0

        print (f'Загальна зарплата: {total_salary}')
        print (f'Середня зарплата: {average_salary}')

    except FileNotFoundError:
        print(f"Файл '{path}' не знайдено.")

total_salary('task_1/text.txt')