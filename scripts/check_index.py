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
text = "Consignor/Shipper: PANALPINA WORLD TRANSPORT (VIETNAM) CO., LTD. AS AGENT FOR AND ON BEHALF OF PANTAINER LTD., 3/F HAI AU BUILDING 39B TRUONG SON ST, TAN BINH, HCMC, VIETNAM TEL: 848.9974780 FAX: 848.9974790 Forwarders Ref. Customs Reference/Status Page: 1 Shippers Reference Bill of Lading No. HCMBKK029112022 Consigned to Order of: PANALPINA WORLD TRANSPORT (VIETNAM) AS AGENT FOR AND ON BEHALF OF PANTAINER LTD., SIRINRAT BUILDING, 14TH FLOOR 3388/47-49 NAMA IV ROAD KLONGTON, KLONGTOEY BANGKOK 10110 TEL: (0)23486000 FAX: (0)23496199 Notify party: SAME AS ABOVE PENANSHIN SHIPPING HCM CO.,LTD Country: Vietnam Port: HOCHIMINH Tel: +84 2871079090 Fax: +84 2871069090 Email: general@penanshin.com.vn Addr: ROOM 6.32 , 6 FLOOR , TOWER B, RIVERGATE BUILDING NO 151-155 BEN VAN DON STR, WARD 6, DISTRICT 4, HCM CITY, VIETNAM Booking Reference BKK02911 Place of Reciept HOCHIMINH CFS Vessel HANSA OSTERBURG V.040S Place of Loading Loading Port of HOCHIMINH ,CFS VIETNAM Port of Discharge BANGKOK CFS Place of Delivery BANGKOK CFS BILL OF LADING Contents, weight, value and measurement according to senders declaration Marks & Number: Control/Seal No. Number and Kind of Packages, Description of Goods LCL/LCL PART OF DRY CONTAINER STC 1. CTNS S.T.C. MAIN MATERIAL ACCESSIORIES FOR MARKING LADIES' UNDERWEAR SHIPPING MARKS: BODY FASHION (THAILAND) - LTD 393, MOO 17, TEMBOL, BANSAOHTHONG, AMPEOR BANSAOTHONG, SAMUTPRAKARN 10540, THAILAND ATTN MRS. CHCNLAGAN KWANDAENG C/NO. 8592 Gross Weight CBM/ Volume 9.00 KGS 1.000 M3 FREIGHT PREPAID CONTAINER & SEAL NO: CSLU2082865/21567932 Total: ONE (1) CARTON ONLY (Original B/L Sunrendered In HOCHIMINH CITY) According to declaration of the consignor. The goods and instructions are accepted and dealt with suject to the Company's Standard Conditions Taken in charge in apparent good order and condition, unless otherwise noted herein, at the place of reciept for transport and delivery as mentioned above. Freight Payable At DESTINATION Freight Amount Cargo Insurance through the undersigned Not covered: Yes/ No Covered according to attached policy: Yes/ No No. of Original B/Lading ZERO For delivery of goods please apply to: PENANSHIN SHIPPING (THAILAND) LTD. 731/32 RATCHADAPISEK ROAD, BANGPONGPENG YANNAWA, BANGKOK 10120, THAILAND TEL: (662) 6839199, FAX: (662) 6839177-78 Place and Date of Issue HO CHI MINH 01 DEC, 2022"
substrings = [
    "PANALPINA WORLD TRANSPORT (VIETNAM) CO., LTD. AS AGENT FOR AND ON BEHALF OF PANTAINER LTD., 3/F HAI AU BUILDING 39B TRUONG SON ST, TAN BINH, HCMC, VIETNAM",
    "PANALPINA WORLD TRANSPORT (VIETNAM) AS AGENT FOR AND ON BEHALF OF PANTAINER LTD., SIRINRAT BUILDING, 14TH FLOOR 3388/47-49 NAMA IV ROAD KLONGTON, KLONGTOEY BANGKOK 10110",
    "SAME AS ABOVE",
    "HOCHIMINH ,CFS VIETNAM",
    "BANGKOK CFS",
    "BANGKOK CFS",
    "HCMBKK029112022",
    "HO CHI MINH 01 DEC, 2022",
    "1",
    "CTNS",
    "9.00",
    "KGS",
    "MAIN MATERIAL ACCESSIORIES FOR MARKING LADIES' UNDERWEAR",
    "1.000 M3",
    "CSLU2082865",
    "21567932"
]

# Find all occurrences for each substring
results = find_all_occurrences(text, substrings)

# Print the results
for substring, indices in results.items():
    if indices:
        print(f"The substring '{substring}' was found at the following indices: {indices}")
    else:
        print(f"The substring '{substring}' was not found.")