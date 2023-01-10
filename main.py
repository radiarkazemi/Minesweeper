from tkinter import *
import settings
import utils
from cell import Cell

root = Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width / 2) - (settings.Wight / 2)
y = (screen_height / 2) - (settings.Height / 2)

root.geometry(f"{settings.Wight}x{settings.Height}+{int(x)}+{int(y)}")
root.resizable(False, False)
root.title("Minesweeper Game")
root.configure(bg="black")

top_frame = Frame(
    root,
    bg="black",
    width=settings.Wight,
    height=utils.height_prc(25))
top_frame.place(x=0, y=0)
left_frame = Frame(
    root,
    bg="black",
    width=utils.width_prc(25),
    height=utils.height_prc(75)
)
left_frame.place(x=0, y=150)

center_frame = Frame(
    root,
    bg="black",
    width=utils.width_prc(75),
    height=utils.height_prc(75)
)
center_frame.place(
    x=utils.width_prc(25),
    y=utils.height_prc(25)
)

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x, y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column=x, row=y
        )

Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(
    x=0, y=0
)

game_title = Label(
    top_frame,
    bg="black",
    fg="white",
    text="Minesweeper Game",
    font=("", 48)
)
game_title.place(
    x=utils.width_prc(25), y=10
)

Cell.randomize_mines()
for c in Cell.all:
    print(c.is_mine)

# ------------------------------------mainloop----------------------------------------

root.mainloop()
