import streamlit as st
import functions

todos = functions.get_todos()
def add_to_do():
    to_do = st.session_state["new_todo"]
    todos.append(to_do+'\n')
    functions.write_todos("todos.txt",todos)


st.title("My To Do App")
st.subheader("this is my to dos")
for index, todo in enumerate(todos):

    check = st.checkbox(todo,key=todo)
    if check:
        todos.pop(index)
        functions.write_todos('todos.txt',todos)
        del st.session_state[todo]
        st.rerun()
st.text_input(label="Enter a to do: ", placeholder="enter a to do",on_change=add_to_do,key="new_todo")

