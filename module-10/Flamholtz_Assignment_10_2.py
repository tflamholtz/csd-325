# Tzvi Flamholtz
# Assignment 10.2
# 08/16/2026
# This program creates a simple to-do list application using the Tkinter library in Python.


# import tkinter and messagebox for GUI and user prompts
import tkinter as tk
import tkinter.messagebox as msg
# Added import for Menu to create a menu bar
from tkinter import Menu

# created a class called Todo that inherits from tk.Tk
class Todo(tk.Tk):
    # defined the constructor method for the Todo class, which initializes the GUI and sets up the task list
    def __init__(self, tasks=None):
        super().__init__()

        # If no tasks are provided, initialize an empty list; otherwise, use the provided tasks
        if not tasks:
            self.tasks = []
        else:
            self.tasks = tasks

        self.tasks_canvas = tk.Canvas(self)

        self.tasks_frame = tk.Frame(self.tasks_canvas)
        self.text_frame = tk.Frame(self)

        self.scrollbar = tk.Scrollbar(self.tasks_canvas, orient="vertical", command=self.
            tasks_canvas.yview)

        self.tasks_canvas.configure(yscrollcommand=self.scrollbar.set)

        # Modified the title
        self.title("Flamholtz-To-Do App v2")
        self.geometry("300x400")

        # Call the add menu function to create the menu bar
        self.create_menu()
        
        self.task_create = tk.Text(self.text_frame, height=3, bg="white", fg="black")

        self.tasks_canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas_frame = self.tasks_canvas.create_window((0, 0), window=self.
            tasks_frame, anchor="n")

        self.task_create.pack(side=tk.BOTTOM, fill=tk.X)
        self.text_frame.pack(side=tk.BOTTOM, fill=tk.X)
        self.task_create.focus_set()

        # Modified bg color
        # Added delete instructions
        todo1 = tk.Label(self.tasks_frame, text="- Add Items Here - Right Click item to Delete", bg="SkyBlue1",
            fg="black", pady=10)

        # Modified the delete task from left click to right click
        todo1.bind("<Button-3>", self.remove_task)

        self.tasks.append(todo1)

        for task in self.tasks:
            task.pack(side=tk.TOP, fill=tk.X)

        self.bind("<Return>", self.add_task)
        self.bind("<Configure>", self.on_frame_configure)
        self.bind_all("<MouseWheel>", self.mouse_scroll)
        self.bind_all("<Button-4>", self.mouse_scroll)
        self.bind_all("<Button-5>", self.mouse_scroll)
        self.tasks_canvas.bind("<Configure>", self.task_width)

        # Modified the color scheme to include two different colors for tasks
        self.colour_schemes = [{"bg": "SkyBlue1", "fg": "black"}, {"bg": "HotPink1", "fg": "white"}]

    # defined a method to create a menu bar with a "File" menu and an "Exit" option
    # This was added to the original code 
    def create_menu(self):
        menu_bar = Menu(self)
        self.config(menu=menu_bar)
        file_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Exit", command=self.destroy)

    # defined a method to add a new task to the task list
    def add_task(self, event=None):
        task_text = self.task_create.get(1.0,tk.END).strip()

        if len(task_text) > 0:
            new_task = tk.Label(self.tasks_frame, text=task_text, pady=10)

            self.set_task_colour(len(self.tasks), new_task)

            # Modified the delete task from left click to right click
            new_task.bind("<Button-3>", self.remove_task)
            new_task.pack(side=tk.TOP, fill=tk.X)

            self.tasks.append(new_task)

        self.task_create.delete(1.0, tk.END)

    # defined a method to remove a task from the task list when the user right-clicks on it
    def remove_task(self, event):
        task = event.widget
        if msg.askyesno("Really Delete?", "Delete " + task.cget("text") + "?"):
            self.tasks.remove(event.widget)
            event.widget.destroy()
            self.recolour_tasks()

    # defined a method to recolour the tasks in the task list based on their position in the list
    def recolour_tasks(self):
        for index, task in enumerate(self.tasks):
            self.set_task_colour(index, task)

    # defined a method to set the background and foreground colors of a task based on its position in the list
    def set_task_colour(self, position, task):
        _, task_style_choice = divmod(position, 2)

        my_scheme_choice = self.colour_schemes[task_style_choice]

        task.configure(bg=my_scheme_choice["bg"])
        task.configure(fg=my_scheme_choice["fg"])

    # defined a method to update the scroll region of the canvas when the frame is configured
    def on_frame_configure(self, event=None):
        self.tasks_canvas.configure(scrollregion=self.tasks_canvas.bbox("all"))

    # defined a method to update the width of the tasks in the canvas when the canvas is resized
    def task_width(self, event):
        canvas_width = event.width
        self.tasks_canvas.itemconfig(self.canvas_frame, width = canvas_width)

    # defined a method to handle mouse scroll events and scroll the canvas accordingly
    def mouse_scroll(self, event):
        if event.delta:
            self.tasks_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        else:
            if event.num == 5:
                move = 1
            else:
                move = -1

            self.tasks_canvas.yview_scroll(move, "units")

# defined the main block of the program, which creates an instance of the Todo class and starts the main event loop
if __name__ == "__main__":
    todo = Todo()
    todo.mainloop()


# # Title: Assignment 10.2
# Author: David Love
# Comments and modifications by: Tzvi Flamholtz
# Date: 08/16/2026