# DO-NOT-EXECUTE Script
======================

## Description

This script is designed to delete every file in the current working directory.

## Usage

To use this script, simply run it in the directory where you want to delete files. **Note:** This script will delete every file in the current working directory without prompting for confirmation. Use with caution!

## Code Explanation

### Variables and Functions

#### `current_dir`

* Type: string
* Description: The current working directory of the script.

#### `files`

* Type: list
* Description: A list of all files in the current working directory.

#### `os.listdir(current_dir)`

* Function: Returns a list of all files and directories in the specified directory.
* Parameters: `current_dir` (string) - The directory to list files from.
* Returns: A list of file and directory names.

#### `os.path.join(current_dir, f)`

* Function: Joins a directory path with a file name to create a full file path.
* Parameters: `current_dir` (string) - The directory path, `f` (string) - The file name.
* Returns: A full file path (string).

#### `os.path.isfile(os.path.join(current_dir, f))`

* Function: Checks if a file exists at the specified path.
* Parameters: `os.path.join(current_dir, f)` (string) - The full file path.
* Returns: `True` if the file exists, `False` otherwise.

#### `os.remove(os.path.join(current_dir, file))`

* Function: Deletes a file at the specified path.
* Parameters: `os.path.join(current_dir, file)` (string) - The full file path.
* Returns: None

### Script Flow

1. The script gets the current working directory using `os.path.dirname(os.path.abspath(__file__))`.
2. It lists all files in the current directory using `os.listdir(current_dir)`.
3. It filters the list to only include files (not directories) using `os.path.isfile(os.path.join(current_dir, f))`.
4. It iterates over the list of files, printing a message for each file indicating that it is being deleted.
5. It attempts to delete each file using `os.remove(os.path.join(current_dir, file))`.
6. If an error occurs while deleting a file, it catches the `OSError` exception and prints an error message.
7. Finally, it prints a success message indicating that every other file in the folder has been deleted.

## Warning USE IT WITH CAUTION!!!!

This script will delete every file in the current working directory without prompting for confirmation. Use with caution!
