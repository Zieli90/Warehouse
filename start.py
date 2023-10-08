from tkinter import *
from tkinter import ttk
import mysql.connector

def show_item():
    print("pokaż towar")

def add_item():
    print("udało się")

def remove_item():
    print("Usuń")

def show_table(tree, cursor):
    table_name = 'stan_magazynu'
    query = f'SELECT * FROM {table_name}'
    cursor.execute(query)
    rows = cursor.fetchall()

    for row in rows:
        tree.insert("", "end", values = row)


connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = 'tomek123',
    database = 'stan'
)

cursor = connection.cursor()

root = Tk()
root.title("Aplikacja magazynowa")
root.geometry('800x600')

tree = ttk.Treeview(root, columns = ("ID","Nazwa", "Opis", "Ilość"), show = "headings")
tree.heading("ID", text = "ID")
tree.heading("Nazwa", text = "Nazwa")
tree.heading("Opis", text = "Opis")
tree.heading("Ilość", text = "Ilość")

tree.column("ID", width = 30)
tree.column("Nazwa", width = 100)
tree.column("Opis", width = 100)
tree.column("Ilość", width = 100)
tree.place(x=400, y=350)
show_table(tree, cursor)

click_show = Button(root, text="Show item", height=2, width=15, command=show_item)
click_show.pack()
click_show.place(x=250, y=350)

click_add = Button(root, text="Add item",  height=2, width=15, command=add_item)
click_add.pack()
click_add.place(x=250,y=400)

click_remove = Button(root, text="Remove item", height=2, width=15, command=remove_item)
click_remove.pack()
click_remove.place(x=250,y=450)

click_exit = Button(root, text="Exit", height=2, width= 15, command=root.destroy)
click_exit.pack()
click_exit.place(x=250,y=500)

tree.pack()

root.mainloop()

cursor.close()
connection.close()