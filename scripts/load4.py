from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForTokenClassification, Trainer, TrainingArguments
import torch
import numpy as np

# Define your label list based on the entities in the bill of lading
label_list = [
    'O',  # Non-entity
    'SHIPPER', 'CONSIGNEE', 'NOTIFY_PARTY', 'FINAL_DESTINATION',
    'PORT_OF_LOADING', 'PORT_OF_UNLOADING', 'PLACE_OF_DELIVERY',
    'CARGO_TYPE', 'BILL_OF_LADING_NUMBER', 'DATE',
    'NUMBER_OF_PACKAGES', 'KIND_OF_PACKAGES', 'GROSS_WEIGHT',
    'DIMENSION_TONNAGE', 'CONTAINER_NUMBER', 'SEAL_NUMBER'
]
label_to_id = {label: i for i, label in enumerate(label_list)}

# Load your dataset
data_files = {
    "train": "data/train_data/train.jsonl",
    "test": "data/train_data/test.jsonl",
    "validation": "data/train_data/validation.jsonl"
}
dataset = load_dataset('json', data_files=data_files)

# Load tokenizer and model
model_name = "bert-base-cased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForTokenClassification.from_pretrained(model_name, num_labels=len(label_list))

# Function to align labels with tokenized words
def align_labels_with_tokens(labels, word_ids):
    aligned_labels = []
    for word_id in word_ids:
        # Only add labels if word_id is not None and within label range
        if word_id is not None and word_id < len(labels):
            aligned_labels.append(labels[word_id])
        else:
            aligned_labels.append(-100)  # -100 is used to ignore token in loss calculation
    return aligned_labels

# Preprocessing function for tokenization and label alignment
def tokenize_and_align_labels(examples):
    tokenized_examples = {"input_ids": [], "attention_mask": [], "labels": []}
    
    for i in range(len(examples["shipper"])):
        # Combine fields into single text, convert numeric fields to string
        text = (
            str(examples['shipper'][i]) + " " +
            str(examples['consignee'][i]) + " " +
            str(examples['notifyParty'][i]) + " " +
            str(examples['finalDestination'][i]) + " " +
            str(examples['codeOfPortOfLoading'][i]) + " " +
            str(examples['portOfUnloading'][i]) + " " +
            str(examples['placeOfDelivery'][i]) + " " +
            str(examples['cargoType'][i]) + " " +
            str(examples['billOfLadingNumber'][i]) + " " +
            str(examples['dateOfHouseBillOfLading'][i]) + " " +
            str(examples['departureDate'][i]) + " " +
            str(examples['numberOfPackages'][i]) + " " +  # Make sure these are strings
            str(examples['kindOfPackages'][i]) + " " +
            str(examples['totalGrossWeight'][i]) + " " +
            str(examples['descriptionOfGoods'][i]) + " " +
            str(examples['grossWeight'][i]) + " " +
            str(examples['dimensionTonnage'][i]) + " " +
            str(examples['contNumber'][i]) + " " +
            str(examples['sealNumber'][i])
        )

        # Tokenize the text
        tokenized_input = tokenizer(text, truncation=True, padding="max_length", max_length=512)
        
        # Initialize labels with 'O' (non-entity)
        labels = [label_to_id['O']] * len(tokenized_input['input_ids'])

        # Add entity labels based on each token's position in the text
        for j, word in enumerate(text.split()):
            if word in str(examples['shipper'][i]):
                labels[j] = label_to_id['SHIPPER']
            elif word in str(examples['consignee'][i]):
                labels[j] = label_to_id['CONSIGNEE']
            elif word in str(examples['notifyParty'][i]):
                labels[j] = label_to_id['NOTIFY_PARTY']
            elif word in str(examples['finalDestination'][i]):
                labels[j] = label_to_id['FINAL_DESTINATION']
            elif word in str(examples['codeOfPortOfLoading'][i]):
                labels[j] = label_to_id['PORT_OF_LOADING']
            elif word in str(examples['portOfUnloading'][i]):
                labels[j] = label_to_id['PORT_OF_UNLOADING']
            elif word in str(examples['placeOfDelivery'][i]):
                labels[j] = label_to_id['PLACE_OF_DELIVERY']
            elif word in str(examples['cargoType'][i]):
                labels[j] = label_to_id['CARGO_TYPE']
            elif word in str(examples['billOfLadingNumber'][i]):
                labels[j] = label_to_id['BILL_OF_LADING_NUMBER']
            elif word in str(examples['dateOfHouseBillOfLading'][i]):
                labels[j] = label_to_id['DATE']
            elif word in str(examples['departureDate'][i]):
                labels[j] = label_to_id['DATE']
            elif word in str(examples['numberOfPackages'][i]):
                labels[j] = label_to_id['NUMBER_OF_PACKAGES']
            elif word in str(examples['kindOfPackages'][i]):
                labels[j] = label_to_id['KIND_OF_PACKAGES']
            elif word in str(examples['totalGrossWeight'][i]):
                labels[j] = label_to_id['GROSS_WEIGHT']
            elif word in str(examples['descriptionOfGoods'][i]):
                labels[j] = label_to_id['DIMENSION_TONNAGE']
            elif word in str(examples['grossWeight'][i]):
                labels[j] = label_to_id['GROSS_WEIGHT']
            elif word in str(examples['dimensionTonnage'][i]):
                labels[j] = label_to_id['DIMENSION_TONNAGE']
            elif word in str(examples['contNumber'][i]):
                labels[j] = label_to_id['CONTAINER_NUMBER']
            elif word in str(examples['sealNumber'][i]):
                labels[j] = label_to_id['SEAL_NUMBER']

        # Align labels with tokens
        word_ids = tokenized_input.word_ids()
        aligned_labels = align_labels_with_tokens(labels, word_ids)

        # Add tokenized inputs and aligned labels
        tokenized_examples["input_ids"].append(tokenized_input["input_ids"])
        tokenized_examples["attention_mask"].append(tokenized_input["attention_mask"])
        tokenized_examples["labels"].append(aligned_labels)

    return tokenized_examples

# Apply the tokenization function to the dataset
tokenized_datasets = dataset.map(tokenize_and_align_labels, batched=True)

# Prepare the Trainer
training_args = TrainingArguments(
    output_dir='./results',
    evaluation_strategy="epoch",
    learning_rate=2e-5,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    num_train_epochs=10,
    weight_decay=0.01,
    logging_dir='./logs',  # Added logging directory for tensorboard
    logging_steps=500,     # Logs after every 500 steps
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets['train'],
    eval_dataset=tokenized_datasets['validation'],
    tokenizer=tokenizer
)

# Train the model
trainer.train()

# Save the trained model and tokenizer
model.save_pretrained('./model')
tokenizer.save_pretrained('./model')
