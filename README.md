# Python Argparse Learning Projects
A collection of CLI (Command Line Interface) tools built while learning Python's argparse library. These projects demonstrate different argparse features from basic argument parsing to subcommands and mutually exclusive groups.

# Projects Overview
### 1. Text Analyzer (text_analyzer.py)
A tool to analyze text files with various statistics and search capabilities.
   
**Features:**
- Count lines, words, and characters
- Search for specific text
- Display file preview

**Usage:**
```bash
# Basic file reading (shows preview)
python text_analyzer.py sample.txt

# Count lines
python text_analyzer.py sample.txt -l

# Count words and characters
python text_analyzer.py sample.txt -w -c

# Search for text
python text_analyzer.py sample.txt -s "python"
```

### 2. File Manager (subCommand.py)
A simple file management tool with subcommands for different operations.

**Features:**
- Create files with optional content
- Delete files (with force option)
- List files in a directory

**Usage:**
```bash
# Create a new file
python file_manager.py create myfile.txt

# Create with content
python file_manager.py create myfile.txt -c "Hello World"

# Delete a file
python file_manager.py delete myfile.txt

# Force delete
python file_manager.py delete myfile.txt -f

# List files in current directory
python file_manager.py list

# List files in specific directory
python file_manager.py list -d /path/to/directory
```

### 3. Temperature Converter (temperature_converter.py)
Convert temperatures between Celsius, Fahrenheit, and Kelvin.

**Features:**
- Mutually exclusive arguments (can only use one at a time)
- Type validation (only accepts numbers)
- Converts to all other units automatically

**Usage:**
```bash
# Convert from Celsius
python temperature_converter.py -c 25

# Convert from Fahrenheit
python temperature_converter.py -f 77

# Convert from Kelvin
python temperature_converter.py -k 298.15
```

### 4. Todo CLI (todo_cli.py)
A complete todo list manager with persistent storage.

**Features:**
- Add tasks
- Mark tasks as complete
- Delete tasks
- View all tasks
- Data persistence using JSON

**Usage:**
```bash
# Add a task
python todo_cli.py add "Learn Python argparse"

# View all tasks
python todo_cli.py list

# Mark task as done (use ID from list)
python todo_cli.py done 1

# Delete a task
python todo_cli.py delete 1
```





