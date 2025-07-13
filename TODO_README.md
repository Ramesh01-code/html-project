# 📝 Todo List Application

A simple, feature-rich command-line todo list application built with Python. Manage your daily tasks efficiently with an intuitive interface and persistent data storage.

## ✨ Features

- **Add Tasks**: Create new tasks with priority levels (high, medium, low)
- **View Tasks**: Display all pending tasks or all tasks including completed ones
- **Mark Complete/Incomplete**: Toggle task completion status
- **Edit Tasks**: Modify task descriptions
- **Delete Tasks**: Remove individual tasks
- **Clear Completed**: Bulk delete all completed tasks
- **Statistics**: View completion rates and priority breakdown
- **Data Persistence**: Tasks are automatically saved to a JSON file
- **Priority System**: Organize tasks by priority with visual indicators
- **Timestamps**: Track when tasks were created and completed

## 🚀 Quick Start

### Prerequisites
- Python 3.6 or higher

### Running the Application

#### Option 1: Direct Python execution
```bash
python3 todo_app.py
```

#### Option 2: Using the launcher script
```bash
# Make the script executable
chmod +x run_todo.sh

# Run the application
./run_todo.sh
```

## 📖 How to Use

When you start the application, you'll see a menu with the following options:

```
🎯 TODO LIST APPLICATION
==================================================
1. ➕ Add new task
2. 📋 View tasks
3. 📋 View all tasks (including completed)
4. ✅ Mark task as completed
5. 🔄 Mark task as incomplete
6. ✏️  Edit task
7. 🗑️  Delete task
8. 🧹 Clear completed tasks
9. 📊 Show statistics
0. 🚪 Exit
==================================================
```

### Adding Tasks
1. Choose option `1`
2. Enter your task description
3. Select priority level (high/medium/low) or press Enter for default (medium)

### Viewing Tasks
- Option `2`: Shows only pending (incomplete) tasks
- Option `3`: Shows all tasks including completed ones

Tasks are displayed grouped by priority:
- 🔴 High Priority
- 🟡 Medium Priority  
- 🟢 Low Priority

### Managing Tasks
- **Complete**: Use option `4` and enter the task ID
- **Mark Incomplete**: Use option `5` and enter the task ID
- **Edit**: Use option `6` to modify task descriptions
- **Delete**: Use option `7` to remove tasks permanently

### Statistics
Option `9` shows:
- Total number of tasks
- Completed vs pending tasks
- Completion percentage
- Breakdown by priority

## 💾 Data Storage

Tasks are automatically saved to `todos.json` in the same directory as the application. This file is created automatically when you add your first task.

### Sample Data Structure
```json
[
  {
    "id": 1,
    "description": "Complete the project report",
    "completed": false,
    "created_at": "2024-01-15T10:30:00.123456",
    "priority": "high",
    "completed_at": null
  }
]
```

## 🎨 Visual Elements

The application uses emojis and colors to make the interface more engaging:
- ✅ Completed tasks
- ⭕ Pending tasks
- 🔴 High priority
- 🟡 Medium priority
- 🟢 Low priority
- 📊 Statistics
- 🧹 Cleanup operations

## 🛠️ Technical Details

- **Language**: Python 3
- **Storage**: JSON file format
- **Dependencies**: Only Python standard library
- **Platform**: Cross-platform (Windows, macOS, Linux)

## 🔧 Customization

You can easily customize the application by modifying `todo_app.py`:

- Change the data file location by modifying the `data_file` parameter
- Add new priority levels in the `priorities` dictionary
- Customize the visual elements and emojis
- Add new features like due dates, categories, etc.

## 📁 File Structure

```
.
├── todo_app.py         # Main application file
├── run_todo.sh         # Launcher script
├── TODO_README.md      # This documentation
└── todos.json          # Data file (created automatically)
```

## 🚨 Error Handling

The application includes robust error handling:
- Invalid input validation
- File I/O error management
- Graceful handling of corrupted data files
- Keyboard interrupt (Ctrl+C) support

## 💡 Tips for Best Use

1. **Use Priorities**: Organize tasks by importance to focus on what matters most
2. **Regular Cleanup**: Use the "Clear completed tasks" feature to keep your list manageable
3. **Check Statistics**: Monitor your productivity with the statistics feature
4. **Backup Data**: The `todos.json` file contains all your tasks - consider backing it up

## 🤝 Contributing

Feel free to extend this application with additional features like:
- Due dates and reminders
- Task categories or tags
- Export to different formats
- Web interface
- Mobile app synchronization

## 📄 License

This project is open source and available under the MIT License.

---

**Happy task managing! 🎯**