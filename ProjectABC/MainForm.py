import tkinter as tk
from tkinter import messagebox
# from PIL import Image, ImageTk  # pip install pillow
import LoginPage as lp
import seconPage as sp
import thirdPage as tp
import dbPage as dp


class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a window
        window = tk.Frame(self)
        window.pack()

        window.grid_rowconfigure(0, minsize=500)
        window.grid_columnconfigure(0, minsize=800)



        self.frames = {}
        for F in (lp.loginform, sp.SecondPage, tp.ThirdPage):
            frame = F(window, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.verifydb()
        self.show_frame(lp.loginform)


    def verifydb(self):
        if dp.isSqlite3Db('appdb.db'):
            dp.connectdb()
        else:
            dp.createdb()
            messagebox.showinfo("Database", "New DB Created")

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()
        self.title("Components Management System")


app = Application()
app.maxsize(1024, 600)
app.state('zoomed')
app.mainloop()
# https://ishwargautam.blogspot.com/2021/10/multiple-page-gui-window-with-login.html
# https://www.youtube.com/watch?v=QfhF9BnmN6E