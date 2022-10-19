from select import select

def select_action() -> int:
    print("\n" + "=" * 20)
    print("Выберите необходимое действие")
    print("1. Найти сотрудника")
    print("2. Сделать выборку сотрудников по должности")
    print("3. Сделать выборку сотрудников по зарплате")
    print("4. Добавить сотрудника")
    print("5. Удалить сотрудника")
    print("6. Обновить данные сотрудника")
    print("7. Экспортировать данные в формате json")
    print("8. Экспортировать данные в формате cmv")
    print("9. Закончить работу")
    return int(input("Введите номер необходимого действия: "))

# 1. Найти сотрудника
def find_empl():
   search_empl = input("Введите ФИО сотрудника: ")
   return search_empl
# print(find_empl())
 

# 2. Сделать выборку сотрудников по должности   
def select_empl_position():
    select_pos = input("Введите искомую позицию: ")
    return select_pos
# print(select_empl_position())


# 3. Сделать выборку сотрудников по зарплате
def select_empl_salary():
    select_salary = input("Введите зарплату: ")
    return select_salary
# print(select_empl_salary())


# 4. Добавить сотрудника
def add_empl():
    add_somebody = input("Добавьте сотрудника: ")
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
    return edit_data
# print(edit_empl_data())


# 7. Экспортировать данные в формате json
def export_data_json():
    export_json = input("Эскпортировать в формат json: ")
    return export_json
# print(export_data_json())


# 8. Экспортировать данные в формате csv
def export_data_csv():
    export_csv = input("Экспортировать в csv: ")
    return export_csv
# print(export_data_csv())


# 9. Закончить работу
def end_work():
    end = input("Завершить работу: ")
    return end
# print(end_work())    



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


    
    
