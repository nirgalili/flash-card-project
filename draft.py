from tkinter import *
import pandas
import random

french_word = None
english_word = None

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- CARDS ------------------------------- #
def flip_to_french():
    canvas.itemconfig(card_canvas, image=front_card_img)
    new_card()
    flip_card_solution()

def flip_to_english():
    canvas.itemconfig(card_canvas, image=back_card_img)
    canvas.itemconfig(canvas_language, text="English")
    canvas.itemconfig(canvas_word, text=english_word)
    flip_to_french()

# ---------------------------- TIMER ------------------------------- #
def flip_card_solution():
    window.after(3000, flip_to_english)




def new_words()->list:
    random_line = random.randint(0, len(df)-1)
    french = df["French"][random_line]
    english = df["English"][random_line]
    new_card_words = [french, english]
    return new_card_words

def new_card():
    # pass
    new_word_list = new_words()
    global french_word
    global english_word
    french_word = new_word_list[0]
    english_word = new_word_list[1]
    print(new_word_list)
    canvas.itemconfig(canvas_language, text="French")
    canvas.itemconfig(canvas_word, text=french_word)




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
# french side
front_card_img = PhotoImage(file="images/card_front.png")
back_card_img = PhotoImage(file="images/card_back.png")
card_canvas = canvas.create_image(800/2, 526/2, image=front_card_img)
canvas_language = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
canvas_word =canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# buttons
right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=new_card)
right_button.grid(column=1, row=1)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=flip_to_english)
wrong_button.grid(column=0, row=1)

# # labels
# title = Label(text="Title (temp)", bg="black")
# title.pack()

# print(new_card())

flip_card_solution()

window.mainloop()