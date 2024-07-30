#!/usr/bin/python3

"""
Exports TODO list data for a specific employee to a CSV file.

This script takes an employee ID as a command-line argument and writes the 
employee's TODO list data to a CSV file named <employee_id>.csv. The CSV file 
includes columns for task ID, title, and completion status.
"""

import csv
import requests
import sys

def export_to_csv(employee_id):
    """Exports TODO data for a given employee ID to a CSV file."""
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(url)
    user = user_response.json()

    if not user:
        print("User not found")
        return

    user_name = user.get('username')
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    filename = f"{employee_id}.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([employee_id, user_name, task['completed'], task['title']])

    print(f"Data exported to {filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./1-export_to_CSV.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            export_to_csv(employee_id)
        except ValueError:
            print("Invalid employee ID. It should be an integer.")

