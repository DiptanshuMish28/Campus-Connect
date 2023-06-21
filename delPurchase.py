from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox as popup
import adminMainPage
import mySQLConnection as database


class PurchaseDelete:
    def __init__(self):
        frame = Tk()

        frame.geometry("1266x668+50+20")
        frame.minsize(1266, 668)
        frame.maxsize(1266, 668)
        frame.title("CampusConnect")
        myicon = PhotoImage(file='images/myIcon.png')
        frame.iconphoto(False, myicon)
        frame.config(bg="white")

        myLayout = Label(frame)
        myLayout.place(x=0, y=0, width=1266, height=434.2)
        myLayout.config(bg="mintcream")

        myLayout2 = Label(frame)
        myLayout2.place(x=0, y=434.2, width=1266, height=668 - 434.2)
        myLayout2.config(bg="midnightblue")

        newWindow = Frame(frame)
        newWindow.place(x=233, y=84, width=800, height=500)
        newWindow.config(bg="white")

        def toMoveBack():
            frame.destroy()
            adminMainPage.AdminMainPage()

        def toDelete():
            getID = IdEntry.get().strip()
            if getID in "":
                popup.showwarning("CampusConnect",
                                  "Kindly Enter ID First!!!!")
                return
            try:
                toMakeInt = int(getID)
                try:
                    database.myQuery.execute(
                        f"select * from mypurchase where p_id={toMakeInt}")
                    myResult = database.myQuery.fetchone()
                    print(myResult)

                    if myResult is not None:
                        if myResult[7] in 'Kunj Vihar':
                            randomm = "update myi set s_s=0 where i_id=1"
                            database.myQuery.execute(randomm)
                            database.myDatabase.commit()
                        if myResult[7] in 'Mitali Park':
                            randomm = "update myi set s_s=0 where i_id=2"
                            database.myQuery.execute(randomm)
                            database.myDatabase.commit()
                        if myResult[7] in 'Jesal Park':
                            randomm = "update myi set s_s=0 where i_id=3"
                            database.myQuery.execute(randomm)
                            database.myDatabase.commit()
                        if myResult[7] in 'Siddhivinayak temple':
                            randomm = "update myi set s_s=0 where i_id=4"
                            database.myQuery.execute(randomm)
                            database.myDatabase.commit()
                        if myResult[7] in 'Valenkani':
                            randomm = "update myi set s_s=0 where i_id=5"
                            database.myQuery.execute(randomm)
                            database.myDatabase.commit()
                        if myResult[7] in 'Agra Baug':
                            randomm = "update myi set s_s=0 where i_id=6"
                            database.myQuery.execute(randomm)
                            database.myDatabase.commit()

                        database.myQuery.execute(
                            f"delete from mypurchase where p_id={toMakeInt}")
                        database.myDatabase.commit()
                        popup.showwarning(
                            "CampusConnect", f"{toMakeInt} deleted succesfully!")
                        frame.destroy()
                        adminMainPage.AdminMainPage()
                    else:
                        popup.showwarning(
                            "CampusConnect", "Kindly Enter Valid ID!!!!")
                except:
                    popup.showwarning(
                        "CampusConnect", "Kindly Enter Valid ID!!!!")
            except:
                popup.showwarning("CampusConnect",
                                  "Oops ID Must In Integer!!")
        # warn = Label(newWindow, text="Note: Deleting ID Will Delete All Data Of The Purchaser!!",
        #              font=("Product Sans", 12))
        # warn.place(x=220, y=35)
        # warn.config(bg="white", fg="red")

        myBlock = Label(newWindow)
        myBlock.place(x=0, y=0, width=300, height=500)
        myBlock.config(bg="mediumslateblue")
        warn = Label(myBlock, text="Note: Deleting ID Will Delete\nAll Data Of The Purchaser\nFrom The Database",
                     font=("Product Sans", 13, "bold"))
        warn.place(x=40, y=205)
        warn.config(bg="mediumslateblue", fg="white")

        IdLabel = Label(newWindow, text="Enter Purchaser's ID",
                        font=("Product Sans", 16, "bold"))
        IdLabel.place(x=305+80+40+20, y=100+20)
        IdLabel.config(bg="white", fg="Slateblue")

        IdEntry = Entry(newWindow, font=("Product Sans", 16))
        IdEntry.place(x=290+80+40+20, y=140+20)
        IdEntry.config(fg="slateblue", highlightcolor="slateblue",
                       highlightthickness=1,
                       highlightbackground="slateblue")

        deleteButton = Button(newWindow, text="Delete",
                              font=("Product Sans", 14))
        deleteButton.place(x=350+80+40+20, y=190+20, width=100, height=40)
        deleteButton.config(bg="slateblue", fg="white",
                            activebackground="slateblue",
                            activeforeground="white",
                            borderwidth=0, command=toDelete)

        back = Button(newWindow, text="🢘", font=(
            "Product Sans", 30), command=toMoveBack)
        back.place(x=350+80+40+20, y=240+20, width=100, height=40)
        back.config(bg="slateblue", fg="white",
                    activebackground="slateblue",
                    activeforeground="white",
                    borderwidth=0)

        # design = Label(newWindow, font=("Product Sans", 24))
        # design.place(x=0, y=440, width=800, height=60)
        # for i in range(100):
        #     design.config(text=f"*"*i)

        frame.mainloop()


if __name__ == '__main__':
    newPage = PurchaseDelete()
