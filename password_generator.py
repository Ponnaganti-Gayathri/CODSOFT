import string
import random
from tkinter import *
from tkinter import messagebox


class GUI():
    def __init__(self, master):
        self.master = master
        self.username = StringVar()
        self.passwordlen = IntVar()
        self.generatedpassword = StringVar()
        self.n_username = StringVar()
        self.n_generatedpassword = StringVar()
        self.n_passwordlen = IntVar()

        root.title('Password Generator')
        root.geometry('660x500')
        root.config(bg='#A3E4D7')
        root.resizable(True, True)

        self.label = Label(text="PASSWORD GENERATOR", anchor=N, fg='black', bg='#BB8FCE',
                           font='qanaya 24 bold')
        self.label.grid(row=0, column=0, columnspan=2)

        self.user = Label(text="Enter User Name: ", font='qanaya 20 bold', bg='#F1948A', fg='black')
        self.user.grid(row=1, column=0)

        self.textfield = Entry(textvariable=self.n_username, font='times 20', bd=6, relief='ridge', bg='#FFFFFF')
        self.textfield.grid(row=1, column=1)
        self.textfield.focus_set()

        self.length = Label(text="Enter Password Length: ", font='qanaya 20 bold', bg='#F1948A', fg='black')
        self.length.grid(row=2, column=0)

        self.length_textfield = Entry(textvariable=self.n_passwordlen, font='times 20', bd=6, relief='ridge',
                                      bg='#FFFFFF')
        self.length_textfield.grid(row=2, column=1)

        self.generated_password = Label(text="Generated Password: ", font='qanaya 20 bold', bg='#F1948A', fg='black')
        self.generated_password.grid(row=3, column=0)

        self.generated_password_textfield = Entry(textvariable=self.n_generatedpassword, font='times 20', bd=6,
                                                  relief='ridge', fg='#DC143C', bg='#FFFFFF')
        self.generated_password_textfield.grid(row=3, column=1)

        self.generate = Button(text="GENERATE PASSWORD", bd=3, relief='solid', padx=1, pady=1, font='qanaya 15 bold',
                               fg='#68228B', bg='#58D68D', command=self.generate_pass)
        self.generate.grid(row=4, column=1)

        self.reset = Button(text="RESET", bd=3, relief='solid', padx=1, pady=1, font='Helvetica 15 bold italic',
                            fg='#F5B041', bg='#D35400', command=self.reset_fields)
        self.reset.grid(row=5, column=1)

    def generate_pass(self):
        upper = string.ascii_uppercase
        lower = string.ascii_lowercase
        chars = "@#%&()\"?!"
        numbers = "1234567890"

        name = self.textfield.get()
        length = self.length_textfield.get()

        if name == "":
            messagebox.showerror("Error", "Name cannot be empty")
            return

        if not name.isalpha():
            messagebox.showerror("Error", "Name must be a string")
            self.textfield.delete(0, END)
            return

        length = int(length)

        if length < 6:
            messagebox.showerror("Error", "Password must be at least 6 characters long")
            self.textfield.delete(0, END)
            return

        u = random.randint(1, length - 3)
        l = random.randint(1, length - 2 - u)
        c = random.randint(1, length - 1 - u - l)
        n = length - u - l - c

        password = random.sample(upper, u) + random.sample(lower, l) + random.sample(chars, c) + random.sample(numbers,
                                                                                                               n)
        random.shuffle(password)
        gen_passwd = "".join(password)
        self.n_generatedpassword.set(gen_passwd)

    def reset_fields(self):
        self.textfield.delete(0, END)
        self.length_textfield.delete(0, END)
        self.generated_password_textfield.delete(0, END)


if __name__ == '__main__':
    root = Tk()
    pass_gen = GUI(root)
    root.mainloop()