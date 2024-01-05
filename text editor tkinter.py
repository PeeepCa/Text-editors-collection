import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def save_file():
    file_path = filedialog.asksaveasfilename()
    if file_path:
        with open(file_path, "w") as file:
            text = text_area.get(1.0, tk.END)
            file.write(text)

def load_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, "r") as file:
            text = file.read()
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, text)

def exit_editor():
    if messagebox.askokcancel("Exit", "Are you sure you want to exit?"):
        window.destroy()

def change_font_color(event=None):
    text = text_area.get(1.0, tk.END)
    words_to_change_color = ["Python", "editor", "font"]

    for word in words_to_change_color:
        start_index = "1.0"
        while True:
            start_index = text_area.search(word, start_index, stopindex=tk.END)
            if not start_index:
                break
            end_index = f"{start_index}+{len(word)}c"
            text_area.tag_add("color", start_index, end_index)
            start_index = end_index

## Create the main window
window = tk.Tk()
window.title("Text Editor")

## Create a text area
text_area = tk.Text(window)
text_area.pack()

## Create the menu bar
menu_bar = tk.Menu(window)
window.config(menu=menu_bar)

## Create the File menu
file_menu = tk.Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Load", command=load_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_editor)

## Configure tag for font color change
text_area.tag_configure("color", foreground="red")  # Change font color to red

## Bind the change_font_color function to the KeyRelease event
text_area.bind("<KeyRelease>", change_font_color)

## Start the main loop
window.mainloop()
