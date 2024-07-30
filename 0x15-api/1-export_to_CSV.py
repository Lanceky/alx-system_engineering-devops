#!/usr/bin/python3

"""
This script fetches TODO list data for a given employee ID from the
JSONPlaceholder API and exports the data to a CSV file.

Usage:
    python3 1-export_to_CSV.py <employee_id>

Parameters:
    <employee_id> - The ID of the employee for whom to fetch TODO data.
"""
import csv
import sys
import requests


def gather_and_export_todo_data(employee_id):
    """
    Fetches TODO list data for a given employee ID and exports it to a CSV file
    Args:
        employee_id (int): The ID of the employee to fetch TODO data for.
    """
    # De
    user_url = (
        f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    )
    todos_url = (
        f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    )

    # Fetch user data
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("User not found")
        return

    user_data = user_response.json()
    username = user_data.get('username')

    # Fetch todos data
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print("Todos not found")
        return

    todos_data = todos_response.json()

    # Define the CSV filename
    csv_filename = f"{employee_id}.csv"

    # Write data to CSV
    with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for todo in todos_data:
            writer.writerow([
                employee_id,
                username,
                todo.get('completed'),
                todo.get('title')
            ])

    print(f"Data exported to {csv_filename}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)
    gather_and_export_todo_data(employee_id)
