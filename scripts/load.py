import pandas as pd
from sklearn.model_selection import train_test_split

# Load the JSONL file
data = pd.read_json("data/labeled_text_jsonl/combined_dataset.jsonl", lines=True)

# Define the split ratios
train_ratio = 0.8
validation_ratio = 0.1
test_ratio = 0.1

# Initial train-test split
train_data, temp_data = train_test_split(data, test_size=(1 - train_ratio), random_state=42)

# Split the temporary dataset into validation and test sets
validation_data, test_data = train_test_split(temp_data, test_size=(test_ratio / (test_ratio + validation_ratio)), random_state=42)

# Verify the splits
print(f"Training Set Size: {len(train_data)}")
print(f"Validation Set Size: {len(validation_data)}")
print(f"Test Set Size: {len(test_data)}")

# Save splits to separate files for easy access
train_data.to_json("data/labeled_text_jsonl/train.jsonl", orient="records", lines=True)
validation_data.to_json("data/labeled_text_jsonl/validation.jsonl", orient="records", lines=True)
test_data.to_json("data/labeled_text_jsonl/test.jsonl", orient="records", lines=True)
