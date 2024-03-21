from visualise_fruits import plot
from database import collection
import load_data
import tkinter

load_data.main()

root = tkinter.Tk()
root.title("Fruits-Visualisation")

root.iconbitmap('logo.ico')
root.geometry("570x300")
root.resizable(False, False)

num_columns = 5

# Dictionnaire pour stocker les variables IntVar
vars = {}
fruits = collection.find({}, {"_id": 0, "name": 1})

# Pour chaque fruit, créer une case à cocher
for i, fruit in enumerate(fruits):
    var = tkinter.IntVar()
    c = tkinter.Checkbutton(root, text=fruit['name'], variable=var)
    c.grid(row=i//num_columns, column=i%num_columns)
    vars[fruit['name']] = var

def get_checked():
    checked = [name for name, var in vars.items() if var.get() == 1]
    fruits = collection.find({"name": {"$in": checked}})
    plot(list(fruits))

button = tkinter.Button(root, text="Compare", command=get_checked)
button.grid(row=i//num_columns + 1, column=0, columnspan=num_columns, pady=(15, 0))

root.mainloop()