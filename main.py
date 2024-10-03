import teamup as tu
import google_sheets as gs
from fuzzywuzzy import fuzz


def name_exists(teamup_info, google_sheet_emails):
    booking_name = teamup_info["Who"]

    for record in google_sheet_emails:
        if booking_name == record[0] + " " + record[1]:
            return record[2]  # Return google sheet email

    return False


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
    google_emails = [record[2] for record in google_sheet_all if record[2]]

    return [record for record in teamup_records if record["email"] not in google_emails]


def main():
    google_sheet_all = gs.fetch_all_google_emails("google_sheets_cvs_files")
    teamup_records = tu.fetch_all_teamup_records("teamup_bookings_cvs_files")

    invalid_records = comp_emails(google_sheet_all, teamup_records)

    if invalid_records:
        processed_emails = set()
        similar_emails = set()
        wrong_email_ok_name = []

        for record in invalid_records.copy():
            email = record["email"]

            if email in processed_emails:  # Check if email has already been processed
                continue

            ok_sim = is_similar_email(email, google_sheet_all, threshold=95)
            if ok_sim:
                similar_emails.add(email)
            else:
                ok_name = name_exists(record, google_sheet_all)
                if ok_name:
                    wrong_email_ok_name.append([record["Who"], ok_name, email])

                else:
                    # Print complete info for invalid records
                    print(
                        f"Invalid Booking: Name: {record['Who']}, \t\tEmail: {record['email']}, "
                        f"\tPrinter: {record['Calendar Name']}, \tDate: {record['Start Date']}"
                    )

            processed_emails.add(email)

        for sim_em in similar_emails:
            print(f"Probably typo email: {sim_em}")

        for name_exist in wrong_email_ok_name:
            print(
                f"License found, but mismatch in email. \nName: {name_exist[0]} \nGoogle: {name_exist[1]} \nTeamup: {name_exist[2]}\n"
            )

    else:
        print("OK: All emails are valid and match the Google Sheet.")


main()
