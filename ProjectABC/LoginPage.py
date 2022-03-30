import tkinter as tk
from tkinter import messagebox
# from PIL import Image, ImageTk  # pip install pillow7
import seconPage as sp
import thirdPage as tp
import dbPage as dp


class loginform(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        #        load = Image.open("img1.jpg")
        #        photo = ImageTk.PhotoImage(load)
        #        label = tk.Label(self, image=photo)
        #        label.image = photo
        #        label.place(x=0, y=0)

        border = tk.LabelFrame(self, text='Login', bg='ivory', bd=10, font=("Arial", 20))
        border.pack(fill="both", expand="yes", padx=150, pady=150)

        L1 = tk.Label(border, text="Username", font=("Arial Bold", 15), bg='ivory')
        L1.place(x=50, y=20)
        T1 = tk.Entry(border, width=30, bd=5)
        T1.place(x=180, y=20)

        L2 = tk.Label(border, text="Password", font=("Arial Bold", 15), bg='ivory')
        L2.place(x=50, y=80)
        T2 = tk.Entry(border, width=30, show='*', bd=5)
        T2.place(x=180, y=80)

        # check db
        def verify():
            try:
                if dp.verifylogin(T1.get(), T2.get()):
                    messagebox.showinfo("Info", "Login Successfull")
                    T2.delete(0, "end")
                    controller.show_frame(sp.SecondPage)
                else:
                    messagebox.showinfo("info", "Re login")
            except:
                messagebox.showinfo("Error", "Please provide correct username and password!!")

        B1 = tk.Button(border, text="Submit", font=("Arial", 15), command=verify)
        B1.place(x=320, y=115)

        def register():
            window = tk.Tk()
            window.resizable(0, 0)
            window.configure(bg="deep sky blue")
            window.title("Register")
            l1 = tk.Label(window, text="Username:", font=("Arial", 15), bg="deep sky blue")
            l1.place(x=10, y=10)
            t1 = tk.Entry(window, width=30, bd=5)
            t1.place(x=200, y=10)

            l2 = tk.Label(window, text="Password:", font=("Arial", 15), bg="deep sky blue")
            l2.place(x=10, y=60)
            t2 = tk.Entry(window, width=30, show="*", bd=5)
            t2.place(x=200, y=60)

            l3 = tk.Label(window, text="Confirm Password:", font=("Arial", 15), bg="deep sky blue")
            l3.place(x=10, y=110)
            t3 = tk.Entry(window, width=30, show="*", bd=5)
            t3.place(x=200, y=110)

            def check():
                if t1.get() != "" or t2.get() != "" or t3.get() != "":
                    if t2.get() == t3.get():
                        with open("credential.txt", "a") as f:
                            f.write(t1.get() + "," + t2.get() + "\n")
                            messagebox.showinfo("Welcome", "You are registered successfully!!")
                    else:
                        messagebox.showinfo("Error", "Your password didn't get match!!")
                else:
                    messagebox.showinfo("Error", "Please fill the complete field!!")

            b1 = tk.Button(window, text="Sign in", font=("Arial", 15), bg="#ffc22a", command=check)
            b1.place(x=170, y=150)

            window.geometry("470x220")
            window.mainloop()

        B2 = tk.Button(self, text="Register", bg="dark orange", font=("Arial", 15), command=register)
        B2.place(x=650, y=20)
