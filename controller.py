import view
import read
import additional

empl_data = read.read_json()
pos = 1
while 1 <= pos <= 9:
    pos = view.select_action()
    if pos == 1:
        what_find = view.find_empl()
        data_to_print = additional.find_what_empl(what_find)
        print(data_to_print)  # заменить на метод из view
    if pos == 2:
        what_find = view.select_empl_position()
        data_to_print = additional.find_what_empl(what_find)
        print(data_to_print)  # заменить на метод из view
    if pos == 3:
        what_find = view.select_empl_salary()
        data_to_print = additional.find_what_empl(what_find)
        print(data_to_print)  # заменить на метод из view
    if pos == 4:
        what_find = view.add_empl()
        data_to_print = additional.find_what_empl(what_find)
        print(data_to_print)  # заменить на метод из view
    if pos == 5:
        what_find = view.delete_empl()
        data_to_print = additional.find_what_empl(what_find)
        print(data_to_print)  # заменить на метод из view
    if pos == 6:
        what_find = view.edit_empl_data()
        data_to_print = additional.find_what_empl(what_find)
        print(data_to_print)  # заменить на метод из view
    if pos == 7:
        what_find = view.export_data_json()
        data_to_print = additional.find_what_empl(what_find)
        print(data_to_print)  # заменить на метод из view
    if pos == 8:
        what_find = view.export_data_csv()
        data_to_print = additional.find_what_empl(what_find)
        print(data_to_print)  # заменить на метод из view
    if pos == 9:
        what_find = view.end_work()
        data_to_print = additional.find_what_empl(what_find)
        print(data_to_print)  # заменить на метод из view

    else:
        print("Некорректный ввод. Программа завершена")