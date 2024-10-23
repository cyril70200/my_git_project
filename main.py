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
    """
    Adds new data to an existing JSON file.

    This function reads the current contents of 'data.json', appends the new data to it,
    and then writes the updated data back to 'data.json'.

    Args:
        data (dict): The new data to be added to the JSON file.

    Raises:
        FileNotFoundError: If 'data.json' does not exist.
        json.JSONDecodeError: If 'data.json' contains invalid JSON.
    """
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

def remove_entry_by_name():
    """
    Prompts the user to enter the name of an entry to remove from a JSON file.
    The function performs the following steps:
    1. Prompts the user to input the name of the entry they want to remove.
    2. Reads the data from 'data.json'.
    3. Searches for entries that match the given name (case-insensitive).
    4. If no matching entries are found, informs the user and exits.
    5. Displays the matching entries to the user.
    6. Prompts the user to select the entry they want to remove by entering a number.
    7. Removes the selected entry from the data.
    8. Writes the updated data back to 'data.json'.
    9. Informs the user of the successful removal or any errors encountered.
    Raises:
        ValueError: If the user input for selecting an entry is not a valid number.
    """
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