from tkinter import *
import pandas
import json
import random

BACKGROUND_COLOR = "#B1DDC6"


# ---------------------------- DATA ------------------------------- #
df = pandas.read_csv("data/french_words.csv")
random_line = random.randint(0, len(df))
print(type(df))
print(random_line)



# ---------------------------- UI SETUP ------------------------------- #


# window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card_img = PhotoImage(file="images/card_front.png")
canvas.create_image(800/2, 526/2, image=front_card_img)
canvas.create_text(400, 150, text="ירדן וניר", font=("Ariel",40, "italic"))
canvas.create_text(400, 263, text="גלילי", font=("Ariel",60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# buttons
right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0)
right_button.grid(column=1, row=1)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0)
wrong_button.grid(column=0, row=1)

# # labels
# title = Label(text="Title (temp)", bg="black")
# title.pack()


window.mainloop()