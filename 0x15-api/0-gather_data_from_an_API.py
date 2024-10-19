#!/usr/bin/python3
"""
This script retrieves TODO list progress for a given employee ID
from the JSONPlaceholder API.
"""

import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Retrieves and displays the TODO list progress for a given employee ID.

    Args:
    employee_id (int): The ID of the employee

    Returns:
    None
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    try:
        user_response = requests.get(user_url)
        user_response.raise_for_status()
        user_data = user_response.json()

        todos_response = requests.get(todos_url)
        todos_response.raise_for_status()
        todos_data = todos_response.json()

        total_tasks = len(todos_data)
        done_tasks = sum(1 for todo in todos_data if todo.get('completed'))
        employee_name = user_data.get('name')

        print(f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):")
        for todo in todos_data:
            if todo.get('completed'):
                print(f"\t {todo.get('title')}")

    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer")
        sys.exit(1)

    get_employee_todo_progress(employee_id)
