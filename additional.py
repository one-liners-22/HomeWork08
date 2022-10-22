import read
import view
import write


data = read.read_json()
new_empl = 'Петров Петр'
def last_id():
    id_list = [i["id"] for i in data]
    return max(id_list)

# def find_what_empl(what_find): # search_empl 
#     data_to_print = []
#     l = list(what_find.split()) # search_empl
#     for i in data:     
#         if len(l) == 3:
#             new_l = str(l[1] + ' ' + l[2])          
#         if len(l) == 2:
#             new_l = str(l[1])
#         if i['last_name'] == l[0] and i['first_name'] == new_l:
#             data_to_print.append(i) 
#     return data_to_print
# Найти сотрудника
def find_what_empl(what_find): #только одно слово - фамилия
    return [i for i in data if i['last_name'] == what_find]            

def new_emple_create(new_empl):

    if not (find_what_empl(new_empl["last_name"]) == find_what_empl(new_empl["first_name"])):
        id = last_id() + 1
        new_empl = {"id": id}
        data.append(new_empl)
        return data
    else:
        print("Похожий сотрудник есть")
        return find_what_empl()   
# print(find_what_empl(new_empl))

# Сделать выборку сотрудников по должности
def select_position(select_pos):
    return [i for i in data if i['position'] == select_pos]
# Сделать выборку сотрудников по зарплате
def select_salary_empl(select_salary):
    return[i for i in data if i['salary'] == select_salary]

# Добавить сотрудника (есть ли он или нет( по имени и фамилии))
def add_what_empl(add_somebody):
    data_to_print = find_what_empl(add_somebody)
    print(data_to_print)
# Удалить сотрудника (по тому же принципу)
def delet_what_empl(del_emp):
    data_to_print = []
    l = list(del_emp.split())
    for i in data:
        if i['last_name'] == l[0] and i['first_name'] == str(l[1] + ' ' + l[2]):
            del i
            return print("Сотрудник удален!")
        else:
            return print('Сотрудник не найден!')
