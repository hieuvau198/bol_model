import os
import json

def convert_txt_to_json(txt_file_path):
    # Read the content of the input text file
    with open(txt_file_path, 'r') as file:
        text_content = file.read()

    # Replace '\n' with spaces
    modified_content = text_content.replace('\n', ' ')

    # Create a dictionary for JSON output
    json_data = {
        "context": modified_content,
    }

    # Get the directory and filename of the input file
    file_directory = os.path.dirname(txt_file_path)
    file_name = os.path.basename(txt_file_path).replace('.txt', '')

    # Define the output JSON file path
    json_file_path = os.path.join(file_directory, f"{file_name}.json")

    # Write the modified content to a JSON file
    with open(json_file_path, 'w') as json_file:
        json.dump(json_data, json_file, indent=2)

    print(f"JSON file created: {json_file_path}")

# Example usage
txt_file_path = input("Enter the path of the text file: ")
convert_txt_to_json(txt_file_path)
