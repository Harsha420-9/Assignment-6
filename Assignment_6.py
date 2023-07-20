#<<<----------ASSIGNMENT-1 PART-1--------------------->>>>

import json
employee_data = [
    {
        "Name": "John Doe",
        "DOB": "1990-01-15",
        "Height": 175,
        "City": "New York",
        "State": "New York"
    },
    {
        "Name": "Jane Smith",
        "DOB": "1985-05-10",
        "Height": 165,
        "City": "Los Angeles",
        "State": "California"
    },
    {
        "Name": "Robert Johnson",
        "DOB": "1993-08-25",
        "Height": 180,
        "City": "Chicago",
        "State": "Illinois"
    },
    {
        "Name": "Mary Brown",
        "DOB": "1988-03-20",
        "Height": 160,
        "City": "Houston",
        "State": "Texas"
    },
    {
        "Name": "Michael Lee",
        "DOB": "1995-11-05",
        "Height": 190,
        "City": "Phoenix",
        "State": "Arizona"
    }
]
with open("employee.json", "w") as json_file:
    json.dump(employee_data, json_file, indent=2)
import json
class Employee:
    def __init__(self, name, dob, height, city, state):
        self.name = name
        self.dob = dob
        self.height = height
        self.city = city
        self.state = state
with open("employee.json", "r") as json_file:
    employee_data = json.load(json_file)
employees = []
for emp in employee_data:
    employees.append(Employee(emp["Name"], emp["DOB"], emp["Height"], emp["City"], emp["State"]))
for emp in employees:
    print(f"Name: {emp.name}, DOB: {emp.dob}, Height: {emp.height}, City: {emp.city}, State: {emp.state}")


#<<<<<<<-------------ASSIGNMENT-1 PART-2--------------------------->>>>>

import json
indian_states_capitals = {
    "Andhra Pradesh": "Hyderabad",
    "Tamil Nadu": "Chennai",
    "Karnataka": "Bengaluru",
    "Maharashtra": "Mumbai",
    "Uttar Pradesh": "Lucknow",
    "Gujarat": "Gandhinagar",
    "Rajasthan": "Jaipur"
}
with open("states_capitals.json", "w") as json_file:
    json.dump(indian_states_capitals, json_file, indent=2)
import json
with open("states_capitals.json", "r") as json_file:
    indian_states_capitals = json.load(json_file)
print("Indian States and Capitals:")
for state, capital in indian_states_capitals.items():
    print(f"{state}: {capital}")
