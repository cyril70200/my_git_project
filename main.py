import json

def display_data():
    with open('data.json', 'r') as file:
        data = json.load(file)
        print(f"Name: {data['name']}")
        print(f"Age: {data['age']}")
        print(f"City: {data['city']}")

if __name__ == "__main__":
    display_data()