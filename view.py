# import tabulate
# import tkinter
from select import select

# def select_action() -> int:
#     print("\n" + "=" * 20)
#     print("Выберите необходимое действие")
#     print("1. Найти сотрудника по фамилии")
#     print("2. Сделать выборку сотрудников по должности")
#     print("3. Сделать выборку сотрудников по зарплате")
#     print("4. Добавить сотрудника")
#     print("5. Удалить сотрудника")#фамилия+имя, далее должность
#     print("6. Обновить данные сотрудника")#фамилия+имя, далее должность затем список действий что обновляем по ключу
#     print("7. Экспортировать данные в формате json")
#     print("8. Экспортировать данные в формате csv")
#     print("9. Закончить работу")
#     return int(input("Введите номер необходимого действия: "))


def select_action() -> int:
    # print("\n" + "=" * 20)
    print("Выберите необходимое действие")
    print("1. Поиск сотрудника")
    print("2. Добавить сотрудника")
    print("3. Удалить сотрудника")  # фамилия+имя, далее должность
    # фамилия+имя, далее должность затем список действий что обновляем по ключу
    print("4. Обновить данные сотрудника")
    print("5. Экспортировать данные ")
    print("6. Закончить работу")
    return int(input("Введите номер необходимого действия: "))


if select_action() == 1:
    def second_menue():
        print("По какому критерию предпочитаете осуществить поиск сотрудника(ов)")
        print("1. Найти сотрудника по фамилии")
        print("2. Сделать выборку сотрудников по должности")
        print("3. Сделать выборку сотрудников по зарплате")
        user_choice = int(input("Введите цифру "))
        return user_choice
    print(second_menue())
# 1. Найти сотрудника

if second_menue == 1:
    def find_empl():
        search_empl = input("Введите фамилию сотрудника: ")  # фамилию

        return search_empl
    # print(find_empl())


# 2. Сделать выборку сотрудников по должности
if second_menue == 2:
    def select_empl_position():
        select_pos = input("Введите искомую позицию: ")
        return select_pos
    # print(select_empl_position())


# 3. Сделать выборку сотрудников по зарплате
if second_menue == 3:
    def select_empl_salary():
        select_salary = input("Введите зарплату: ")
        return select_salary
    # print(select_empl_salary())


# 4. Добавить сотрудника, найден похожий сотрудник
def add_empl():
    add_somebody = input("Добавьте сотрудника: ")
    archive = {"id": ""}
    archive["last_name"] = (input("Введите фамилию сотрудника: "))
    archive["first_name"] = (input("Введите имя сотрудника: "))
    archive["position"] = (input("Введите должность сотрудника: "))
    archive["phone_number"] = (input("Введите телефонный номер сотрудника: "))
    archive["salary"] = (input("Введите зарплату сотрудника: "))
    return add_somebody
# print(add_empl())


# 5. Удалить сотрудника
def delete_empl():
    del_emp = input("Удалите сотрудника: ")
    return del_emp
# print(delete_empl())


# 6. Обновить данные сотрудника
def edit_empl_data():
    edit_data = input("Обновите данные сотрудника: ")
    print("Какие данные вы хотите обновить: ")
    edit = {"id": ""}
    edit["last_name"] = (input("Введите фамилию сотрудника: "))
    edit["first_name"] = (input("Введите имя сотрудника: "))
    edit["position"] = (input("Введите должность сотрудника: "))
    edit["phone_number"] = (input("Введите телефонный номер сотрудника: "))
    edit["salary"] = (input("Введите зарплату сотрудника: "))
    return edit_data
# print(edit_empl_data())


# 7. Экспортировать данные в формате json/csv
def export_data_json():
    print("Выберите формат экспорта файла json/csv: ")

    if export_data_json == 1:
        def data_json():
            export_data_json = input("Введите 1 для экспорта формата json: ")  

        return export_data_json
    elif export_data_csv == 2:
        def export_data_csv():
            export_data_csv = input("Введите 2 для экспорта формата csv: ")
    else:
        print("Введены не верные данные, введите 1 или 2")

    export_json = input("Эскпортировать в формат json: ")
    return export_json
# print(export_data_json())


# # 8. Экспортировать данные в формате csv
# def export_data_csv():
#     export_csv = input("Экспортировать в csv: ")
#     return export_csv
# # print(export_data_csv())


# 9. Закончить работу
def end_work():
    end = input("Завершить работу: ")
    return end

# print(end_work())


# def print_all_contacts(data):
#     data_to_print = []

#     for i in range(len(data)):
#         listik = list(data[i].values())
#         listik.pop(0)
#         data_to_print.append(listik)

#     col_names = ["Фамилия", "Имя Отчество", "Должность", "Телефон", "Зарплата"]
#     # print(data_to_print)
#     print(tabulate(data_to_print, headers=col_names,
#           tablefmt="fancy_grid", showindex="never"))

# # #print_all_contacts(data)


# Функционал
#     print("1. Найти сотрудника")
# def find_empl
#     print("2. Сделать выборку сотрудников по должности")
# def select_empl_position
#     print("3. Сделать выборку сотрудников по зарплате")
# def select_empl_salary
#     print("4. Добавить сотрудника")
# def add_empl
#     print("5. Удалить сотрудника")
# def delete_empl
#     print("6. Обновить данные сотрудника")
# def edit_empl_data
#     print("7. Экспортировать данные в формате json")
# def export_data_json
#     print("8. Экспортировать данные в формате csv")
# def export_data_cmv
#     print("9. Закончить работу")
# def end_work
