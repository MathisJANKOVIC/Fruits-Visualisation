import tkinter as tk
from database import collection
from visualise import plotting
# Récupérer les noms des fruits
fruits = collection.find({}, {"_id": 0, "name": 1})

# Créer une fenêtre Tkinter
root = tk.Tk()
root.title("Fruits-Visualisation")
root.geometry("570x300")
root.resizable(False, False)
# Nombre de colonnes
num_columns = 5

# Dictionnaire pour stocker les variables IntVar
vars = {}

# Pour chaque fruit, créer une case à cocher
for i, fruit in enumerate(fruits):
    var = tk.IntVar()
    c = tk.Checkbutton(root, text=fruit['name'], variable=var)
    c.grid(row=i//num_columns, column=i%num_columns)
    vars[fruit['name']] = var

# Fonction pour récupérer les noms des fruits cochés
def get_checked():
    checked = [name for name, var in vars.items() if var.get() == 1]
    fruits = collection.find({"name": {"$in": checked}})
    plotting(list(fruits))


button = tk.Button(root, text="Compare", command=get_checked)
button.grid(row=i//num_columns + 1, column=0, columnspan=num_columns, pady=(15, 0))

# Lancer la boucle Tkinter
root.mainloop()