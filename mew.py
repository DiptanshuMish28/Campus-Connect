from tkinter import *
from tkinter import ttk
import mySQLConnection as database
import adminMainPage


class PurchaseTable():
    def __init__(self):
        frame = Tk()
        frame.geometry("1286x668+50+20")
        frame.minsize(1266, 668)
        frame.maxsize(1266, 668)
        frame.title("CampusConnect")
        myicon = PhotoImage(file='images/myIcon.png')
        frame.iconphoto(False, myicon)
        myTitle = Label(frame, text="PURCHASER'S TABLE",
                        font=("Product Sans", 24, "bold"))
        myTitle.place(x=0, y=0, width=1266, height=50)
        myTitle.config(bg="midnightblue", fg="white")
        database.myQuery.execute("select * from mypurchase")

        def toMoveBack():
            frame.destroy()
            adminMainPage.AdminMainPage()
        Back = Button(myTitle, text="<<", font=("Product Sans", 16, "bold"))
        Back.place(x=10, y=4)
        Back.config(bg="midnightblue", fg="white", activeforeground="white", activebackground="midnightblue",
                    borderwidth=0, command=toMoveBack)
        tree = ttk.Treeview(frame)
        tree['show'] = "headings"
        styles = ttk.Style()
        styles.theme_use("clam")
        styles.configure(".", font=("Product Sans", 14))
        styles.configure("Treeview.Heading", foreground="midnightblue", font=('Product Sans', 11, "bold"), background="white",
                         borderwidth=0)
        tree["columns"] = ("ID", "NAME", "ADDRESS", "BTYPE", "ATYPE",
                           "ASQFT", "LOC", "LANDMARK", "UP", "LP", "CONTACT", "ACTIONS")
        tree.column("ID", width=10, minwidth=50, anchor=CENTER)
        tree.column("NAME", width=50, minwidth=50, anchor=CENTER)
        tree.column("ADDRESS", width=50, minwidth=50, anchor=CENTER)
        tree.column("BTYPE", width=50, minwidth=50, anchor=CENTER)
        tree.column("ATYPE", width=50, minwidth=50, anchor=CENTER)
        tree.column("ASQFT", width=50, minwidth=50, anchor=CENTER)
        tree.column("LOC", width=50, minwidth=50, anchor=CENTER)
        tree.column("LANDMARK", width=50, minwidth=50, anchor=CENTER)
        tree.column("UP", width=50, minwidth=50, anchor=CENTER)
        tree.column("LP", width=50, minwidth=50, anchor=CENTER)
        tree.column("CONTACT", width=50, minwidth=50, anchor=CENTER)
        tree.column("ACTIONS", width=50, minwidth=50, anchor=CENTER)
        tree.heading("ID", text="ID", anchor=CENTER)
        tree.heading("NAME", text="NAME", anchor=CENTER)
        tree.heading("ADDRESS", text="ADDRESS", anchor=CENTER)
        tree.heading("BTYPE", text="BUILDING TYPE", anchor=CENTER)
        tree.heading("ATYPE", text="AREA TYPE", anchor=CENTER)
        tree.heading("ASQFT", text="AREA SQ FT.", anchor=CENTER)
        tree.heading("LOC", text="LOCATION", anchor=CENTER)

        # Adding data to the treeview
        for i in range(len(data)):
            tree.insert(parent="", index=i, iid=i, text="", values=(
                data[i]["name"], data[i]["age"], data[i]["gender"], data[i]["address"], data[i]["location"]))

        # Adding a scrollbar to the treeview
        scrollbar = ttk.Scrollbar(root, orient=VERTICAL, command=tree.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        tree.configure(yscrollcommand=scrollbar.set)

        root.mainloop()
