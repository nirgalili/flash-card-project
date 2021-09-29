from tkinter import *
import json
import random

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- UI SETUP ------------------------------- #


# window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 526/2, image=front_card_img) # 100,100 is the center of canvas were we want the center of the pic to be
canvas.grid(column=0, row=0, columnspan=2)

# buttons
right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0)
right_button.grid(column=1, row=1)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0)
wrong_button.grid(column=0, row=1)


window.mainloop()