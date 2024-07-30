#!/usr/bin/python3

import csv
import sys
import requests

def main():
    """Export TODO list for a given employee ID to CSV."""
    if len(sys.argv) != 2:
        print("Usage: ./1-export_to_CSV.py <employee_id>")
        return

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        return

    # API endpoints
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    # Fetch user data
    user_response = requests.get(users_url)
    users = user_response.json()
    
    # Fetch TODO data
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    # Find the user by ID
    user = next((user for user in users if user["id"] == employee_id), None)
    if not user:
        print("User not found")
        return

    # Filter TODOs by employee ID
    user_todos = [todo for todo in todos if todo["userId"] == employee_id]

    # Export to CSV
    filename = f"{employee_id}.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for todo in user_todos:
            writer.writerow([employee_id, user['username'], todo['completed'], todo['title']])

if __name__ == "__main__":
    main()

