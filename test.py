import os

# Print current working directory
print("Current Working Directory:", os.getcwd())

# Try opening the file
try:
    with open("C:\\Users\\ethan\\OneDrive\\Desktop\\Programming\\miniprojectsem4\\server\\emt.txt", "r") as file:
        # Your file processing code here
        pass
except FileNotFoundError:
    print("Error: 'emotions.txt' file not found.")