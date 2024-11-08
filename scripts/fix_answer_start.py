import json
import os

def fix_answer_start(json_path):
    # Load the JSON content
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Traverse through each 'answer_start' and fix it if it's a list
    for item in data["data"]:
        for qas in item["qas"]:
            for answer in qas["answers"]:
                if isinstance(answer["answer_start"], list) and len(answer["answer_start"]) == 1:
                    answer["answer_start"] = answer["answer_start"][0]

    # Create the output file path
    base, ext = os.path.splitext(json_path)
    output_path = f"{base}_fixed_index{ext}"

    # Write the fixed content to the new file
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Fixed JSON saved to: {output_path}")

# Example usage:
json_path = input("Enter the path of the JSON file: ")
fix_answer_start(json_path)
