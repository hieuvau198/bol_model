import os
import json

def find_all_occurrences(text, substring):
    """Find all the start indices of a substring in a given text."""
    start_indices = []
    start = text.find(substring)
    while start != -1:
        start_indices.append(start)
        start = text.find(substring, start + 1)
    return start_indices

def update_answer_starts(json_file_path):
    # Load the JSON data
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    # Iterate over the data to update "answer_start"
    for item in data['data']:
        context = item['context']
        
        for qa in item['qas']:
            answer_text = qa['answers'][0]['text']  # Assuming one answer per question
            # Find all occurrences of the answer in the context
            start_indices = find_all_occurrences(context, answer_text)
            
            # Update answer_start
            qa['answers'][0]['answer_start'] = start_indices if start_indices else None

    # Save the modified JSON to a new file
    input_filename = os.path.basename(json_file_path).replace('.json', '')
    output_filename = f"{input_filename}_update_index.json"
    output_file_path = os.path.join(os.path.dirname(json_file_path), output_filename)
    
    with open(output_file_path, 'w') as outfile:
        json.dump(data, outfile, indent=2)

    print(f"Updated JSON file created: {output_file_path}")

# Example usage
json_file_path = input("Enter the path of the JSON file: ")
update_answer_starts(json_file_path)
