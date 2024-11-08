import json

# Function to check if answer text is in the context and the answer_start is correct
def check_answers(data):
    results = []
    total_questions = 0
    correct_answers = 0

    # Loop through each entry in the data
    for entry in data:
        context = entry["context"]

        # Loop through each Q&A pair
        for qa in entry["qas"]:
            total_questions += 1
            question = qa["question"]
            answer_info = qa["answers"][0]  # Assuming there's only one answer per question

            answer_text = answer_info["text"]
            answer_start = answer_info["answer_start"]

            # Find all occurrences of the answer text in the context
            occurrences = []
            start_index = context.find(answer_text)
            while start_index != -1:
                occurrences.append(start_index)
                start_index = context.find(answer_text, start_index + 1)

            # Check if the expected start index is in the list of occurrences
            if answer_start in occurrences:
                result = {
                    "question": question,
                    "answer_text": answer_text,
                    "status": "Correct"
                }
                correct_answers += 1
            elif occurrences:
                result = {
                    "question": question,
                    "answer_text": answer_text,
                    "status": "Answer start index mismatch",
                    "expected_start": answer_start,
                    "actual_start": occurrences[0]  # Show the first occurrence
                }
            else:
                # Answer text not found in context
                result = {
                    "question": question,
                    "answer_text": answer_text,
                    "status": "Answer text not found in context",
                    "expected_start": answer_start,
                    "actual_start": -1
                }

            results.append(result)

    return results, correct_answers, total_questions


# Main function to read the JSON file and process the checks
def main(json_file_path):
    # Load the JSON data
    with open(json_file_path, "r", encoding="utf-8") as file:
        data = json.load(file)["data"]

    # Perform the check
    results, correct_answers, total_questions = check_answers(data)

    # Print the results
    for result in results:
        print(f"Question: {result['question']}")
        print(f"Answer: {result['answer_text']}")
        print(f"Status: {result['status']}")
        if 'expected_start' in result and 'actual_start' in result:
            print(f"Expected start: {result['expected_start']}, Actual start: {result['actual_start']}")
        print()

    # Print the summary of correct results
    print(f"Correct answers: {correct_answers}/{total_questions}")
    if total_questions > 0:
        percentage = (correct_answers / total_questions) * 100
        print(f"Percentage of correct answers: {percentage:.2f}%")
    else:
        print("No questions found to check.")


# Run the script
if __name__ == "__main__":
    # Replace with the actual path to your JSON file
    json_file_path = input("Please enter the path to your JSON file: ")
    main(json_file_path)
