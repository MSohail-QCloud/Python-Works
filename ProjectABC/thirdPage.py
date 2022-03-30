import tkinter as tk
import LoginPage as lp
import seconPage as sp

class ThirdPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(bg='Tomato')

        Label = tk.Label(self,
                         text="Store some content related to your \n project or what your application made for. \n All the best!!",
                         bg="orange", font=("Arial Bold", 25))
        Label.place(x=40, y=150)

        Button = tk.Button(self, text="Home", font=("Arial", 15), command=lambda: controller.show_frame(lp.loginform))
        Button.place(x=650, y=450)

        Button = tk.Button(self, text="Back", font=("Arial", 15), command=lambda: controller.show_frame(sp.SecondPage))
        Button.place(x=100, y=450)
