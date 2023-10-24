import tkinter as tk
from tkinter import ttk
import mysql.connector

def show_item():
    print("Pokaż towar")

def add_item():
    add_window = tk.Toplevel(root)
    add_window.title("Add item")

    add_label = tk.Label(add_window, text="Nazwa:")
    add_label.pack()
    name_entry = tk.Entry(add_window)
    name_entry.pack()

    description_label = tk.Label(add_window, text="Opis:")
    description_label.pack()
    description_entry = tk.Entry(add_window)
    description_entry.pack()

    quantity_label = tk.Label(add_window, text="Ilość:")
    quantity_label.pack()
    quantity_entry = tk.Entry(add_window)
    quantity_entry.pack()

    def add_new_item():
        item_name = name_entry.get()
        item_description = description_entry.get()
        item_quantity = quantity_entry.get()

        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="tomek123",
            database="stan"
        )
        cursor = connection.cursor()

        query = "INSERT INTO stan_magazynu (Nazwa, Opis, Ilość) VALUES (%s, %s, %s)"
        values = (item_name, item_description, item_quantity)
        cursor.execute(query, values)

        connection.commit()
        cursor.close()
        connection.close()

        add_window.destroy()

    add_button = tk.Button(add_window, text="Dodaj towar", command=add_new_item)
    add_button.pack()

def remove_item():
    print("Usuń")

def refresh_table():
    for item in tree.get_children():
        tree.delete(item)
    show_table()

def show_table():
    table_name = 'stan_magazynu'
    query = f'SELECT * FROM {table_name}'
    cursor.execute(query)
    rows = cursor.fetchall()

    for row in rows:
        tree.insert("", "end", values=row)

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password='tomek123',
    database='stan'
)

cursor = connection.cursor()

root = tk.Tk()
root.title("Aplikacja magazynowa")
root.geometry('800x600')

tree = ttk.Treeview(root, columns=("ID", "Nazwa", "Opis", "Ilość"), show="headings")
tree.heading("ID", text="ID")
tree.heading("Nazwa", text="Nazwa")
tree.heading("Opis", text="Opis")
tree.heading("Ilość", text="Ilość")

tree.column("ID", width=30)
tree.column("Nazwa", width=100)
tree.column("Opis", width=100)
tree.column("Ilość", width=100)
tree.place(x=400, y=350)
show_table()

click_show = tk.Button(root, text="Show item", height=2, width=15, command=show_item)
click_show.pack()
click_show.place(x=250, y=350)

click_add = tk.Button(root, text="Add item", height=2, width=15, command=add_item)
click_add.pack()
click_add.place(x=250, y=400)

click_remove = tk.Button(root, text="Remove item", height=2, width=15, command=remove_item)
click_remove.pack()
click_remove.place(x=250, y=450)

click_refresh = tk.Button(root, text="Refresh", height=2, width=15, command=refresh_table)
click_refresh.pack()
click_refresh.place(x=250, y=500)

tree.pack()

root.mainloop()

cursor.close()
connection.close()
