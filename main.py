import teamup as tu
import google_sheets as gs
from fuzzywuzzy import fuzz


def is_similar_email(email, google_sheet_emails, threshold):
    """
    Check if an email is sufficiently similar to any email in the Google Sheet list.
    95% similarity is acceptable.
    """
    for google_email in google_sheet_emails:
        if fuzz.ratio(email, google_email) >= threshold:
            return True
    return False


def comp_emails(google_sheet_all, teamup_records):
    # Emails in Teamup that aren't in the Google Sheet
    return [
        record for record in teamup_records if record["email"] not in google_sheet_all
    ]


def main():
    google_sheet_all = gs.fetch_all_google_emails("google_excel_sheets")
    teamup_records = tu.fetch_all_teamup_records("teamup_bookings")

    invalid_records = comp_emails(google_sheet_all, teamup_records)

    if invalid_records:
        processed_emails = set()
        similar_emails = set()

        for record in invalid_records.copy():
            email = record["email"]

            if email in processed_emails:  # Check if email has already been processed
                continue

            ok_email = is_similar_email(email, google_sheet_all, threshold=95)
            if ok_email:
                similar_emails.add(email)
            else:
                # Print complete info for invalid records
                print(
                    f"Invalid Booking: Name: {record['Who']}, \t\tEmail: {record['email']}, "
                    f"\tPrinter: {record['Calendar Name']}, \tDate: {record['Start Date']}"
                )

            processed_emails.add(email)

        for sim_em in similar_emails:
            print(f"Not exact, but similar to existing: {sim_em}")

    else:
        print("OK: All emails are valid and match the Google Sheet.")


main()
