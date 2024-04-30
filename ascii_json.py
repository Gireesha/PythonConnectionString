import json

# Define employees as a global variable
employees = None

# Open the JSON file
# Close the file (automatically done by 'with' statement)
with open('employee.json', 'r') as employee_json_file:
    # Load JSON data from the file into a Python list
    employees = json.load(employee_json_file)