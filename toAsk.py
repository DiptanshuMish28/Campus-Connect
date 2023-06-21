from tkinter import *
from PIL import ImageTk, Image
import loginAsa
import clientLogin
import adminLogin


class ToAsk:
    def __init__(self):
        frame = Tk()

        frame.geometry("1266x668+50+20")
        frame.minsize(1266, 668)
        frame.maxsize(1266, 668)
        frame.title("CampusConnect")
        myicon = PhotoImage(file='images/zmyicon2.png')
        frame.iconphoto(False, myicon)
        frame.config(bg="purple")

        def clientClick():
            frame.destroy()
            clientLogin.ClientLogin()

        def adminClick():
            frame.destroy()
            adminLogin.AdminLogin()

        myWallpaper = ImageTk.PhotoImage(Image.open("images/zareyouaa2.jpg"))
        areYouA = Label(frame, image=myWallpaper)
        areYouA.place(x=0, y=0)

        newWindow = Frame(frame)
        newWindow.place(x=233, y=84, width=800, height=500)
        newWindow.config(bg="white")

        areYouA = Label(newWindow, text="Select your profile",
                        font=("Product Sans", 35, "bold"))
        areYouA.place(x=125, y=40, width=500, height=60)
        areYouA.config(bg="white")

        clientPic = ImageTk.PhotoImage(Image.open("images/zclient2.jpg"))
        clientButton = Button(newWindow, image=clientPic, command=clientClick)
        clientButton.place(x=50, y=120, width=300, height=300)
        clientButton.config(borderwidth=0)

        adminPic = ImageTk.PhotoImage(Image.open("images/zadmin2.jpg"))
        adminButton = Button(newWindow, image=adminPic, command=adminClick)
        adminButton.place(x=450, y=120, width=300, height=300)
        adminButton.config(borderwidth=0)

        clientLabel = Label(newWindow, text="Student",
                            font=("Product Sans", 16, "bold"))
        clientLabel.place(x=168, y=440)
        clientLabel.config(bg="white")

        adminLabel = Label(newWindow, text="Admin",
                           font=("Product Sans", 16, "bold"))
        adminLabel.place(x=568, y=440)
        adminLabel.config(bg="white")

        def buttonClick():
            frame.destroy()
            newPage = loginAsa.LoginAsA()

        button = Button(frame, command=buttonClick, text="ç",
                        font=("Wingdings", 30, "bold"))
        button.place(x=20, y=30, width=100, height=40)
        button.config(bg="white", borderwidth=1)
        frame.mainloop()


if __name__ == '__main__':
    ask = ToAsk()
