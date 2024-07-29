#!/usr/bin/python3

import sys
import requests

def gather_todo_data(employee_id):
    # Define the API URLs
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

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
    done_tasks = [todo['title'] for todo in todos_data if todo.get('completed')]

    # Print the result
    print(f"Employee {employee_name} is done with tasks({len(done_tasks)}/{total_tasks}):")
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

