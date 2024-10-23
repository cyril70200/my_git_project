# Dummy Project

This is a dummy project to get familiar with GitHub and Visual Studio Code. The project uses a Python environment to read and display data from a JSON file.

## Project Structure
 ├── README.md 
 ├── data.json 
 └── main.py


## Requirements

- Python 3.x

## Setup

1. Clone the repository:
    ```sh
    git clone git push -u origin main
    cd dummy-project
    ```

2. Create a virtual environment:
    ```sh
    python -m venv venv
    ```

3. Activate the virtual environment:
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```

4. Install dependencies (if any):
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Add your data to the `data.json` file. Example:
    ```json
    {
        "name": "John Doe",
        "age": 30,
        "city": "New York"
    }
    ```

2. Run the `main.py` script to display the data:
    ```sh
    python main.py
    ```

## License

This project is licensed under the MIT License.