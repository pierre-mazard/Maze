import tkinter as tk
from tkinter import messagebox, filedialog
from maze_generator import Maze

class MazeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Générateur de Labyrinthe")
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Taille du labyrinthe (n):").pack()
        self.entry_size = tk.Entry(self.root)
        self.entry_size.pack()

        tk.Label(self.root, text="Nom du fichier:").pack()
        self.entry_filename = tk.Entry(self.root)
        self.entry_filename.pack()

        tk.Button(self.root, text="Créer Labyrinthe", command=self.create_maze).pack()
        tk.Button(self.root, text="Ouvrir Labyrinthe", command=self.open_maze).pack()

    def create_maze(self):
        n = int(self.entry_size.get())
        filename = self.entry_filename.get()
        if not filename.endswith(".txt"):
            filename += ".txt"
        maze = Maze(n)
        maze.save_maze(filename)
        messagebox.showinfo("Succès", f"Labyrinthe sauvegardé dans le fichier mazes/{filename}")

    def open_maze(self):
        filename = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")], initialdir='mazes')
        if filename:
            with open(filename, 'r') as f:
                maze = f.read()
            messagebox.showinfo("Labyrinthe", maze)

if __name__ == "__main__":
    root = tk.Tk()
    app = MazeApp(root)
    root.mainloop()
