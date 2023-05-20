from tkinter import *
from tkinter import font
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
ENG_CARD_COLOR = "#91C2AF"

# ===== Data ===== #
try:
    data = pandas.read_csv("./day-31/Flash Card/data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("./day-31/Flash Card/data/french_words.csv")
finally:
    words_dict = data.to_dict(orient="records")
    words = {}


# for (index, row) in data.iterrows():
#     print(row.French)

# ===== Functions ===== #
def change_canvas_back():
    canvas.itemconfig(card_image, image=img_card_back)
    lang_name.config(text="English", fg="white", bg=ENG_CARD_COLOR)
    
    foreign_word.config(text=words["English"], fg="white", bg=ENG_CARD_COLOR)

def change_canvas_front():
    canvas.itemconfig(card_image, image=img_card_front)
    lang_name.config(text="French", fg="black", bg="white")
    foreign_word.config(fg="black", bg="white")

def choose_word():
    global words
    words = random.choice(words_dict)
    fr_word = words["French"]
    foreign_word.config(text=fr_word)
    print(words)
    
    return words

def right_clicked():
    words = choose_word()
    change_canvas_front()
    window.after(3000, change_canvas_back)
    words_dict.remove(words)
    print(len(words_dict))
    df = pandas.DataFrame(words_dict)
    df.to_csv("./day-31/Flash Card/data/words_to_learn.csv", index=False)

def wrong_clicked():
    choose_word()
    change_canvas_front()
    window.after(3000, change_canvas_back)

# ===== Window & Canvas ===== #
window = Tk()
window.title("Flash Cards")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50, height=800, width=1000)

img_card_back = PhotoImage(file="./day-31/Flash Card/images/card_back.png")
img_card_front = PhotoImage(file="./day-31/Flash Card/images/card_front.png")
canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = canvas.create_image(400, 263, image=img_card_front)
canvas.grid(column=0, row=0, columnspan=2, sticky="nsew")
window.after(3000, change_canvas_back)



# ===== Buttons ===== #
lang_name = Label(text="French", font=font.Font(family="Arial", size=40, slant="italic"), bg="white")
lang_name.place(x=400, y=150, anchor="center")
foreign_word = Label(text="", font=font.Font(family="Arial", size=60, weight="bold"), bg="white")
foreign_word.place(x=400, y=263, anchor="center")

# ===== Buttons ===== #
img_right_button = PhotoImage(file="./day-31/Flash Card/images/right.png")
img_wrong_button = PhotoImage(file="./day-31/Flash Card/images/wrong.png")
right_button = Button(image=img_right_button, highlightthickness=0, command=right_clicked)
right_button.grid(column=0, row=1)
wrong_button = Button(image=img_wrong_button, highlightthickness=0, command=wrong_clicked)
wrong_button.grid(column=1, row=1)

words = choose_word()

window.mainloop()
