import csv
import os


def fetch_google_emails_csv(file_path):
    records = []

    with open(file_path, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            
            if row[2] and row[2] != "Booking email" and row[2] != "Email":  # Emails in 3rd column
                row[2] = row[2].strip().lower()  # Strip any whitespace
                #if row["email"]:
                #print(row)
                records.append(row)
    return records


def fetch_all_google_emails(folder_path):
    all_records = []

    # All CSV files in the folder
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".csv"):
            file_path = os.path.join(folder_path, file_name)
            print(f"Processing {file_path}...")
            emails = fetch_google_emails_csv(file_path)
            all_records.extend(emails)  # Add emails from this CSV file to the set

    return all_records
