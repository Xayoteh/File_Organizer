# File Organizer

Simple python scrypt to organize files inside a directory by their extensions

## How to use

You can either:

- Run the script in the directory you want to organize

or 

- Pass the path (absolute or relative) to the directory as an argument. 

    If the path is invalid (not a directory or doesn't exist) the program will show the following message and exit: `Invalid path: "Path"`

The program will show the path and ask for a confirmation

`Working on directory "Path", continue? [y/n]:`

After that it will show every file moved as follows:

`Moved "file_name" to "destination_path"`

If a file with the same name already exist in "destination_path" you will se the next message:

`A file with the name "file_name" already exists in "destination_path"`

### Notes: 
- "destination_path" is relative to the current path.
- Files with its name already existing in "destination_path" will remain in their original path.
- Files without a valid extension will be ignored. No message about them will be shown and they'll stay in their original path.
