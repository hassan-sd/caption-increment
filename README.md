* Patreon: https://www.patreon.com/sd_hassan
# Text File Word Replacement Tool

This is a simple Python script that helps you replace a word with an incremental change in multiple text files.
It can be used if you want to assign a unique value in every caption of your dataset text files, might be helpful to avoid having a similar face averaged between all your images in training

## Prerequisites

Python version 3.x is required to run this script.

## Functionality

This tool performs the following tasks:

- Loads a folder that contains text files. Each text file contains one line prompts.
- Finds every instance of a user-designated word in these files.
- Replaces every instance of that word with an incremental change, such as "woman", "woman2", "woman3", incrementing at a file level. The first text file would have the first incremental change, the 2nd text file would have the 2nd incremental change, and so on.

Users can input the word to find and the word to replace it with. Users can also choose if it's incremented by a number or a letter, such as "WomanA", "WomanB", or "Woman1", "Woman2".

## Usage

To run the script, use the following steps:

1. Clone the repository to your local machine.
2. Open your terminal and navigate to the directory where the Python script is located.
3. Run the script using the command `python3 word_replace.py`.
4. Follow the prompts on the command line to input the necessary information.

```bash
$ python3 hassan-incrementor.py
Enter the path of the directory: /path/to/your/directory
Enter the word to find: woman
Enter the base word to replace with: lady
Enter increment type (number or letter): number
```

This will replace every instance of 'woman' in the text files in the specified directory with 'lady', 'lady1', 'lady2', and so on, incrementing the suffix for each file.

## Note

This script replaces exact word matches. If the word to find is a part of another word (e.g., 'man' in 'woman'), it won't be replaced. To replace such occurrences as well, you can modify the `re.sub` function in the script to remove the word boundary check (`\b`).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
