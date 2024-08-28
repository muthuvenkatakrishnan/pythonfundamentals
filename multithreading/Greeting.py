import threading
def lets_celebrate(name):
    for names in name:
        print(f"Hello, {names}! Let have vodka.")

good_people = threading.Thread(target=lets_celebrate, args=(["Muthu", "Suhas", "Charu Roopa","Chetana","Spoorthi"],))
good_people.start()