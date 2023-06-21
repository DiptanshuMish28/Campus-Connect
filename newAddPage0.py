from tkinter import *
from tkinter import ttk
import newPageAdd
import clientMain
import tkinter as tk
from tkinter import ttk
import sqlite3
from tkinter import Frame
import newPageAdd
import clientMain


# s = ttk.Style()
# s.configure('.', font=("Product Sans", 16))


class NewAddPage0:
    def __init__(self, loginId):

        # style = ttk.Style()
        # style.configure('.', font=('Product Sans', 16))

        conn = sqlite3.connect('cc.db')

        # Create a cursor object
        c = conn.cursor()

        # Define a function to retrieve data from the database

        def back1():
            frame.destroy()
            clientMain.ClientMain(loginId)

        def get_data():
            # Execute a query to retrieve data from the database
            c.execute('SELECT * FROM products')
            data = c.fetchall()
            return data

        # Define a function to display the data in the UI

        def display_data():
            # Clear any existing data in the treeview widget
            treeview.delete(*treeview.get_children())

            # Get the data from the database
            data = get_data()

            # Loop through the data and insert it into the treeview widget
            for row in data:
                treeview.insert('', 'end', values=row)

        # Define a function to handle the TreeviewSelect event

        def on_select(event):
            # Get the selected item from the treeview widget
            item = treeview.selection()[0]

            # Get the values of the selected item
            values = treeview.item(item, 'values')

            # Open a new window to display the details of the selected item
            window = tk.Toplevel(frame)
            window.title('Product Details')
            window.geometry('500x300')
            window.resizable(False, False)

            # Create labels to display the details
            name_label = ttk.Label(window, text='Name:',
                                   font=("Product Sans", 16))
            name_label.grid(row=0, column=0, padx=10,
                            pady=10, sticky='w')
            name_value = ttk.Label(
                window, text=values[0], font=("Product Sans", 16))
            name_value.grid(row=0, column=1, padx=10, pady=10, sticky='w')

            desc_label = ttk.Label(
                window, text='Description:', font=("Product Sans", 16))
            desc_label.grid(row=1, column=0, padx=10, pady=10, sticky='w')
            desc_value = ttk.Label(
                window, text=values[1], font=("Product Sans", 16))
            desc_value.grid(row=1, column=1, padx=10, pady=10, sticky='w')

            price_label = ttk.Label(window, text='Price:',
                                    font=("Product Sans", 16))
            price_label.grid(row=2, column=0, padx=10, pady=10, sticky='w')
            price_value = ttk.Label(
                window, text=values[2], font=("Product Sans", 16))
            price_value.grid(row=2, column=1, padx=10, pady=10, sticky='w')

            contact_label = ttk.Label(
                window, text='Contact Number:', font=("Product Sans", 16))
            contact_label.grid(row=3, column=0, padx=10, pady=10, sticky='w')
            contact_value = ttk.Label(
                window, text="YOUR MOM", font=("Product Sans", 16))
            contact_value.grid(row=3, column=1, padx=10, pady=10, sticky='w')
        frame = Tk()

        frame.geometry("1266x668+50+20")
        frame.minsize(1266, 668)
        frame.maxsize(1266, 668)
        frame.title("CampusConnect")
        myicon = PhotoImage(file='images/myIcon.png')
        frame.iconphoto(False, myicon)
        frame.config(bg="mediumpurple")

        newWindow = Frame(frame)
        newWindow.place(x=30, y=20, width=1206, height=628)
        newWindow.config(bg="white")

        treeview = ttk.Treeview(frame, columns=(
            'name', 'description', 'price', 'contact_number'), show='headings', height=15)
        treeview.column('name', width=150)
        treeview.column('description', width=400)
        treeview.column('price', width=100)
        treeview.column('contact_number', width=150)
        treeview.heading('name', text='Name')
        treeview.heading('description', text='Description')
        treeview.heading('price', text='Price')
        treeview.heading('contact_number', text='Contact Number')
        treeview.bind('<<TreeviewSelect>>', on_select)

        treeview.pack(padx=10, pady=150)
        refresh_button = Button(
            frame, text='Refresh', command=display_data, font=("Product Sans", 16))
        refresh_button.pack(side='right', padx=200, pady=0)

        # Create a button to go back to the main window
        back_button = Button(frame, text='Back',
                             command=back1, font=("Product Sans", 16))
        back_button.pack(side='left', padx=200, pady=0)

        def nextProp():
            frame.destroy()
            newPageAdd.NewAddPage(loginId)

        def back1():
            frame.destroy()
            clientMain.ClientMain(loginId)

        display_data()
        frame.mainloop()


if __name__ == '__main__':
    myPage = NewAddPage0(900)
