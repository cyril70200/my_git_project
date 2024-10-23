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

def remove_entry_by_name():
    name = input("Enter the name of the entry you want to remove: ")
    
    with open('data.json', 'r') as file:
        data = json.load(file)
    
    matching_entries = [entry for entry in data if name.lower() in entry['name'].lower()]
    
    if not matching_entries:
        print("No matching entries found.")
        return
    
    print("Matching entries:")
    for i, entry in enumerate(matching_entries, start=1):
        print(f"{i}. Name: {entry['name']}, Age: {entry['age']}, City: {entry['city']}")
    
    try:
        choice = int(input("Enter the number of the entry you want to remove: "))
        if 1 <= choice <= len(matching_entries):
            entry_to_remove = matching_entries[choice - 1]
            data.remove(entry_to_remove)
            with open('data.json', 'w') as file:
                json.dump(data, file, indent=4)
            print("Entry removed successfully.")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    display_data()
    remove_entry_by_name()