import csv


def fetch_emails_from_teamup_csv(file_path):
    emails = set()  # avoid duplicates

    with open(file_path, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            email = row.get("email")  # 'email' column
            if email:
                emails.add(email.strip().lower())  # strip any whitespace

    return emails
