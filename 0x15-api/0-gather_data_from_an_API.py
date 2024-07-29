#!/usr/bin/python3

"""
This script fetches TODO list data for a given employee ID from the
JSONPlaceholder API and displays the progress of completed tasks.

Usage:
    python3 0-gather_data_from_an_API.py <employee_id>

Parameters:
    <employee_id> - The ID of the employee for whom to fetch TODO data.
"""

import sys
import requests


def gather_todo_data(employee_id):
    """
    Fetches TODO list data for a given employee ID and prints their TODO
    list progress.

    Args:
        employee_id (int): The ID of the employee to fetch TODO data for.
    """
    # Define the API URLs
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
    employee_name = user_data.get('name')

    # Fetch todos data
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print("Todos not found")
        return

    todos_data = todos_response.json()

    # Calculate completed and total tasks
    total_tasks = len(todos_data)
    done_tasks = [
        todo['title'] for todo in todos_data if todo.get('completed')
    ]

    # Print the result
    print(
        f"Employee {employee_name} is done with tasks({len(done_tasks)}/"
        f"{total_tasks}):"
    )
    for task in done_tasks:
        print(f"\t {task}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    gather_todo_data(employee_id)
