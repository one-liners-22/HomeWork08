import read
import view
import write


data = read.read_json()
new_empl = 'Петров Петр'
def last_id():
    id_list = [i["id"] for i in data]
    return max(id_list)

def find_what_empl(what_find):
    data_to_print = []
    l = list(what_find.split())
    for i in data:     
        if len(l) == 3:
            new_l = str(l[1] + ' ' + l[2])          
        if len(l) == 2:
            new_l = str(l[1])
        if i['last_name'] == l[0] and i['first_name'] == new_l:
            data_to_print.append(i) 
    return data_to_print

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
def select_position(select_pos = 'главный бухгалтер'):
    return [i for i in data if i['position'] == select_pos]
print(select_position())
# Сделать выборку сотрудников по зарплате
# Добавить сотрудника (есть ли он или нет( по имени и фамилии))
# Удалить сотрудника (по тому же принципу)