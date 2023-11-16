import tkinter as tk
from tkinter import messagebox

def show_message():
    messagebox.showinfo("Info", "Contoh GUI menggunakan Tkinter!")

# Membuat jendela utama
app = tk.Tk()
app.title("Contoh GUI")

# Membuat tombol di dalam jendela
button = tk.Button(app, text="Klik Saya", command=show_message)
button.pack(pady=100)

# Menjalankan loop utama
app.mainloop()
