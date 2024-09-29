import csv
import os


def fetch_teamup_records_csv(file_path):
    records = []  # Store full records

    with open(file_path, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            email = row.get("email")
            if email:
                row["email"] = email.strip().lower()
                records.append(row)  # Store the full record

    return records


def fetch_all_teamup_records(folder_path):
    all_records = []

    # Process all CSV files in the folder
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".csv"):
            file_path = os.path.join(folder_path, file_name)
            records = fetch_teamup_records_csv(file_path)
            all_records.extend(records)  # Add records from this CSV file to the list

    return all_records
