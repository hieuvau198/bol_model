import torch
from transformers import AutoTokenizer, BertForTokenClassification
from transformers import pipeline

# Load the tokenizer and model
model_dir = "./model"  # path to your model folder
tokenizer = AutoTokenizer.from_pretrained(model_dir)
model = BertForTokenClassification.from_pretrained(model_dir)

# Create a pipeline for token classification
ner_pipeline = pipeline("token-classification", model=model, tokenizer=tokenizer, aggregation_strategy="simple")

# Input text for testing
text = """
Consignor/Shipper:
SS. LOGISTICS CO., LTD
280A25 LUONG DINH CUA STREET, AN PHU WARD,
DISTRICT THU DUC, HO CHI MINH CITY, VIETNAM.
TEL: (84)- 28-7106.9986 FAX: (84)- 28.7106.9986

Forwarders Ref.

Customs Reference/Status

Page: 1

Shippers Reference
Bill of Lading No.
HCMBKK033112022

Consigned to Order of:
SSL. LOGISTICS CO., LTD
22/22 SOI CHALERMPRAKEIT RAMA 9 42,
CHALERMPRAKEIT ROAD, KWANG
NONGPON KHET PRALET, BANGKOK
10250, THAILAND
Notify party:
SAME AS CONSIGNEE

PENANSHIN SHIPPING HCM CO.,LTD
Country: Vietnam
Port: HOCHIMINH
Tel: +84 2871079090
Fax: +84 2871069090
Email: general@penanshin.com.vn
Addr: ROOM 6.32 , 6 FLOOR , TOWER B,
RIVERGATE BUILDING NO 151-155 BEN VAN DON STR, WARD 6,
DISTRICT 4, HCM CITY, VIETNAM

Booking Reference
BKK03311
Place of Reciept
HOCHIMINH CFS
Vessel
HANSA OSTERBURG V.040S

Place of Loading
HOCHIMINH CFS

BILL OF LADING

Port of Discharge
BANGKOK CFS

Place of Delivery
BANGKOK CFS

Contents, weight, value and measurement according to senders declaration

Marks & Number

Number and Kind of Packages, Description of Goods

Gross Weight

CBM/ Volume

PART OF DRY CONTAINER STC
2 CTNS
CLOTH MASK

19.760 kgs

1.000 CBM

LCL/LCL

SHIPPING MARKS:
HOYA LENS VIETNAM
1/2-2/2
INVOICE NO.: HOLV-NST-001

FREIGHT PREPAID
CONTAINER & SEAL NO:
CSLU2082865/21567932

(Original B/L Surrendered In HOCHIMINH CITY)

According to declaration of the consignor.
The goods and instructions are accepted and dealt with suject to the Company's Standard Conditions
Taken in charge in apparent good order and condition, unless otherwise noted herein, at the place of reciept for transport and delivery
as mentioned above.
Freight Payable At
DESTINATION

Freight Amount
Cargo Insurance through the undersigned
Not covered: Yes/ No
Covered according to attached policy: Yes/ No

No. of Original B/Lading
ZERO

For delivery of goods please apply to: PENANSHIN SHIPPING (THAILAND) LTD.
731/32 RATCHADAPISEK ROAD, BANGPONGPENG YANNAWA,
BANGKOK 10120, THAILAND
TEL: (662) 6839199, FAX: (662) 6839177-78

Place and Date of Issue
HO CHI MINH 01 DEC, 2022

"""

# Run the pipeline on the input text
output = ner_pipeline(text)

# Display the results
for entity in output:
    print(f"Entity: {entity['word']}, Label: {entity['entity_group']}, Confidence: {entity['score']:.2f}")
