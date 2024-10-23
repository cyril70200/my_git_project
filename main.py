import json

def display_data():
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
            for entry in data:
                print(f"First Name: {entry['first_name']}")
                print(f"Last Name: {entry['last_name']}")
                print(f"Age: {entry['age']}")
                print(f"City: {entry['city']}")
                print('---')
    except FileNotFoundError:
        print("No data found. Please add some data first.")

def add_data(data):
    with open('data.json', 'r') as file:
        old_data = json.load(file)
    old_data.append(data)
    with open('data.json', 'w') as file:
        json.dump(old_data, file, indent=4)

def enter_data():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    age = input("Enter age: ")
    city = input("Enter city: ")
    data = {
        'first_name': first_name,
        'last_name': last_name,
        'age': age,
        'city': city
    }
    add_data(data)

if __name__ == "__main__":
    display_data()
    enter_data()