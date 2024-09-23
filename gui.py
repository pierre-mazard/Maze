import tkinter as tk
from tkinter import filedialog
import random

def generate_maze(n):
    maze = [['#' for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if random.choice([True, False]):
                maze[i][j] = '.'
    maze[0][0] = '.'  # Entrée
    maze[n-1][n-1] = '.'  # Sortie
    return maze

def save_maze(maze, filename):
    with open(filename, 'w') as f:
        for row in maze:
            f.write(''.join(row) + '\n')

def create_maze():
    n = int(entry.get())
    filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if filename:
        maze = generate_maze(n)
        save_maze(maze, filename)
        tk.messagebox.showinfo("Succès", f"Labyrinthe sauvegardé dans le fichier {filename}")

def open_maze():
    filename = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if filename:
        with open(filename, 'r') as f:
            maze = f.read()
        tk.messagebox.showinfo("Labyrinthe", maze)

app = tk.Tk()
app.title("Générateur de Labyrinthe")

tk.Label(app, text="Taille du labyrinthe (n):").pack()
entry = tk.Entry(app)
entry.pack()

tk.Button(app, text="Créer Labyrinthe", command=create_maze).pack()
tk.Button(app, text="Ouvrir Labyrinthe", command=open_maze).pack()

app.mainloop()
