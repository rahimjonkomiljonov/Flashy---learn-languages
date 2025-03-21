import random
from tkinter import *
import pandas


BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
data_dict = {}

# Creating a window

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Creating a dictionary from csv data
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/korean 100 words.csv")
    data_dict = original_data.to_dict(orient="records")
else:
    data_dict = data.to_dict(orient="records")
# Creating a front card word
flip_timer = None
def next_card():
    global current_card, flip_timer
    if flip_timer:
        window.after_cancel(flip_timer)
    if not data_dict:
        canvas.itemconfig(lan_name, text="Congratulations!", fill="black")
        canvas.itemconfig(word_name, text="No more words to learn!", fill="black")
    current_card = random.choice(data_dict)
    current_word = current_card["Korean"]
    canvas.itemconfig(word_name, text=current_word, fill="black")
    canvas.itemconfig(card_img, image=card_f_img)
    canvas.itemconfig(lan_name, text="Korean", fill="black")
    flip_timer = window.after(3000, show_translation)

def is_known():
    data_dict.remove(current_card)
    data = pandas.DataFrame(data_dict)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

# Flip the card
def show_translation():
    canvas.itemconfig(card_img, image=card_b_img)
    canvas.itemconfig(lan_name, text="English", fill="white")
    canvas.itemconfig(word_name, text=current_card["English"], fill="white")
# Creating canvas
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_f_img = PhotoImage(file="images/card_front.png")
card_b_img = PhotoImage(file="images/card_back.png")
card_img = canvas.create_image(400, 263, image=card_f_img)


lan_name = canvas.create_text(400, 150, text="Korean", font=("Arial", 40, "italic"))
word_name = canvas.create_text(400, 263, font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2, padx=50, pady=30)

# Creating right button
right = PhotoImage(file="images/right.png")
right_button = Button(image=right, highlightthickness=0, bg=BACKGROUND_COLOR, command=is_known)
right_button.grid(row=1, column=1, pady=20)

# Creating wrong button
wrong = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card)
wrong_button.grid(row=1, column=0, pady=20)

print(data_dict)
next_card()

window.mainloop()
