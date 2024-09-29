import csv


def fetch_emails_from_csv(file_path):
    emails = set()  # avoid duplicates

    with open(file_path, mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) > 2 and row[2] != "Booking email":  # emails in 3rd column
                email = row[2].strip()  # strip any whitespace
                if email:
                    emails.add(email.lower())

    return emails
