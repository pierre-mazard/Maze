import os
import random
import tkinter as tk
from tkinter import messagebox, filedialog

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
    # Créer le dossier 'mazes' s'il n'existe pas
    if not os.path.exists('mazes'):
        os.makedirs('mazes')
    
    filepath = os.path.join('mazes', filename)
    with open(filepath, 'w') as f:
        for row in maze:
            f.write(''.join(row) + '\n')

def create_maze():
    n = int(entry.get())
    filename = f"maze_{n}x{n}.txt"  # Nom de fichier automatique basé sur la taille du labyrinthe
    maze = generate_maze(n)
    save_maze(maze, filename)
    messagebox.showinfo("Succès", f"Labyrinthe sauvegardé dans le fichier mazes/{filename}")

def open_maze():
    filename = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")], initialdir='mazes')
    if filename:
        with open(filename, 'r') as f:
            maze = f.read()
        messagebox.showinfo("Labyrinthe", maze)

app = tk.Tk()
app.title("Générateur de Labyrinthe")

tk.Label(app, text="Taille du labyrinthe (n):").pack()
entry = tk.Entry(app)
entry.pack()

tk.Button(app, text="Créer Labyrinthe", command=create_maze).pack()
tk.Button(app, text="Ouvrir Labyrinthe", command=open_maze).pack()

app.mainloop()

