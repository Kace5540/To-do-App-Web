def get_todos(filepath="todos.txt"):
    with open(filepath, "r") as file:
        todos = file.readlines()
    return todos


def write_todos(file,todos):
    with open(file,"w") as file:
        file.writelines(todos)