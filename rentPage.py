
from tkinter import *
from tkinter import messagebox as popup
import mySQLConnection as dataBase
import clientLogin
import clientMain
from PIL import ImageTk, Image


class Rent:
    def __init__(self, LoginID):
        frame = Tk()

        frame.geometry("1266x668+50+20")
        frame.minsize(1266, 668)
        frame.maxsize(1266, 668)
        frame.title("CampusConnect")
        myicon = PhotoImage(file='images/myIcon.png')
        frame.iconphoto(False, myicon)
        frame.config(bg="indigo")

        newWindow = Frame(frame)
        newWindow.place(x=30, y=20, width=1206, height=628)
        newWindow.config(bg="white")

        myWall = ImageTk.PhotoImage(Image.open("images/rentInside.jpg"))
        myWallpaper = Label(newWindow, image=myWall)
        myWallpaper.place(x=0, y=0, width=500, height=628)
        myWallpaper.config(bg="black")

        dataBase.myQuery.execute("select * from myrent order by r_id")
        myResult = dataBase.myQuery.fetchall()
        lastID = ()
        for x in myResult:
            lastID = x
        myNewID = lastID[0] + 1

        def toMoveBack():
            frame.destroy()
            newPage = clientMain.ClientMain(LoginID)

        def toSubmit():

            psuedoName = NameEntry.get()
            psuedoAdd = AddressEntry.get()
            psuedoAreaSq = AreaMeasureEntry.get()
            psuedoLocation = LocationEntry.get()
            psuedoLandmark = LandMarkEntry.get()
            psuedoUp = UpperPriceEntry.get()
            psuedoLp = LowerPriceEntry.get()
            psuedoCno = ContactEntry.get()

            Name = psuedoName.strip()
            Add = psuedoAdd.strip()
            AreaSq = psuedoAreaSq.strip()
            Location = psuedoLocation.strip()
            LandMark = psuedoLandmark.strip()
            Up = psuedoUp.strip()
            Lp = psuedoLp.strip()
            Cno = psuedoCno.strip()

            if Name in "" or Add in "" or AreaSq in "" or Location in "" or LandMark in "" or Up in "" or Lp in "" or Cno in "":
                popup.showwarning("CampusConnect",
                                  "Oops! Some Field Are Left To Fill.")
                return

            if x.get() == 1:
                Btype = "Flat"
            elif x.get() == 2:
                Btype = "Bungalow"
            else:
                popup.showwarning("CampusConnect",
                                  "Kindly Select Building Type !!!.")
                return

            if y.get() == 1:
                Atype = "Residential"
            elif y.get() == 2:
                Atype = "Commercial"
            elif y.get() == 3:
                Atype = "Industrial"
            else:
                popup.showwarning("CampusConnect",
                                  "Kindly Select Area Type !!!.")
                return

            if len(Cno) > 10:
                popup.showwarning("CampusConnect",
                                  "Contact Number is Greater Than 10 Digits.")
            if len(Cno) < 10:
                popup.showwarning("CampusConnect",
                                  "Contact Number is Lesser Than 10 Digits.")
            else:
                try:
                    Check1 = float(AreaSq)
                    Check2 = float(Up)
                    Check3 = float(Lp)
                    Check4 = int(Cno)
                    try:
                        my = "insert into myrent values(?,?,?,?,?,?,?,?,?,?,?)"
                        val = (myNewID, Name, Add, Btype, Atype,
                               AreaSq, Location, LandMark, Up, Lp, Cno)
                        dataBase.myQuery.execute(my, val)
                        dataBase.myDatabase.commit()
                        popup.showinfo("CampusConnect",
                                       "Data Inserted Successfully")
                        frame.destroy()
                        newPage = clientMain.ClientMain(LoginID)
                    except:
                        print("abeeyy yaar")
                except:
                    popup.showwarning("CampusConnect",
                                      "Kindly Enter Valid Details!!!.")

        IdLabel = Label(newWindow, text="Rent ID : ",
                        font=("Product Sans", 14))
        IdLabel.place(x=550, y=45)
        IdLabel.config(bg="white", fg="dark magenta")
        IdEntry = Label(newWindow, font=("Product Sans", 14), text=myNewID)
        IdEntry.place(x=730, y=45)
        IdEntry.config(width=25, fg="dark magenta", bg="white")

        NameLabel = Label(newWindow, text="Owner's Name : ",
                          font=("Product Sans", 14))
        NameLabel.place(x=550, y=95)
        NameLabel.config(bg="white", fg="dark magenta")
        NameEntry = Entry(newWindow, font=("Product Sans", 14),
                          highlightcolor="dark magenta", highlightbackground="dark magenta", highlightthickness=1)
        NameEntry.place(x=730, y=95)
        NameEntry.config(width=25, fg="dark magenta")

        AddressLabel = Label(
            newWindow, text="Owner's Address : ", font=("Product Sans", 14))
        AddressLabel.place(x=550, y=145)
        AddressLabel.config(bg="white", fg="dark magenta")
        AddressEntry = Entry(newWindow, font=("Product Sans", 14),
                             highlightcolor="dark magenta", highlightbackground="dark magenta", highlightthickness=1)
        AddressEntry.place(x=730, y=145)
        AddressEntry.config(width=25, fg="dark magenta")

        BuildingTypeLabel = Label(
            newWindow, text="Building Type : ", font=("Product Sans", 14))
        BuildingTypeLabel.place(x=550, y=195)
        BuildingTypeLabel.config(bg="white", fg="dark magenta")
        x = IntVar()
        Bplot = Radiobutton(newWindow, text="FLAT", variable=x,
                            value=1, font=("Product Sans", 14))
        Bplot.place(x=730, y=195)
        Bplot.config(fg="dark magenta", bg="white",
                     activebackground="white", activeforeground="dark magenta")
        Bgplot = Radiobutton(newWindow, text="BUNGALOW",
                             variable=x, value=2, font=("Product Sans", 14))
        Bgplot.place(x=840, y=195)
        Bgplot.config(fg="dark magenta", bg="white",
                      activebackground="white", activeforeground="dark magenta")

        AreaTypeLabel = Label(
            newWindow, text="Area Type : ", font=("Product Sans", 14))
        AreaTypeLabel.place(x=550, y=245)
        AreaTypeLabel.config(bg="white", fg="dark magenta")
        y = IntVar()
        Residential = Radiobutton(
            newWindow, text="RESIDENTIAL", variable=y, value=1, font=("Product Sans", 14))
        Residential.place(x=660, y=245)
        Residential.config(fg="dark magenta", bg="white",
                           activebackground="white", activeforeground="dark magenta")
        Commercial = Radiobutton(
            newWindow, text="COMMERCIAL", variable=y, value=2, font=("Product Sans", 14))
        Commercial.place(x=840, y=245)
        Commercial.config(fg="dark magenta", bg="white",
                          activebackground="white", activeforeground="dark magenta")
        Industrial = Radiobutton(
            newWindow, text="INDUSTRIAL", variable=y, value=3, font=("Product Sans", 14))
        Industrial.place(x=1020, y=245)
        Industrial.config(fg="dark magenta", bg="white",
                          activebackground="white", activeforeground="dark magenta")

        AreaMeasureLabel = Label(
            newWindow, text="Area (Sq.Ft) : ", font=("Product Sans", 14))
        AreaMeasureLabel.place(x=550, y=295)
        AreaMeasureLabel.config(bg="white", fg="dark magenta")
        AreaMeasureEntry = Entry(newWindow, font=("Product Sans", 14),
                                 highlightcolor="dark magenta", highlightbackground="dark magenta",
                                 highlightthickness=1)
        AreaMeasureEntry.place(x=730, y=295)
        AreaMeasureEntry.config(width=25, fg="dark magenta")

        LocationLabel = Label(newWindow, text="Location : ",
                              font=("Product Sans", 14))
        LocationLabel.place(x=550, y=345)
        LocationLabel.config(bg="white", fg="dark magenta")
        LocationEntry = Entry(newWindow, font=("Product Sans", 14),
                              highlightcolor="dark magenta", highlightbackground="dark magenta", highlightthickness=1)
        LocationEntry.place(x=730, y=345)
        LocationEntry.config(width=25, fg="dark magenta")

        LandMarkLabel = Label(newWindow, text="Landmark : ",
                              font=("Product Sans", 14))
        LandMarkLabel.place(x=550, y=395)
        LandMarkLabel.config(bg="white", fg="dark magenta")
        LandMarkEntry = Entry(newWindow, font=("Product Sans", 14),
                              highlightcolor="dark magenta", highlightbackground="dark magenta", highlightthickness=1)
        LandMarkEntry.place(x=730, y=395)
        LandMarkEntry.config(width=25, fg="dark magenta")

        UpperPriceLabel = Label(
            newWindow, text="Upper Price : ", font=("Product Sans", 14))
        UpperPriceLabel.place(x=550, y=445)
        UpperPriceLabel.config(bg="white", fg="dark magenta")
        UpperPriceEntry = Entry(newWindow, font=("Product Sans", 14),
                                highlightcolor="dark magenta", highlightbackground="dark magenta", highlightthickness=1)
        UpperPriceEntry.place(x=730, y=445)
        UpperPriceEntry.config(width=25, fg="dark magenta")

        LowerPriceLabel = Label(
            newWindow, text="Lower Price : ", font=("Product Sans", 14))
        LowerPriceLabel.place(x=550, y=495)
        LowerPriceLabel.config(bg="white", fg="dark magenta")
        LowerPriceEntry = Entry(newWindow, font=("Product Sans", 14),
                                highlightcolor="dark magenta", highlightbackground="dark magenta", highlightthickness=1)
        LowerPriceEntry.place(x=730, y=495)
        LowerPriceEntry.config(width=25, fg="dark magenta")

        ContactLabel = Label(
            newWindow, text="Contact No. : ", font=("Product Sans", 14))
        ContactLabel.place(x=550, y=545)
        ContactLabel.config(bg="white", fg="dark magenta")
        ContactEntry = Entry(newWindow, font=("Product Sans", 14),
                             highlightcolor="dark magenta", highlightbackground="dark magenta", highlightthickness=1)
        ContactEntry.place(x=730, y=545)
        ContactEntry.config(width=25, fg="dark magenta")

        Submit = Button(newWindow, text="SUBMIT", font=("Product Sans", 14))
        Submit.place(x=1050, y=350)
        Submit.config(width=8, borderwidth=0, bg="indigo", fg="white",
                      activebackground="orchid",
                      activeforeground="white", command=toSubmit)
        Back = Button(newWindow, text="BACK", font=("Product Sans", 14))
        Back.place(x=1050, y=400)
        Back.config(width=8, borderwidth=0, bg="indigo", fg="white",
                    activebackground="orchid",
                    activeforeground="white", command=toMoveBack)
        frame.mainloop()


if __name__ == "__main__":
    myPage = Rent(99)
