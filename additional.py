import read
import view
import write


data = read.read_json()

def last_id():
    id_list = [i["id"] for i in data]
    return max(id_list)

def find_what_empl(what_find):
    data_to_print = {}
    data_to_print = [i for i in data if what_find in str(i.values())]
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
         

x = find_what_empl('6')
y = find_what_empl('6')

print(x)
print(y)
print(x == y)