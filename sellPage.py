
from tkinter import *
from tkinter import messagebox as popup
import mySQLConnection as dataBase
import clientLogin
import clientMain
from PIL import ImageTk, Image


class Sell:
    def __init__(self, LoginID):
        frame = Tk()

        frame.geometry("1266x668+50+20")
        frame.minsize(1266, 668)
        frame.maxsize(1266, 668)
        frame.title("Sell")
        myicon = PhotoImage(file='images/myIcon.png')
        frame.iconphoto(False, myicon)
        frame.config(bg="#4D50F1")

        newWindow = Frame(frame)
        newWindow.place(x=30, y=20, width=1206, height=628)
        newWindow.config(bg="white")

        myWall = ImageTk.PhotoImage(Image.open("images/sell.png"))
        myWallpaper = Label(newWindow, image=myWall)
        myWallpaper.place(x=0, y=0, width=500, height=628)
        myWallpaper.config(bg="black")

        dataBase.myQuery.execute("select * from mysell order by s_id")
        myResult = dataBase.myQuery.fetchall()
        lastID = ()
        for x in myResult:
            lastID = x
        myNewID = lastID[0] + 1

        def toMoveBack():
            frame.destroy()
            newPage = clientMain.ClientMain(LoginID)

        def toSubmit():
         # Title Sem  Price Donation Condition
            psuedoName = NameEntry.get()
            psuedoTitle = TitleEntry.get()
            psuedoSem = SemEntry.get()
            psuedoPrice = PriceEntry.get()
            psuedoCondition = ConditionEntry.get()
            psuedoDesc = DescEntry.get(1.0, END)
            psuedoContact = ContactEntry.get()

            Name = psuedoName.strip()
            Title = psuedoTitle.strip()
            Sem = psuedoSem.strip()
            Price = psuedoPrice.strip()
            Condition = psuedoCondition.strip()
            Desc = psuedoDesc.strip()
            Contact = psuedoContact.strip()

            if Name in "" or Title in "" or Sem in "" or Price in "" or Condition in "" or Contact in "" or Desc in "":
                popup.showwarning("CAMPUS CONNECT",
                                  "Oops! Some Field Are Left To Fill.")
                return

            if x.get() == 1:
                Dtype = "YES"
            elif x.get() == 2:
                Dtype = "NO"
            else:
                popup.showwarning("CAMPUS CONNECT",
                                  "Kindly Select Product Type !!!.")
                return

            # if y.get() == 1:
            #     Atype = "Residential"
            # elif y.get() == 2:
            #     Atype = "Commercial"
            # elif y.get() == 3:
            #     Atype = "Industrial"
            # else:
            #     popup.showwarning("Campus Connect", "Kindly Select Area Type !!!.")
            #     return

            if len(Contact) > 10:
                popup.showwarning("Campus Connect",
                                  "Contact Number is Greater Than 10 Digits.")
            if len(Contact) < 10:
                popup.showwarning("Campus Connect",
                                  "Contact Number is Lesser Than 10 Digits.")
            else:
             # Title Sem  Price Donation Condition
                try:
                    my = "insert into mysell values(?,?,?,?,?,?,?,?,?)"
                    val = (myNewID, Name, Title, Sem, Price,
                           Dtype, Contact, Condition, Desc)
                    dataBase.myQuery.execute(my, val)
                    dataBase.myDatabase.commit()
                    popup.showinfo("Campus Connect",
                                   "Data Inserted Successfully")
                    frame.destroy()
                    newPage = clientMain.ClientMain(LoginID)
                except:
                    print("abeeyy yaar")
                    popup.showwarning("Campus Connect",
                                      "Kindly Enter Valid Details!!!.")

        IdLabel = Label(newWindow, text="SELL ID : ",
                        font=("Product Sans", 14))
        IdLabel.place(x=550, y=45)
        IdLabel.config(bg="white", fg="#4D50F1")
        IdEntry = Label(newWindow, font=("Product Sans", 14), text=myNewID)
        IdEntry.place(x=730, y=45)
        IdEntry.config(width=25, fg="#4D50F1", bg="white")

        NameLabel = Label(newWindow, text="SELLER'S NAME : ",
                          font=("Product Sans", 14))
        NameLabel.place(x=550, y=95)
        NameLabel.config(bg="white", fg="#4D50F1")
        NameEntry = Entry(newWindow, font=("Product Sans", 14),
                          highlightcolor="#4D50F1", highlightbackground="#4D50F1", highlightthickness=1)
        NameEntry.place(x=730, y=95)
        NameEntry.config(width=25, fg="#4D50F1")

        TitleLabel = Label(newWindow, text="BOOK TITLE : ",
                           font=("Product Sans", 14))
        TitleLabel.place(x=550, y=145)
        TitleLabel.config(bg="white", fg="#4D50F1")
        TitleEntry = Entry(newWindow, font=("Product Sans", 14),
                           highlightcolor="#4D50F1", highlightbackground="#4D50F1", highlightthickness=1)
        TitleEntry.place(x=730, y=145)
        TitleEntry.config(width=25, fg="#4D50F1")

        SemLabel = Label(newWindow, text="SEMESTER :",
                         font=("Product Sans", 14))
        SemLabel.place(x=550, y=195)
        SemLabel.config(bg="white", fg="#4D50F1")
        SemEntry = Entry(newWindow, font=("Product Sans", 14),
                         highlightcolor="#4D50F1", highlightbackground="#4D50F1",
                         highlightthickness=1)
        SemEntry.place(x=730, y=195)
        SemEntry.config(width=25, fg="#4D50F1")

        PriceLabel = Label(newWindow, text="ASKING PRICE :",
                           font=("Product Sans", 14))
        PriceLabel.place(x=550, y=245)
        PriceLabel.config(bg="white", fg="#4D50F1")
        PriceEntry = Entry(newWindow, font=("Product Sans", 14),
                           highlightcolor="#4D50F1", highlightbackground="#4D50F1",
                           highlightthickness=1)
        PriceEntry.place(x=730, y=245)
        PriceEntry.config(width=25, fg="#4D50F1")

        DonationLabel = Label(
            newWindow, text="UP FOR DONATION : ", font=("Product Sans", 14))
        DonationLabel.place(x=550, y=295)
        DonationLabel.config(bg="white", fg="#4D50F1")
        x = IntVar()
        DonationY = Radiobutton(newWindow, text="YES",
                                variable=x, value=1, font=("Product Sans", 14))
        DonationY.place(x=730, y=295)
        DonationY.config(fg="#4D50F1", bg="white",
                         activebackground="white", activeforeground="#4D50F1")
        DonationN = Radiobutton(newWindow, text="NO",
                                variable=x, value=2, font=("Product Sans", 14))
        DonationN.place(x=840, y=295)
        DonationN.config(fg="#4D50F1", bg="white",
                         activebackground="white", activeforeground="#4D50F1")

        ConditionLabel = Label(
            newWindow, text="CONDITION : ", font=("Product Sans", 14))
        ConditionLabel.place(x=550, y=345)
        ConditionLabel.config(bg="white", fg="#4D50F1")
        ConditionEntry = Entry(newWindow, font=("Product Sans", 14),
                               highlightcolor="#4D50F1", highlightbackground="#4D50F1", highlightthickness=1)
        ConditionEntry.place(x=730, y=345)
        ConditionEntry.config(width=25, fg="#4D50F1")

        DescLabel = Label(newWindow, text="DESCRIPTION : ",
                          font=("Product Sans", 14))
        DescLabel.place(x=550, y=395)
        DescLabel.config(bg="white", fg="#4D50F1")
        DescEntry = Text(newWindow, font=("Product Sans", 14), fg="#4D50F1",
                         highlightthickness=1, highlightbackground="#4D50F1", highlightcolor="#4D50F1"
                         )
        DescEntry.place(x=730, y=395, height=130, width=200)

        ContactLabel = Label(
            newWindow, text="CONTACT NO. : ", font=("Product Sans", 14))
        ContactLabel.place(x=550, y=545)
        ContactLabel.config(bg="white", fg="#4D50F1")
        ContactEntry = Entry(newWindow, font=("Product Sans", 14),
                             highlightcolor="#4D50F1", highlightbackground="#4D50F1", highlightthickness=1)
        ContactEntry.place(x=730, y=545)
        ContactEntry.config(width=25, fg="#4D50F1")

        Submit = Button(newWindow, text="SUBMIT", font=("Product Sans", 14))
        Submit.place(x=1050, y=445)
        Submit.config(width=8, borderwidth=0, bg="#4D50F1", fg="white",
                      activebackground="orchid",
                      activeforeground="white", command=toSubmit)
        Back = Button(newWindow, text="BACK", font=("Product Sans", 14))
        Back.place(x=1050, y=495)
        Back.config(width=8, borderwidth=0, bg="#4D50F1", fg="white",
                    activebackground="#4D50F1",
                    activeforeground="white", command=toMoveBack)
        frame.mainloop()


if __name__ == "__main__":
    myPage = Sell(99)
