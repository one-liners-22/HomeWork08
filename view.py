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

def find_empl():
   search_empl = input("Введите ФИО сотрудника: ")
   return search_empl
# print(find_empl())
        
def select_empl_position():
    select_pos = input("Введите искомую позицию: ")
    return select_pos
# print(select_empl_position())




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
#     print("8. Экспортировать данные в формате cmv")
# def export_data_cmv
#     print("9. Закончить работу")
# def end_work
#     return int(input("Введите номер необходимого действия: "))

    
    
