import json

def display_data():
    with open('data.json', 'r') as file:
        data = json.load(file)
        for entry in data:
            print(f"Name: {entry['name']}")
            print(f"Age: {entry['age']}")
            print(f"City: {entry['city']}")
            print('---')

def add_data(data):
    with open('data.json', 'r') as file:
        old_data = json.load(file)
    old_data.append(data)
    with open('data.json', 'w') as file:
        json.dump(old_data, file, indent=4)

def enter_data():
    name = input("Enter name: ")
    age = input("Enter age: ")
    city = input("Enter city: ")
    data = {
        'name': name,
        'age': age,
        'city': city
    }
    add_data(data)

if __name__ == "__main__":
    display_data()
    enter_data()