# **Python project on Random Quote Generation via .json**

## **A fully functional EXAMPLE project written in python on how to read quotes randomly from an .json file**

### **Overview**
This project demonstrates a simple Python script to fetch random quotes from a JSON file and display them. It consists of two main files: main.py and read_json.py, which work together to retrieve and display a random quote.

### **Files**
1. main.py
This file serves as the entry point of the application. It imports the read_json module to fetch a random quote and displays it along with its author, year, and source.

2. read_json.py
This file contains the function getQuote() which retrieves a random quote from the quotes.json file. It reads the JSON file, loads the quotes, and returns a randomly selected quote each time it's called.

### **Usage**
To use this project, follow these steps:

1. Ensure you have Python installed on your system.
2. Place the `quotes.json` file in the same directory as the Python scripts.
3. Run the `main.py` script using Python: `python main.py`.
4. The script will output a random quote along with its author, year, and source.
5. Feel free to customize the `quotes.json` file with your own collection of quotes to personalize the project.

### **Acknowledgements**
This project was created as a simple example for educational purposes. It can be expanded and modified to suit various applications and scenarios.