import Tkinter as tk

class Home:
    global mainwindow
    global buttonrow
    global root
    global w
    global h

    w = 640
    h = 320
    heightbuttonrow = 30
    root = tk.Tk()
    root.title('DeviceConfirmation')
    root.geometry("%dx%d+%d+%d" % (w, h, 0, 0))

    buttonrow = tk.Frame(root)
    buttonrow.place(y=0, x=270)

    # main frame
    mainwindow = tk.Frame(root)
    mainwindow.place(y=heightbuttonrow, x=0, width=w, height=(h - heightbuttonrow))

    __token = None

    def drawstaticbuttons(self):
        for widget in buttonrow.winfo_children():
            widget.destroy()
        button = tk.Button(buttonrow, text='Close', command=lambda: root.destroy())
        button.pack(side='left')

    def drawLoginPage(self):
        if self.__token is None:
            for widget in mainwindow.winfo_children():
                widget.destroy()

            loginframe = tk.Frame(mainwindow)
            loginframe.place(y=0, x=0, width=w)
            label = tk.Label(loginframe, text="login", fg="white", bg="purple", font="Helvetica 16 bold", width=w)
            label.pack()

            self.label_1 = tk.Label(loginframe, text="Username")
            self.label_2 = tk.Label(loginframe, text="Password")

            self.entry_1 = tk.Entry(loginframe)
            self.entry_2 = tk.Entry(loginframe, show="*")

            self.label_1.grid(row=0)
            self.label_2.grid(row=1)
            self.entry_1.grid(row=0, column=1)
            self.entry_2.grid(row=1, column=1)

            self.checkbox = tk.Checkbutton(self, text="Keep me logged in")
            self.checkbox.grid(columnspan=2)

            self.logbtn = tk.Button(self, text="Login", command=self._login_btn_clickked)
            self.logbtn.grid(columnspan=2)

            self.pack()
        pass

    def _login_btn_clickked(self):
        # print("Clicked")
        username = self.entry_1.get()
        password = self.entry_2.get()

        # print(username, password)

        if username == "john" and password == "password":
            tm.showinfo("Login info", "Welcome John")
        else:
            tm.showerror("Login error", "Incorrect username")


    def __init__(self):
        if self.__token is None:
            self.drawLoginPage()
        self.root.mainloop()
Home()