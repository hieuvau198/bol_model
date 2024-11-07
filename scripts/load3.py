from transformers import AutoTokenizer, AutoModelForTokenClassification

# Define your label list based on the entities in the bill of lading
label_list = [
    'O',  # Non-entity
    'SHIPPER',  # Shipper (company or entity)
    'CONSIGNEE',  # Consignee (company or entity)
    'NOTIFY_PARTY',  # Notify Party (entity)
    'FINAL_DESTINATION',  # Final Destination
    'PORT_OF_LOADING',  # Port of Loading
    'PORT_OF_UNLOADING',  # Port of Unloading
    'PLACE_OF_DELIVERY',  # Place of Delivery
    'CARGO_TYPE',  # Cargo Type
    'BILL_OF_LADING_NUMBER',  # Bill of Lading Number
    'DATE',  # Dates (date of house bill, departure date)
    'NUMBER_OF_PACKAGES',  # Number of Packages
    'KIND_OF_PACKAGES',  # Type of Packages
    'GROSS_WEIGHT',  # Gross Weight
    'DIMENSION_TONNAGE',  # Dimension or Tonnage
    'CONTAINER_NUMBER',  # Container Number
    'SEAL_NUMBER'  # Seal Number
]

# Load tokenizer and model
model_name = "bert-base-cased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForTokenClassification.from_pretrained(model_name, num_labels=len(label_list))

# Set the label-to-ID and ID-to-label mappings
model.config.id2label = {i: label for i, label in enumerate(label_list)}
model.config.label2id = {label: i for i, label in enumerate(label_list)}

print(f"Model loaded successfully with {len(label_list)} labels.")
