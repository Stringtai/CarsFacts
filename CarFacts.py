import csv
import customtkinter as ctk
from tkinter import messagebox
from CTkScrollableDropdown import *


def load_car_facts(filename):
    car_facts = {}
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            model = row['model'].strip().lower()
            car_facts[model] = row
    return car_facts


def get_car_fact(car_facts, model):
    model = model.strip().lower()
    if model in car_facts:
        fact = car_facts[model]['fact']
        make = car_facts[model]['make']
        year = car_facts[model]['year']
        engine = car_facts[model]['engine']
        price = car_facts[model]['price']
        seating = car_facts[model]['seating']
        return f"{make} {model.title()} ({year}): {fact}, {engine}, {price}, {seating}"
    else:
        return "I haven't done that car / Car doesn't exist, please try something else."


def on_search():
    model = searchbar.get()
    result = get_car_fact(car_facts, model)
    result_label.configure(text=result)


def on_exit():
    if messagebox.askyesno("Exit", "Do you want to exit?"):
        root.destroy()


def on_credit():
    messagebox.showinfo("Credits", "Coded and edited by String#0910")


if __name__ == "__main__":
    car_facts = load_car_facts('car_facts.csv')

    root = ctk.CTk()
    root.title("CarFacts")
    root.geometry("800x350")
    # Blank space
    instruction_label = ctk.CTkLabel(root, text="        ", font=("Helvetica", 12))
    instruction_label.pack(pady=5)

    with open("CarsInFile.txt") as f:
        cars = f.read().splitlines()


    searchbar = ctk.CTkComboBox(root, values=cars, justify="center", dropdown_hover_color="#0591FF", width=500)
    searchbar.pack(pady=10)

    if cars and cars[0].startswith("Press here for Car list dropdown else write car names here ---"):
        cars.pop(0)

    CTkScrollableDropdown(searchbar, values=cars, justify="center", button_color="transparent")

    search_button = ctk.CTkButton(root, text="Search", hover_color="#0591FF", command=on_search)
    search_button.pack(pady=10)

    exit_button = ctk.CTkButton(root, text="Exit", hover_color="#0591FF", command=on_exit)
    exit_button.pack(pady=10)

    credit_button = ctk.CTkButton(root, text="Credits", hover_color="#0591FF", command=on_credit)
    credit_button.pack(pady=10)

    result_label = ctk.CTkLabel(root, text="", wraplength=400, font=("Helvetica", 12))
    result_label.pack(pady=10)

    root.mainloop()
