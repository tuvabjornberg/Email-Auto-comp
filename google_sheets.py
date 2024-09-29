import csv
import os


def fetch_google_emails_csv(file_path):
    emails = set()  # Avoid duplicates

    with open(file_path, mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) > 2 and row[2] != "Booking email":  # Emails in 3rd column
                email = row[2].strip()  # Strip any whitespace
                if email:
                    emails.add(email.lower())

    return emails


def fetch_all_google_emails(folder_path):
    all_emails = set()

    # All CSV files in the folder
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".csv"):
            file_path = os.path.join(folder_path, file_name)
            print(f"Processing {file_path}...")
            emails = fetch_google_emails_csv(file_path)
            all_emails.update(emails)  # Add emails from this CSV file to the set

    return all_emails
