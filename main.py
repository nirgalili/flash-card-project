from tkinter import *
import pandas as pd
import random

card_words_list = None

TIMER = 3000

BACKGROUND_COLOR = "#B1DDC6"


def english_side():
    canvas.itemconfig(card_canvas, image=back_card_img)
    canvas.itemconfig(canvas_language, text="English", fill="white")
    canvas.itemconfig(canvas_word, text=card_words_list["English"], fill="white")


def new_card():
    global card_words_list, flip_timer
    window.after_cancel(flip_timer)
    card_words_list = random.choice(to_learn)
    french_word = card_words_list["French"]
    english_word = card_words_list["English"]
    print(f"French word - {french_word}, English word - {english_word}")
    canvas.itemconfig(canvas_language, text="French", fill="black")
    canvas.itemconfig(canvas_word, text=french_word, fill="black")
    flip_timer = window.after(TIMER, english_side)
    df_to_learn = pd.DataFrame(to_learn)
    df_to_learn.to_csv("data/words_to_learn.csv", index=False)


def remove_words_from_to_learn():
    to_learn.remove(card_words_list)
    new_card()

# data


try:
    new_df = pd.read_csv("data/words_to_learn.csv")
    to_learn = new_df.to_dict(orient="records")
    # print(to_learn)

except FileNotFoundError:
    df = pd.read_csv("data/french_words.csv")
    to_learn = df.to_dict(orient="records")
    # print(to_learn)

# UI

# window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card_img = PhotoImage(file="images/card_front.png")
back_card_img = PhotoImage(file="images/card_back.png")
card_canvas = canvas.create_image(800/2, 526/2, image=front_card_img)
canvas_language = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
canvas_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# buttons
right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=remove_words_from_to_learn)
right_button.grid(column=1, row=1)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=new_card)
wrong_button.grid(column=0, row=1)

flip_timer = window.after(500, new_card)

window.mainloop()