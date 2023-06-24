import os
import re

def load_and_replace(base_path, old_word, new_word_base, increment_by='number'):
    # Check if base_path is a directory
    if not os.path.isdir(base_path):
        raise Exception('Provided path is not a directory.')

    # Get list of text files in the directory
    txt_files = [f for f in os.listdir(base_path) if f.endswith('.txt')]

    # Initialize the incremental variable
    increment = 1 if increment_by == 'number' else 'A'

    # Loop over each text file
    for file_name in txt_files:
        file_path = os.path.join(base_path, file_name)

        # Load the file and read its contents
        with open(file_path, 'r') as file:
            file_contents = file.read()

        # Replace old_word with new_word
        new_word = new_word_base + str(increment)
        file_contents = re.sub(r'\b' + old_word + r'\b', new_word, file_contents)

        # Write the modified contents back to the file
        with open(file_path, 'w') as file:
            file.write(file_contents)

        # Increment the variable
        if increment_by == 'number':
            increment += 1
        else:
            increment += 'A'


if __name__ == "__main__":
    base_path = input("Enter the path of the directory: ")
    old_word = input("Enter the word to find: ")
    new_word_base = input("Enter the base word to replace with: ")
    increment_by = input("Enter increment type (number or letter): ")

    load_and_replace(base_path, old_word, new_word_base, increment_by)
