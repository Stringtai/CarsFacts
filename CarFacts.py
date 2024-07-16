import csv

print("Please check 'CarsInFile' file before useage")
print("Type 'exit' to quit")
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
        return "I haven't done that car please try somethimg else."


if __name__ == "__main__":
    car_facts = load_car_facts('car_facts.csv')

    while True:
        model = input("Car name? ")
        if model.lower() == 'exit':
            break
        print(get_car_fact(car_facts, model))
