import csv
import customtkinter as ctk
from tkinter import messagebox
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
        return f"{make} {model.title()} ({year}) {fact} {engine} {price} {seating}:"
    else:
        return "I haven't done that car / Car doesnt exist please try somethimg else."


def on_search():
    model = entry.get()
    result = get_car_fact(car_facts, model)
    result_label.configure(text=result)


def on_exit():
    if messagebox.askyesno("Exit", "Do you want to exit?"):
        root.destroy()

def on_credit():
    messagebox.showinfo(root,"Coded and edited by Stringtai")


if __name__ == "__main__":
    car_facts = load_car_facts('car_facts.csv')

    root = ctk.CTk()
    root.title("CarFacts")
    root.geometry("800x350")

    instructionLabel = ctk.CTkLabel(root, text="Please check 'Cars in File' before usage", font=("Helvetica", 12))
    instructionLabel.pack(pady=5)

    entry = ctk.CTkEntry(root, placeholder_text="Insert Car names here", width=500)
    entry.pack(pady=10)

    search_button = ctk.CTkButton(root, text="Search", hover_color="#0591FF", command=on_search)
    search_button.pack(pady=10)

    exit_button = ctk.CTkButton(root, text="Exit",hover_color="#0591FF", command=on_exit)
    exit_button.pack(pady=10)

    credit_button = ctk.CTkButton(root, text="credits",hover_color="#0591FF", command=on_credit)
    credit_button.pack(pady=10)

    result_label = ctk.CTkLabel(root, text="", wraplength=400, font=("Helvetica", 12))
    result_label.pack(pady=10)

    root.mainloop()
