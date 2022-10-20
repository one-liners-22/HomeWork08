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
        print(data_to_print) # заменить на метод из view
    if pos == 2:
        what_find = view.select_empl_position()
        data_to_print = additional.find_what_empl(what_find)
        print(data_to_print) # заменить на метод из view

else:
    print("Некорректный ввод. Программа завершена")

