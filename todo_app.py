#!/usr/bin/env python3
"""
Simple To-Do List Application
A command-line interface for managing your daily tasks.
"""

import json
import os
import datetime
from typing import List, Dict, Any

class TodoApp:
    def __init__(self, data_file: str = "todos.json"):
        """Initialize the Todo application with a data file."""
        self.data_file = data_file
        self.todos = self.load_todos()
    
    def load_todos(self) -> List[Dict[str, Any]]:
        """Load todos from the JSON file."""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as file:
                    return json.load(file)
            return []
        except (json.JSONDecodeError, FileNotFoundError):
            print(f"Warning: Could not load {self.data_file}. Starting with empty list.")
            return []
    
    def save_todos(self) -> None:
        """Save todos to the JSON file."""
        try:
            with open(self.data_file, 'w') as file:
                json.dump(self.todos, file, indent=2)
        except Exception as e:
            print(f"Error saving todos: {e}")
    
    def add_todo(self, description: str, priority: str = "medium") -> None:
        """Add a new todo item."""
        todo = {
            "id": len(self.todos) + 1,
            "description": description.strip(),
            "completed": False,
            "created_at": datetime.datetime.now().isoformat(),
            "priority": priority.lower(),
            "completed_at": None
        }
        self.todos.append(todo)
        self.save_todos()
        print(f"✅ Added: '{description}' with {priority} priority")
    
    def list_todos(self, show_completed: bool = False) -> None:
        """Display all todos."""
        if not self.todos:
            print("📝 No todos found. Add some tasks to get started!")
            return
        
        print("\n" + "="*60)
        print("📋 YOUR TO-DO LIST")
        print("="*60)
        
        # Filter todos based on show_completed parameter
        filtered_todos = self.todos if show_completed else [t for t in self.todos if not t['completed']]
        
        if not filtered_todos:
            if not show_completed:
                print("🎉 All tasks completed! Great job!")
            return
        
        # Group by priority
        priorities = {"high": [], "medium": [], "low": []}
        for todo in filtered_todos:
            priority = todo.get("priority", "medium")
            if priority in priorities:
                priorities[priority].append(todo)
        
        # Display by priority
        priority_symbols = {"high": "🔴", "medium": "🟡", "low": "🟢"}
        
        for priority, symbol in priority_symbols.items():
            if priorities[priority]:
                print(f"\n{symbol} {priority.upper()} PRIORITY:")
                for todo in priorities[priority]:
                    status = "✅" if todo['completed'] else "⭕"
                    created = datetime.datetime.fromisoformat(todo['created_at']).strftime("%Y-%m-%d")
                    print(f"  {status} [{todo['id']}] {todo['description']} (Added: {created})")
    
    def mark_completed(self, todo_id: int) -> None:
        """Mark a todo as completed."""
        for todo in self.todos:
            if todo['id'] == todo_id:
                if todo['completed']:
                    print(f"ℹ️  Task '{todo['description']}' is already completed!")
                else:
                    todo['completed'] = True
                    todo['completed_at'] = datetime.datetime.now().isoformat()
                    self.save_todos()
                    print(f"🎉 Completed: '{todo['description']}'")
                return
        print(f"❌ No todo found with ID {todo_id}")
    
    def mark_incomplete(self, todo_id: int) -> None:
        """Mark a todo as incomplete."""
        for todo in self.todos:
            if todo['id'] == todo_id:
                if not todo['completed']:
                    print(f"ℹ️  Task '{todo['description']}' is already incomplete!")
                else:
                    todo['completed'] = False
                    todo['completed_at'] = None
                    self.save_todos()
                    print(f"🔄 Marked incomplete: '{todo['description']}'")
                return
        print(f"❌ No todo found with ID {todo_id}")
    
    def delete_todo(self, todo_id: int) -> None:
        """Delete a todo item."""
        for i, todo in enumerate(self.todos):
            if todo['id'] == todo_id:
                description = todo['description']
                del self.todos[i]
                self.save_todos()
                print(f"🗑️  Deleted: '{description}'")
                return
        print(f"❌ No todo found with ID {todo_id}")
    
    def edit_todo(self, todo_id: int, new_description: str) -> None:
        """Edit a todo's description."""
        for todo in self.todos:
            if todo['id'] == todo_id:
                old_description = todo['description']
                todo['description'] = new_description.strip()
                self.save_todos()
                print(f"✏️  Updated: '{old_description}' → '{new_description}'")
                return
        print(f"❌ No todo found with ID {todo_id}")
    
    def clear_completed(self) -> None:
        """Remove all completed todos."""
        completed_count = len([t for t in self.todos if t['completed']])
        if completed_count == 0:
            print("ℹ️  No completed tasks to clear.")
            return
        
        confirm = input(f"Are you sure you want to delete {completed_count} completed task(s)? (y/N): ")
        if confirm.lower() == 'y':
            self.todos = [t for t in self.todos if not t['completed']]
            self.save_todos()
            print(f"🧹 Cleared {completed_count} completed task(s)")
        else:
            print("Operation cancelled.")
    
    def show_stats(self) -> None:
        """Show statistics about todos."""
        total = len(self.todos)
        completed = len([t for t in self.todos if t['completed']])
        pending = total - completed
        
        print("\n" + "="*40)
        print("📊 STATISTICS")
        print("="*40)
        print(f"📝 Total tasks: {total}")
        print(f"✅ Completed: {completed}")
        print(f"⭕ Pending: {pending}")
        if total > 0:
            completion_rate = (completed / total) * 100
            print(f"🎯 Completion rate: {completion_rate:.1f}%")
        
        # Priority breakdown
        if self.todos:
            priorities = {"high": 0, "medium": 0, "low": 0}
            for todo in self.todos:
                if not todo['completed']:
                    priority = todo.get("priority", "medium")
                    if priority in priorities:
                        priorities[priority] += 1
            
            print(f"\nPending by priority:")
            print(f"🔴 High: {priorities['high']}")
            print(f"🟡 Medium: {priorities['medium']}")
            print(f"🟢 Low: {priorities['low']}")

def display_menu():
    """Display the main menu."""
    print("\n" + "="*50)
    print("🎯 TODO LIST APPLICATION")
    print("="*50)
    print("1. ➕ Add new task")
    print("2. 📋 View tasks")
    print("3. 📋 View all tasks (including completed)")
    print("4. ✅ Mark task as completed")
    print("5. 🔄 Mark task as incomplete")
    print("6. ✏️  Edit task")
    print("7. 🗑️  Delete task")
    print("8. 🧹 Clear completed tasks")
    print("9. 📊 Show statistics")
    print("0. 🚪 Exit")
    print("="*50)

def get_priority():
    """Get priority input from user."""
    while True:
        priority = input("Priority (high/medium/low) [medium]: ").strip().lower()
        if not priority:
            return "medium"
        if priority in ["high", "medium", "low"]:
            return priority
        print("Invalid priority. Please enter 'high', 'medium', or 'low'.")

def main():
    """Main application loop."""
    app = TodoApp()
    
    print("🎉 Welcome to your Personal Todo List!")
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (0-9): ").strip()
        
        try:
            if choice == '1':
                description = input("Enter task description: ").strip()
                if description:
                    priority = get_priority()
                    app.add_todo(description, priority)
                else:
                    print("❌ Task description cannot be empty!")
            
            elif choice == '2':
                app.list_todos(show_completed=False)
            
            elif choice == '3':
                app.list_todos(show_completed=True)
            
            elif choice == '4':
                app.list_todos(show_completed=False)
                if app.todos and any(not t['completed'] for t in app.todos):
                    todo_id = int(input("Enter task ID to mark as completed: "))
                    app.mark_completed(todo_id)
            
            elif choice == '5':
                completed_todos = [t for t in app.todos if t['completed']]
                if completed_todos:
                    app.list_todos(show_completed=True)
                    todo_id = int(input("Enter task ID to mark as incomplete: "))
                    app.mark_incomplete(todo_id)
                else:
                    print("ℹ️  No completed tasks to mark as incomplete.")
            
            elif choice == '6':
                app.list_todos(show_completed=False)
                if app.todos:
                    todo_id = int(input("Enter task ID to edit: "))
                    new_description = input("Enter new description: ").strip()
                    if new_description:
                        app.edit_todo(todo_id, new_description)
                    else:
                        print("❌ Description cannot be empty!")
            
            elif choice == '7':
                app.list_todos(show_completed=True)
                if app.todos:
                    todo_id = int(input("Enter task ID to delete: "))
                    app.delete_todo(todo_id)
            
            elif choice == '8':
                app.clear_completed()
            
            elif choice == '9':
                app.show_stats()
            
            elif choice == '0':
                print("👋 Thank you for using Todo List! Have a productive day!")
                break
            
            else:
                print("❌ Invalid choice. Please enter a number between 0-9.")
        
        except ValueError:
            print("❌ Invalid input. Please enter a valid number.")
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    main()