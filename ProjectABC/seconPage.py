import tkinter as tk
from tkinter import messagebox
import LoginPage as lp
import thirdPage as tp
import dbPage as dp
# from PIL import Image, ImageTk  # pip install pillow



class SecondPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        #        load = Image.open("img2.jpg")
        #        photo = ImageTk.PhotoImage(load)
        #        label = tk.Label(self, image=photo)
        #        label.image = photo
        #        label.place(x=0, y=0)

        lc=tk.Label(self, text="Logged User: ", font=("Arial", 10), bg='ivory')
        lc.place(x=0, y=0)
        LblLoguser = tk.Label(self, text="abc", font=("Arial", 10), bg='ivory')
        LblLoguser.place(x=80, y=0)

        if dp.isSqlite3Db('appdb.db'):
            dp.connectdb()
            LblLoguser.config(text=dp.getsessionuser())

        lblRack = tk.Label(self, text="Rack#:", font=("Arial", 12), bg="deep sky blue")
        lblRack.place(x=10, y=50)
        txtRack = tk.Entry(self, width=40, bd=1)
        txtRack.place(x=110, y=50)

        lblDes = tk.Label(self, text="Description:", font=("Arial", 12), bg="deep sky blue")
        lblDes.place(x=10, y=80)
        txtDescription = tk.Entry(self, width=40, bd=1)
        txtDescription.place(x=110, y=90)

        lblQty = tk.Label(self, text="Balance Qty:", font=("Arial", 12), bg="deep sky blue")
        lblQty.place(x=10, y=110)
        txtQty = tk.Entry(self, width=40, bd=1)
        txtQty.place(x=110, y=110)

        lblUQty = tk.Label(self, text="Issue Qty:", font=("Arial", 12), bg="deep sky blue")
        lblUQty.place(x=10, y=140)
        txtUsedQty = tk.Entry(self, width=20, bd=1)
        txtUsedQty.place(x=140, y=140)
        txtUsedQty.insert(0, 1)

        def AddQty():
            txt = (txtUsedQty.get())
            if txt != "":
                defaultQty = int(txt)
                defaultQty += 1
                txtUsedQty.insert(0, defaultQty)
            else:
                txtUsedQty.insert(0, 1)

        btnAddComp = tk.Button(self, text="+", font=("Arial", 12), bg="#ffc22a", command=AddQty())
        btnAddComp.place(x=110, y=140)

        btnMinusComp = tk.Button(self, text="-", font=("Arial", 12), bg="#ffc22a", command=AddQty())
        btnMinusComp.place(x=210, y=140)

        def AddCompon():
            window = tk.Tk()
            window.resizable(0, 0)
            window.configure(bg="deep sky blue")
            window.title("Add Components")
            l1 = tk.Label(window, text="Rack#:", font=("Arial", 15), bg="deep sky blue")
            l1.place(x=10, y=10)
            t1 = tk.Entry(window, width=30, bd=5)
            t1.place(x=200, y=10)

            l2 = tk.Label(window, text="Description:", font=("Arial", 15), bg="deep sky blue")
            l2.place(x=10, y=60)
            t2 = tk.Entry(window, width=50, bd=5)
            t2.place(x=200, y=60)

            l3 = tk.Label(window, text="Qty:", font=("Arial", 15), bg="deep sky blue")
            l3.place(x=10, y=110)
            t3 = tk.Entry(window, width=30, bd=5)
            t3.place(x=200, y=110)

            def Add():
                if t1.get() != "" or t2.get() != "" or t3.get() != "":
                    # f.write(t1.get() + "," + t2.get() + "\n")
                    abc = (t1.get(), t2.get(), t3.get())
                    dp.addComponents(abc)
                    messagebox.showinfo("Info", "Your addition is successful!!")
                    window.destroy()
                else:
                    messagebox.showinfo("Error", "Please fill the complete field!!")

            b1 = tk.Button(window, text="Add Detail", font=("Arial", 15), bg="#ffc22a", command=Add)
            b1.place(x=170, y=150)

            window.geometry("700x220")
            window.mainloop()

        Button = tk.Button(self, text="Next", font=("Arial", 15), command=lambda: controller.show_frame(tp.ThirdPage))
        Button.place(x=650, y=450)

        B2 = tk.Button(self, text="Add Components", bg="dark orange", font=("Arial", 15), command=AddCompon)
        B2.place(x=150, y=450)

        Button = tk.Button(self, text="Back", font=("Arial", 15), command=lambda: controller.show_frame(lp.loginform))
        Button.place(x=100, y=450)
