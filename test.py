# frame = Tk()
#
# frame.geometry("1266x668+50+20")
# frame.minsize(1266, 668)
# frame.maxsize(1266, 668)
# frame.title("CampusConnect")
# myicon = PhotoImage(file='images/myIcon.png')
# frame.iconphoto(False, myicon)
#
#
# def loginClick():
#     frame.destroy()
#     newPage = toAsk.ToAsk()
#
#
# header = Label(frame, text="CampusConnect", font=("Product Sans", 30, "bold"))
# header.place(x=0, y=0, width=1266, height=65)
# header.config(bg="black", fg="white")
#
# loginPic = ImageTk.PhotoImage(Image.open("images/login.jpg"))
# loginLabel = Label(header, image=loginPic)
# loginLabel.place(x=20, y=5, width=50, height=50)
#
# login = Button(header, text="LOGIN", font=("Product Sans", 20), borderwidth=0,
#                activeforeground="white",
#                activebackground="black",
#                command=loginClick)
# login.place(x=77, y=5, width=80, height=50)
# login.config(bg="black", fg="white")
#
# aboutPic = ImageTk.PhotoImage(Image.open("images/info.jpg"))
# aboutLabel = Label(header, image=aboutPic)
# aboutLabel.place(x=1065, y=2, width=50, height=50)
#
# aboutUs = Button(header, text="ABOUT US", font=("Product Sans", 20), borderwidth=0,
#                  activeforeground="white",
#                  activebackground="black")
# aboutUs.place(x=1111, y=5, width=140, height=50)
# aboutUs.config(bg="black", fg="white")
# mainPic = ImageTk.PhotoImage(Image.open("images/froPage.jpg"))
#
# tosetImage = Label(frame, image=mainPic)
# tosetImage.place(x=0, y=60, width=1266, height=608)
#
# frame.mainloop()
