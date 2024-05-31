import tkinter as tk
from PIL import Image, ImageTk, ImageDraw, ImageFont
import random


footballers = [
    ("Thiago Silva", 86), ("Reece James", 84), ("N'Golo Kanté", 89), ("Mason Mount", 83),
    ("Raheem Sterling", 86), ("Ben Chilwell", 82), ("Edouard Mendy", 86), ("Kai Havertz", 84),
    ("Wesley Fofana", 79), ("Mateo Kovačić", 84), ("Cole Palmer", 70), ("Christopher Nkunku", 86),
    ("Nicolas Jackson", 76), ("Moisés Caicedo", 78), ("Gianfranco Zola", 90), ("Frank Lampard", 91),
    ("Didier Drogba", 91), ("John Terry", 90), ("Petr Čech", 91), ("Claude Makélélé", 89),
    ("Ashley Cole", 89), ("Michael Essien", 88), ("Dennis Wise", 87), ("Peter Osgood", 88),
    ("Pelé", 98), ("Diego Maradona", 97), ("Zinedine Zidane", 96), ("Johan Cruyff", 94),
    ("Ronaldinho", 94), ("Paolo Maldini", 94), ("Lev Yashin", 94), ("George Best", 93),
    ("Thierry Henry", 93), ("Ruud Gullit", 93), ("Lionel Messi", 93), ("Cristiano Ronaldo", 92),
    ("Robert Lewandowski", 91), ("Kevin De Bruyne", 91), ("Neymar Jr.", 91), ("Jan Oblak", 91),
    ("Virgil van Dijk", 90), ("Mohamed Salah", 90), ("Sadio Mane", 90), ("Kylian Mbappe", 90),
    ("Andrés Iniesta", 90), ("Xavi Hernández", 89), ("Franz Beckenbauer", 94), ("Marco van Basten", 93),
    ("Michel Platini", 92), ("Roberto Baggio", 92), ("David Beckham", 90), ("Lothar Matthäus", 93),
    ("Fabio Cannavaro", 92), ("Garrincha", 93), ("Romário", 93), ("Rivaldo", 92),
    ("Luis Figo", 91), ("Dennis Bergkamp", 91), ("Eric Cantona", 90), ("Gianluigi Buffon", 92),
    ("Iker Casillas", 91), ("Francesco Totti", 91), ("Ryan Giggs", 90), ("Paul Scholes", 89),
    ("Alessandro Del Piero", 92), ("Andrea Pirlo", 90), ("Fernando Torres", 89), ("Sergio Ramos", 89),
    ("Luka Modrić", 89), ("Samuel Eto'o", 89), ("Didier Deschamps", 88), ("Roberto Carlos", 91),
    ("Patrick Vieira", 90), ("Clarence Seedorf", 89), ("Davor Šuker", 88), ("Gary Lineker", 89),
    ("Jurgen Klinsmann", 88), ("Fernando Hierro", 89), ("Michael Ballack", 89), ("Alfredo Di Stéfano", 95),
    ("Eusebio", 94), ("Hristo Stoichkov", 90), ("Kaka", 91), ("Zlatan Ibrahimović", 91),
    ("David Villa", 90), ("Robin van Persie", 89), ("Carlos Tevez", 89), ("Sergio Agüero", 90),
    ("Manuel Neuer", 91), ("Philipp Lahm", 90), ("Dani Alves", 89), ("Javier Zanetti", 90),
    ("Bobby Charlton", 94), ("Gerd Müller", 93), ("Bobby Moore", 93), ("Lev Yashin", 94),
    ("Raymond Kopa", 92), ("Kevin Keegan", 91), ("Dino Zoff", 92), ("Ruud van Nistelrooy", 90),
    ("Arjen Robben", 90), ("Frank Rijkaard", 89), ("Pavel Nedvěd", 90), ("Marcelo", 89)
]

weights = [1 / ovr for _, ovr in footballers]
total_weight = sum(weights)
normalized_weights = [weight / total_weight for weight in weights]

def open_fifa_pack():
    player, ovr = random.choices(footballers, weights=normalized_weights)[0]
    update_result_label(f"{player} - OVR {ovr}")

def update_result_label(text):
    font_path = "arial.ttf" 
    font_size = 20
    outline_thickness = 2

    text_img = Image.new('RGBA', (500, 100), (0, 0, 0, 0))
    draw = ImageDraw.Draw(text_img)
    font = ImageFont.truetype(font_path, font_size)

    for x in range(-outline_thickness, outline_thickness+1):
        for y in range(-outline_thickness, outline_thickness+1):
            if x != 0 or y != 0:
                draw.text((250 + x, 30 + y), text, font=font, fill="black", anchor="mm")
    draw.text((250, 30), text, font=font, fill="white", anchor="mm")

    text_photo = ImageTk.PhotoImage(text_img)
    result_label.config(image=text_photo)
    result_label.image = text_photo

def show_fifa_pack_page():
    first_page_frame.pack_forget()
    fifa_pack_frame.pack()

root = tk.Tk()
root.title("FIFA Pack Opener")
root.configure(bg="black")


first_page_frame = tk.Frame(root, bg="black")
first_page_frame.pack(fill="both", expand=True)

try:
    toty_image = Image.open("Toty.png").convert("RGBA")
    toty_photo = ImageTk.PhotoImage(toty_image)
except Exception as e:
    print(f"Error loading image: {e}")
    toty_photo = None

if toty_photo:
    toty_label = tk.Label(first_page_frame, image=toty_photo, bg="black")
else:
    toty_label = tk.Label(first_page_frame, text="TOTY", font=("Helvetica", 24), bg="black", fg="white")
toty_label.pack(pady=20)

start_button = tk.Button(first_page_frame, text="Start", command=show_fifa_pack_page, font=("Helvetica", 16), bg="black", fg="white")
start_button.pack(pady=20)


fifa_pack_frame = tk.Frame(root, bg="black")

try:
    fifa_pack_image = Image.open("FifaPack.png").convert("RGBA")
    fifa_pack_photo = ImageTk.PhotoImage(fifa_pack_image)
except Exception as e:
    print(f"Error loading image: {e}")
    fifa_pack_photo = None

if fifa_pack_photo:
    open_pack_button = tk.Button(fifa_pack_frame, image=fifa_pack_photo, command=open_fifa_pack, borderwidth=0, highlightthickness=0, bg="black")
else:
    open_pack_button = tk.Button(fifa_pack_frame, text="Open FIFA Pack", command=open_fifa_pack, borderwidth=0, highlightthickness=0, bg="black", fg="white")
open_pack_button.pack(pady=20)

description_label = tk.Label(fifa_pack_frame, text="Tekan Pack Diatas Untuk Mendapat Pemain Bola Dengan Ovr Yang Bervariasi", font=("Helvetica", 12), bg="black", fg="white")
description_label.pack(pady=10)

result_label = tk.Label(fifa_pack_frame, text="", font=("Helvetica", 16), bg="black")
result_label.pack(pady=20)

root.mainloop()
