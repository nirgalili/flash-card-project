from tkinter import *
import pandas
import json
import random

BACKGROUND_COLOR = "#B1DDC6"

def new_words():
    random_line = random.randint(0, len(df)-1)
    french = df["French"][random_line]
    english = df["English"][random_line]
    new_card_words = [french, english]
    return new_card_words

def new_card():
    # pass
    new_word = new_words()
    print(new_word)
    canvas.itemconfig(canvas_word, text=new_word[0])




# ---------------------------- DATA ------------------------------- #
df = pandas.read_csv("data/french_words.csv")
random_line = random.randint(0, len(df))




# ---------------------------- UI SETUP ------------------------------- #


# window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card_img = PhotoImage(file="images/card_front.png")
canvas.create_image(800/2, 526/2, image=front_card_img)
canvas_language = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
canvas_word =canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# buttons
right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=new_card)
right_button.grid(column=1, row=1)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=new_card)
wrong_button.grid(column=0, row=1)

# # labels
# title = Label(text="Title (temp)", bg="black")
# title.pack()

# print(new_card())
window.mainloop()