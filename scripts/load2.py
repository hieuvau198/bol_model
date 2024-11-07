from datasets import load_dataset

# Load the datasets
data_files = {
    "train": "data/train_data/train.jsonl",
    "test": "data/train_data/test.jsonl",
    "validation": "data/train_data/validation.jsonl"
}
dataset = load_dataset('json', data_files=data_files)
