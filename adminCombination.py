from tkinter import *
from PIL import ImageTk, Image
import adminMainPage
import mypurchaseTable
import mySellTable
import myRentTable
import myUserDetails
import purchaseSearch
import rentSearch
import sellSearch
import userSearch
import delPurchase
import delRent
import delSell
import dellUser


class AdminCombination:
    def __init__(self, pageNumber):
        frame = Tk()
        frame.geometry("1266x668+50+20")
        frame.minsize(1266, 668)
        frame.maxsize(1266, 668)
        frame.title("CampusConnect")
        myicon = PhotoImage(file='images/myIcon.png')
        frame.iconphoto(False, myicon)
        frame.config(bg="cornsilk")

        def toMoveBack():
            frame.destroy()
            adminMainPage.AdminMainPage()

        def toMoveOnPurchasePage():
            if pageNumber == 1:
                frame.destroy()
                mypurchaseTable.PurchaseTable()
            elif pageNumber == 2:
                frame.destroy()
                purchaseSearch.PurchaseSearch()
            else:
                frame.destroy()
                delPurchase.PurchaseDelete()

        def toMoveOnRentPage():
            if pageNumber == 1:
                frame.destroy()
                myRentTable.RentTable()
            elif pageNumber == 2:
                frame.destroy()
                rentSearch.RentSearch()
            else:
                frame.destroy()
                delRent.RentDelete()

        def toMoveOnSellPage():
            if pageNumber == 1:
                frame.destroy()
                mySellTable.SellTable()
            elif pageNumber == 2:
                frame.destroy()
                sellSearch.SellSearch()
            else:
                frame.destroy()
                delSell.SellDelete()

        def toMoveOnUserPage():
            if pageNumber == 1:
                frame.destroy()
                myUserDetails.UserTable()
            elif pageNumber == 2:
                frame.destroy()
                userSearch.UserSearch()
            else:
                frame.destroy()
                dellUser.UserDelete()

        pur = ImageTk.PhotoImage(Image.open("images/zpurchaseDis2.jpg"))
        myFrame1 = Label(frame, image=pur)
        myFrame1.place(x=0, y=0, width=422, height=494)
        myFrame1.config(bg="cornsilk")
        myPur = Button(frame, text="PURCHASE", font=("Product Sans", 24, "bold"), borderwidth=0,
                       command=toMoveOnPurchasePage)
        myPur.place(x=0, y=494, width=422, height=40)
        myPur.config(bg="#4D50F1", fg="white",
                     activeforeground="#4D50F1", activebackground="white")

        ren = ImageTk.PhotoImage(Image.open("images/zuser2.png"))
        myFrame2 = Label(frame, image=ren)
        myFrame2.place(x=422, y=0, width=422, height=494)
        myFrame2.config(bg="aqua")
        myRen = Button(frame, text="USER DETAILS ", font=("Product Sans", 24, "bold"), borderwidth=0,
                       command=toMoveOnRentPage)
        myRen.place(x=422, y=494, width=422, height=40)
        myRen.config(bg="#4D50F1", fg="white",
                     activeforeground="#4D50F1", activebackground="white")

        sell = ImageTk.PhotoImage(Image.open("images/zsellDis2.jpg"))
        myFrame3 = Label(frame, image=sell)
        myFrame3.place(x=844, y=0, width=422, height=494)
        mySol = Button(frame, text="SELL", font=("Product Sans", 24, "bold"), borderwidth=0,
                       command=toMoveOnSellPage)
        mySol.place(x=844, y=494, width=422, height=40)
        mySol.config(bg="#4D50F1", fg="white",
                     activeforeground="#4D50F1", activebackground="white")

        myInfo = Button(frame, text=f"USER", font=("Product Sans", 22, "bold"))
        myInfo.place(x=0, y=534, width=1266, height=78.2)
        myInfo.config(bg="white", fg="#4D50F1", borderwidth=0, activeforeground="#4D50F1",
                      activebackground="white", command=toMoveOnUserPage)

        Back = Button(frame, text="ç", font=(
            "Wingdings", 30, "bold"), command=toMoveBack)
        Back.place(x=0, y=612.2, width=1266, height=55)
        Back.config(bg="#4D50F1", fg="white", borderwidth=0, activeforeground="white",
                    activebackground="mediumpurple")

        frame.mainloop()


if __name__ == "__main__":
    newPage = AdminCombination(1)
