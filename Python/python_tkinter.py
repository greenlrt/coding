import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hello_world = tk.Button(self)
        self.hello_world["text"] = "Hello World"
        self.hello_world.pack(side="top")

def submit():
    print(text.get("1.0", tk.END))

root = tk.Tk()
root.title("This is my title")

menu = tk.Menu(root)
filemenu = tk.Menu(menu)
filemenu.add_command(label="Close", command=root.destroy)
menu.add_cascade(label="File", menu=filemenu)
root.config(menu=menu)

label = tk.Label(root, text="This is a label")
label.pack()

text = tk.Text(root)
text.pack()
text.insert(tk.END, "This is a text object")

button = tk.Button(root)
button["text"] = "This is a button"
button["command"] = submit
button.pack()

#app = Application(master=root)
#app.mainloop()

root.mainloop()
