def find_all_occurrences(text, substrings):
    results = {}

    # Loop through each substring
    for substring in substrings:
        start = 0
        indices = []

        # Loop to find each occurrence of the current substring
        while True:
            start = text.find(substring, start)
            if start == -1:
                break
            indices.append(start)
            start += len(substring)  # Move to the next character after the found substring

        results[substring] = indices
    
    return results

# Example usage
text = "Consignor/Shipper: GLOBAL TRADE EXPORTS INC. 180 QUEEN ST., SUITE 1200 TORONTO, ON, CANADA TEL: +1 416 789 1234 FAX: +1 416 789 5678  Forwarders Ref.  Customs Reference/Status  Page: 1  Shippers Reference Bill of Lading No. TORNYC05252024  Consigned to Order of: TO THE ORDER OF METRO BANK USA BBL NO. 7/DKK 857430 TO BE ISSUED BY GLOBAL TRADE LINES LTD.  Notify party: NEW YORK IMPORT SOLUTIONS LLC 600 MADISON AVENUE, 10TH FLOOR NEW YORK, NY 10022, USA TEL: +1 212 345 6789 FAX: +1 212 345 6790  AMERICAS SHIPPING AGENCY LTD. Country: Canada Port: TORONTO Tel: +1 416 333 5678 Fax: +1 416 333 5679 Email: contact@americasshipping.ca Addr: SUITE 5B, 25 FRONT ST W, TORONTO, ON, CANADA  Booking Reference NYC10023 Place of Receipt TORONTO PORT Vessel NORTH ATLANTIC STAR V.118W  Place of Loading TORONTO PORT, CANADA  Port of Discharge NEW YORK, USA  Place of Delivery NEW YORK CFS  BILL OF LADING Contents, weight, value, and measurement according to senderâ€™s declaration  Marks & Number  Number and Kind of Packages, Description of Goods  Gross Weight  CBM/ Volume  PART OF DRY CONTAINER STC 5 CTNS S.T.C TEXTILES, 60% COTTON, 40% POLYESTER W: 120 CM  320.50 kgs  3.750 CBM  LCL/LCL  SHIPPING MARKS: FREIGHT PREPAID URBAN APPAREL GROUP INC. C/NO. 5 PO NO: PONYC023JD01245 (8JPQ09/03)  CONTAINER & SEAL NO: TRLU3098571/76543210  (Original B/L Surrendered In TORONTO)  According to declaration of the consignor. The goods and instructions are accepted and dealt with subject to the Companyâ€™s Standard Conditions. Taken in charge in apparent good order and condition, unless otherwise noted herein, at the place of receipt for transport and delivery as mentioned above.  Freight Payable At DESTINATION  Freight Amount Cargo Insurance through the undersigned Not covered: Yes/ No Covered according to attached policy: Yes/ No  No. of Original B/Lading ZERO  For delivery of goods please apply to: AMERICAS SHIPPING AGENCY (USA) LLC 200 BROADWAY, SUITE 300, NEW YORK, NY 10007, USA TEL: +1 212 555 6789, FAX: +1 212 555 6790  Place and Date of Issue TORONTO 25 MAY, 2024"
substrings = [
    "TO THE ORDER OF METRO BANK USA BBL NO. 7/DKK 857430 TO BE ISSUED BY GLOBAL TRADE LINES LTD.",
    "NEW YORK IMPORT SOLUTIONS LLC 600 MADISON AVENUE, 10TH FLOOR NEW YORK, NY 10022, USA",
    "TORONTO PORT, CANADA",
    "NEW YORK, USA",
]

# Find all occurrences for each substring
results = find_all_occurrences(text, substrings)

# Print the results
for substring, indices in results.items():
    if indices:
        print(f"The substring '{substring}' was found at the following indices: {indices}")
    else:
        print(f"The substring '{substring}' was not found.")