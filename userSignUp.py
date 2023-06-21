from tkinter import *
from PIL import ImageTk, Image
import mySQLConnection as dataBase
import clientLogin
from tkinter import messagebox as popup

# create class user signup


class UserSignUp:
    def __init__(self):
        frame = Tk()
        frame.geometry("1266x668+50+20")
        frame.minsize(1266, 668)
        frame.maxsize(1266, 668)
        frame.title("CampusConnect")
        frame.config(bg="midnightblue")
        myGender = "Love"

        # select all details from the myUser table and arrange in asc, then go to the last row and do +1, thats the new id that needs to be assigned.
        dataBase.myQuery.execute("select * from myUser order by user_id")
        myResult = dataBase.myQuery.fetchall()
        lastID = ()
        for x in myResult:
            lastID = x
        myNewID = lastID[0] + 1

        def toSubmit():
            global myGender
            psuedoName = userName.get()
            psuedoPass = userPass.get()
            psuedoPassC = userPassC.get()
            psuedoMobile = userPhno.get()
            psuedoAdd = userAddress.get(1.0, END)
            psuedoCurrsem = userCurrsem.get()
            psuedoDept = userDept.get()
            psuedoEmail = userEmail.get()

            Name = psuedoName.strip()
            Pass = psuedoPass.strip()
            PassC = psuedoPassC.strip()
            Mobile = psuedoMobile.strip()
            Add = psuedoAdd.strip()
            Currsem = psuedoCurrsem.strip()
            Dept = psuedoDept.strip()
            Email = psuedoEmail.strip()

            if Name in "" or Pass in "" or PassC in "" or Mobile in "" or Add in "" or Currsem in "" or Dept in "" or Email in "":
                popup.showwarning("CampusConnect",
                                  "Oops! Some Field Are Left To Fill.")
                return
            if PassC not in Pass or Pass not in PassC:
                popup.showwarning("CampusConnect", "Confirm Password Doesn't Matched With Original "
                                  "Password.")
                return

            if x.get() == 1:
                myGender = "Male"
            elif x.get() == 2:
                myGender = "Female"
            else:
                popup.showwarning("CampusConnect",
                                  "Kindly select gender field.")
                return

            if len(Mobile) > 10:
                popup.showwarning("CampusConnect",
                                  "Contact Number is Greater Than 10 Digits.")
                return

            if len(Mobile) < 10:
                popup.showwarning("CampusConnect",
                                  "Contact Number is Lesser Than 10 Digits.")
                return

            if len(Add) > 300:
                popup.showwarning("CampusConnect",
                                  "Address Field is Greater Than 300 Digits.")
            else:
                try:
                    myQuery = "insert into myUser values(?, ?, ?, ?, ?, ?, ?, ?, ?) "
                    values = (myNewID, Name, Pass, myGender,
                              Add, Mobile, Currsem, Dept, Email)
                    dataBase.myQuery.execute(myQuery, values)
                    dataBase.myDatabase.commit()
                    frame.destroy()
                    newPage = clientLogin.ClientLogin()
                except:
                    popup.showwarning(
                        "CampusConnect", "EXCEPTION OCCURED")

        def toMoveBack():
            frame.destroy()
            newPage = clientLogin.ClientLogin()

        newWindow = Frame(frame)
        newWindow.place(x=30, y=20, width=1206, height=628)
        newWindow.config(bg="white")

        myWall = ImageTk.PhotoImage(Image.open("images/zuserSignUp2.png"))
        myWallpaper = Label(newWindow, image=myWall)
        myWallpaper.place(x=0, y=0, width=500, height=628)
        myWallpaper.config(bg="black")

        userIDLabel = Label(newWindow, text="USER ID : ",
                            font=("Product Sans", 14))
        userIDLabel.place(x=590, y=45)
        userIDLabel.config(bg="white", fg="midnightblue")
        userID = Label(newWindow, text=myNewID,
                       font=("Product Sans", 14, "bold"))
        userID.place(x=690, y=45, height=25, width=200)
        userID.config(bg="white", fg="midnightblue")

        userNameLabel = Label(
            newWindow, text="USER NAME : ", font=("Product Sans", 14))
        userNameLabel.place(x=557, y=100)
        userNameLabel.config(bg="white", fg="midnightblue")
        userName = Entry(newWindow, font=("Product Sans", 14), fg="midnightblue",
                         highlightthickness=1, highlightbackground="midnightblue", highlightcolor="midnightblue"
                         )
        userName.place(x=690, y=100, height=25, width=200)

        userPassLabel = Label(newWindow, text="PASSWORD : ",
                              font=("Product Sans", 14))
        userPassLabel.place(x=557, y=155)
        userPassLabel.config(bg="white", fg="midnightblue")

        userPass = Entry(newWindow, font=("Product Sans", 14), fg="midnightblue",
                         highlightthickness=1, highlightbackground="midnightblue", highlightcolor="midnightblue"
                         )
        userPass.place(x=690, y=155, height=25, width=200)

        userPassCLabel = Label(
            newWindow, text="CONFIRM PASSWORD : ", font=("Product Sans", 14))
        userPassCLabel.place(x=557, y=210)
        userPassCLabel.config(bg="white", fg="midnightblue")
        userPassC = Entry(newWindow, font=("Product Sans", 14), fg="midnightblue",
                          highlightthickness=1, highlightbackground="midnightblue", highlightcolor="midnightblue"
                          )
        userPassC.place(x=780, y=210, height=25, width=200)

        userGender = Label(newWindow, text="GENDER : ",
                           font=("Product Sans", 14))
        userGender.place(x=557, y=265)
        userGender.config(bg="white", fg="midnightblue")
        x = IntVar()
        # PY_VAR0
        GenderM = Radiobutton(newWindow, text="Male", variable=x, value=1, font=("Product Sans", 14), fg="midnightblue",
                              bg="white")
        GenderM.place(x=660, y=265)
        GenderF = Radiobutton(newWindow, text="Female", variable=x, value=2, font=("Product Sans", 14), fg="midnightblue",
                              bg="white")
        GenderF.place(x=740, y=265)

        userPhnoLabel = Label(
            newWindow, text="PHONE NO. : ", font=("Product Sans", 14))
        userPhnoLabel.place(x=557, y=320)
        userPhnoLabel.config(bg="white", fg="midnightblue")
        userPhno = Entry(newWindow, font=("Product Sans", 14), fg="midnightblue",
                         highlightthickness=1, highlightbackground="midnightblue", highlightcolor="midnightblue")
        userPhno.place(x=690, y=320, height=25, width=200)

        userAddressLabel = Label(
            newWindow, text="LOCATION : ", font=("Product Sans", 14))
        userAddressLabel.place(x=557, y=375)
        userAddressLabel.config(bg="white", fg="midnightblue")
        userAddress = Text(newWindow, font=("Product Sans", 14), fg="midnightblue",
                           highlightthickness=1, highlightbackground="midnightblue", highlightcolor="midnightblue"
                           )
        userAddress.place(x=680, y=375, height=25, width=200)

        # warn = Label(newWindow, text="Maximum : 300 Words.")
        # warn.place(x=690, y=480)
        # warn.config(fg="red", bg="white")

        userCurrsemLabel = Label(
            newWindow, text="CURRENT SEM : ", font=("Product Sans", 14))
        userCurrsemLabel.place(x=557, y=430)
        userCurrsemLabel.config(bg="white", fg="midnightblue")
        userCurrsem = Entry(newWindow, font=("Product Sans", 14), fg="midnightblue",
                            highlightthickness=0.5, highlightbackground="midnightblue", highlightcolor="midnightblue",
                            )
        userCurrsem.place(x=715, y=430, height=25, width=200)

        userDeptLabel = Label(
            newWindow, text="DEPARTMENT : ", font=("Product Sans", 14))
        userDeptLabel.place(x=557, y=485)
        userDeptLabel.config(bg="white", fg="midnightblue")
        userDept = Entry(newWindow, font=("Product Sans", 14), fg="midnightblue",
                         highlightthickness=0.5, highlightbackground="midnightblue", highlightcolor="midnightblue",
                         )
        userDept.place(x=715, y=485, height=25, width=200)

        userEmailLabel = Label(newWindow, text="EMAIL : ",
                               font=("Product Sans", 14))
        userEmailLabel.place(x=557, y=540)
        userEmailLabel.config(bg="white", fg="midnightblue")
        userEmail = Entry(newWindow, font=("Product Sans", 14), fg="midnightblue",
                          highlightthickness=0.5, highlightbackground="midnightblue", highlightcolor="midnightblue",
                          )
        userEmail.place(x=650, y=540, height=25, width=200)

        submit = Button(newWindow, text="SUBMIT", font=(
            "Product Sans", 14), command=toSubmit)
        submit.place(x=803, y=590, height=30, width=100)
        submit.config(bg="midnightblue", fg="white",
                      activeforeground="midnightblue")

        myicon = PhotoImage(file='images/zmyicon2.png')
        frame.iconphoto(False, myicon)

        button = Button(newWindow, command=toMoveBack,
                        text="RETURN", font=("Product Sans", 14))
        button.place(x=683, y=590, height=30, width=100)
        button.config(bg="midnightblue", fg="white",
                      activeforeground="midnightblue")

        frame.mainloop()


if __name__ == "__main__":
    myWindow = UserSignUp()
